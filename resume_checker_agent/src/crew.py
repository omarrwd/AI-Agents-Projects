import os
import yaml
import PyPDF2
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from tools.search_tool import DuckDuckGoTool

# Load environment variables
load_dotenv()
def load_config(path: str) -> dict:
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def extract_resume_text(pdf_path: str) -> str:
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

class ResumeCheckerCrew:
    def __init__(self, agents_config: dict, tasks_config: dict):
        self.llm = LLM(
            model="openrouter/qwen/qwq-32b:free",
            base_url="https://openrouter.ai/api/v1",
            temperature=1,
            api_key=os.getenv('OPENROUTER_API_KEY')
        )

        # Initialize agents from configuration
        self.researcher = Agent(
            role=agents_config['resume_researcher']['role'],
            goal=agents_config['resume_researcher']['goal'],
            backstory=agents_config['resume_researcher']['backstory'],
            verbose=True,
            tools=[DuckDuckGoTool()],
            llm=self.llm
        )
        self.analyzer = Agent(
            role=agents_config['resume_analyzer']['role'],
            goal=agents_config['resume_analyzer']['goal'],
            backstory=agents_config['resume_analyzer']['backstory'],
            verbose=True,
            llm=self.llm
        )

        # Create tasks and assign corresponding agents
        self.research_task = Task(
            description=tasks_config['resume_research_task']['description'],
            expected_output=tasks_config['resume_research_task']['expected_output'],
            agent=self.researcher,
            output_file='output/research_task.md' # This is the file that will be contain the final report.
            
        )
        self.analysis_task = Task(
            description=tasks_config['resume_analysis_task']['description'],
            expected_output=tasks_config['resume_analysis_task']['expected_output'],
            agent=self.analyzer,
            context=[self.research_task],
             output_file='output/analysis_task.md' # This is the file that will be contain the final report.

        )

    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher, self.analyzer],
            tasks=[self.research_task, self.analysis_task],
            process=Process.sequential,
            verbose=True,
        )