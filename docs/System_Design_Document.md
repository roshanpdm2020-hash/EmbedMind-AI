EmbedMind AI — System Design Document
1. Problem Statement

Students and early-career developers often struggle to understand whether their code follows good programming practices. Existing AI tools frequently generate lengthy explanations or modify code unnecessarily, making learning more difficult.

EmbedMind AI addresses this problem by providing concise, structured, and actionable code analysis. The system uses Google's Gemini Large Language Model to identify the programming language, summarize the code's purpose, detect possible issues, suggest optimizations, recommend best practices, and generate an improved version while preserving the original functionality.

2. Objective

The objective of this project is to build a lightweight AI-powered code analysis assistant that:

Accepts source code from the user.
Analyzes the code using a Large Language Model.
Generates a structured review.
Suggests meaningful improvements.
Preserves the original logic and behavior.
3. Technology Stack
Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python, FastAPI
AI Model	Google Gemini API
API Communication	REST (JSON)
Version Control	Git & GitHub
4. System Architecture
                +----------------+
                |     User       |
                +--------+-------+
                         |
                         v
                +----------------+
                |   Frontend     |
                | (HTML + JS)    |
                +--------+-------+
                         |
                  HTTP POST Request
                         |
                         v
                +----------------+
                | FastAPI Server |
                |    (app.py)    |
                +--------+-------+
                         |
                  Prompt Generation
                         |
                         v
                +----------------+
                | Google Gemini  |
                |      API       |
                +--------+-------+
                         |
                  AI Generated Output
                         |
                         v
                +----------------+
                | FastAPI Server |
                +--------+-------+
                         |
                         v
                +----------------+
                | Frontend UI    |
                | Display Result |
                +----------------+
5. Workflow
Step 1

The user pastes source code into the web interface.

Step 2

JavaScript captures the input and sends it to the FastAPI backend through a POST request.

Step 3

The backend validates the request and constructs a carefully engineered prompt.

Step 4

The prompt is sent to the Google Gemini API.

Step 5

Gemini analyzes the code and generates:

Programming Language
Purpose
Bugs or Errors
Optimization Suggestions
Best Practices
Improved Version
Step 6

The backend receives the response from Gemini.

Step 7

The frontend renders the structured analysis for the user.

6. Prompt Design

A custom prompt was designed to ensure that the model generates consistent and practical outputs.

The prompt instructs the model to:

Keep responses concise.
Limit descriptive sections to short bullet points.
Avoid unnecessary explanations.
Preserve original functionality.
Suggest only meaningful optimizations.
Avoid cosmetic-only code changes.
Return "No significant improvements needed." when appropriate.

This prompt engineering approach improves consistency while reducing hallucinations and unnecessary verbosity.

7. Design Decisions and Trade-offs
Why FastAPI?
Lightweight and easy to develop with.
High performance for REST APIs.
Simple integration with AI services.
Why Google Gemini API?
Strong reasoning and code understanding.
Fast response times.
Free developer tier suitable for prototyping.
Why a Minimal Frontend?

The primary focus of this project is AI workflow and backend integration rather than UI complexity. A simple interface improves usability and keeps the project lightweight.

8. Limitations

Current limitations include:

Supports analysis of one code snippet at a time.
No syntax highlighting.
No file upload functionality.
Requires an active internet connection.
Depends on Gemini API availability.
9. Future Improvements

Potential future enhancements include:

Multi-file project analysis.
Syntax highlighting.
File upload support.
PDF export of reports.
User authentication.
Support for multiple LLM providers.
10. Conclusion

EmbedMind AI demonstrates how a Large Language Model can be integrated into a practical developer productivity tool. By combining a lightweight frontend, a FastAPI backend, and Google's Gemini API, the system delivers structured code analysis in real time. The project helps students and early-career developers quickly understand their code and improve their programming practices through clear, AI-assisted feedback.