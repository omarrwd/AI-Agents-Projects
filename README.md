<div align="center">
  
# 🤖 The Journey of 10 AI Agent Projects 🤖

**_Building Simple AI Agents with Free and Accessible Tools Using the CrewAI Framework_**

![Agents Banner](https://img.shields.io/badge/AI%20Agents-Journey-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-brightgreen?style=flat-square)
![CrewAI](https://img.shields.io/badge/CrewAI-Powered-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

</div>

## 🌟 Introduction

Welcome to my journey of creating 10 simple projects for AI agents using free tools! (I will try to use free tools as much as possible) each project designed to solve specific problem.

### 📋 Projects Goals

- Build a foundation for more complex multi-agent systems to gain experience.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🤖 project  #1: Resume Checker

The first project in this collection is the Resume Checker—an AI-powered tool that searches the internet for best practices to create resumes that pass Applicant Tracking Systems (ATS). It then analyzes your resume against these practices to enhance its effectiveness.

### ✨ Features

- **ATS Optimization Research**: Automatically researches the latest best practices for ATS optimization
- **Resume Analysis**: Provides detailed feedback on how well your resume meets ATS requirements
- **Specific Improvement Suggestions**: Delivers actionable recommendations for enhancing your resume
- **PDF Processing**: Extracts and processes text from PDF resumes

### 🛠️ How It Works

This project uses a multi-agent system powered by CrewAI:

1. **Resume Researcher Agent**: Searches for and compiles the latest best practices for ATS optimization
2. **Resume Analyzer Agent**: Takes your resume and the research results to generate detailed feedback

The agents work sequentially to provide comprehensive analysis based on up-to-date information.

## 🚀 Getting Started

### Prerequisites

- Python 3.11
- OpenRouter API key (to use free LLMs)

## Setup Options
### Option A: Using CrewAI Framework
first of all you should install the framework from [crewai install](https://docs.crewai.com/installation)
Then: 
1. git clone   ``` https://github.com/omarrwd/AI-Agents-Projects ```
2. cd ``` resume_checker_agent  ```
3. Install dependencies:
   ```bash
   crewai install

   ```

4. Create a `.env` file with your API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```
   
5. If you need to install additional packages (this is from crew ai Docs), use:
   ```
   uv add <package-name>:
   ```

6. if there is error of PyPDF2 package or any package you can try install it, use:
   ```
   uv add <package-name>:
   ```

### Option B: Using CrewAI as Python library 

1. git clone   ``` https://github.com/omarrwd/AI-Agents-Projects ```
2. cd ``` resume_checker_agent  ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

   ```

4. Create a `.env` file with your API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

5. if there is error of PyPDF2 package or any package you can try install it, use:
   ```
   pip install <package_name>
   ```
### Usage

1. put your resume PDF file in the `knowledge` folder
2. write the name of the resume in main.py in ```     resume_path = os.path.join('knowledge', 'replace_with_resume_file_name.pdf') ```
3. Run the resume checker:
   
   A. if you are using crewai framework:
   ```bash
   crewai run
   ```
   B. if you are using crewai as python library
      ```bash
   python main.py
   ```
   
4. Review the output in output folder

## 📝 Configuration

The agent behavior can be configured through YAML files:

- `config/agents.yaml`: Defines agent roles, goals, and backstories
- `config/tasks.yaml`: Specifies the tasks and expected outputs

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 📝 Note

I am a beginner in AI agent development, and this is my first project in this domain. While I have set specific goals and roles for agents, I acknowledge that there is ample room for improvement. If you have suggestions for better-defined goals, roles, better structure , or any other enhancements, I am eager to learn from your insights. Your feedback will be invaluable as I continue my learning journey.


## 📄 License

This project is licensed under the MIT License.
