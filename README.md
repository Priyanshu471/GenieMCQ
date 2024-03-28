# GenieMCQ

## Purpose

GenieMCQ is designed to automatically generate multiple-choice questions (MCQs) from the content of PDF or Text files. This tool aims to assist educators, content creators, and students in creating quizzes and study materials efficiently, without the need for manual question formulation.

## Technology and Libraries Used

- **Python**: The primary programming language used for developing GenieMCQ.
- **Flask**: A micro web framework written in Python, used for setting up the web server.
- **PyPDF2**: A Pure-Python library built as a PDF toolkit. It is used for extracting text from PDF files.
- **openai**: Utilized for accessing OpenAI's API for generating questions based on the text extracted from PDFs.
- **langchain**: A library for working with language models, used in conjunction with OpenAI's API for generating and evaluating MCQs.
- **python-dotenv**: Used for loading environment variables from a .env file, which includes API keys for OpenAI.

## Requirements

Python 3.6 or later is required to run GenieMCQ.

## Future Scope

In the future, I plan to develop a full-fledged frontend for GenieMCQ to enhance user experience significantly. This will allow users to manage their generated MCQs more efficiently and interactively. Additionally, the application will introduce different subscription plans to cater to various user needs, ranging from individual educators to large educational institutions.

## User requirements

User will have to provide a file, number of questions, subject and the difficulty level and the rest of the thing will be handled by backend.

### Testing

For testing the application you have to clone this application to your local machine

1. Open your terminal.
2. Navigate to the directory where you want to clone the repository.
3. Use the command `git clone https://github.com/Priyanshu471/GenieMCQ.git` to clone the repository.
4. Once the cloning is complete, navigate to the project directory using the command `cd GenieMCQ`.
5. Run app.py file to run the server.
6. Send data to server at `/generate`.

- file - pdf or text
- number - number of questions (for testing please keep it upto 5)
- subject - subject related to file you have given
- hardness - difficulty level of questions

You can play around with llm, prompts to explore.
I am testing and analysing different LLMs for making it cost effective.
