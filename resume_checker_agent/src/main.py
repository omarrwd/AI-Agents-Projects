import os
from .crew import load_config, extract_resume_text, ResumeCheckerCrew

def run():
    # Define the path to the resume PDF in the knowledge folder
    resume_path = os.path.join('src', 'knowledge', 'Omar-Rashed-Hassan.pdf')
    resume_text = extract_resume_text(resume_path)
    # Load agents and tasks configurations
    agents_config = load_config('src/config/agents.yaml')
    tasks_config = load_config('src/config/tasks.yaml')
    
    # Initialize crew and kick off the tasks with the provided input
    crew_instance = ResumeCheckerCrew(agents_config, tasks_config)
    inputs = {
        'resume_content': resume_text
    }
    response = crew_instance.crew().kickoff(inputs=inputs)
    
    print("\n--- RESUME ANALYSIS RESULTS ---\n")
    print(response)

if __name__ == "__main__":
    run()