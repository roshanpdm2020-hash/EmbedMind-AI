EmbedMind AI — System Design Document
1. Problem Statement

Students and beginner developers often receive AI-generated code reviews that are either too verbose or inconsistent. Many tools explain every line of code instead of providing a concise summary of the program's purpose, potential issues, optimization suggestions, best practices, and an improved version.

EmbedMind AI solves this by providing a structured, easy-to-read analysis using a Large Language Model (Google Gemini API).

2. Objective

Build a lightweight AI-powered code analysis assistant that:

Accepts source code from the user.
Sends it to a Large Language Model.
Returns a structured analysis.
Generates an improved version of the code while preserving functionality.
3. Technology Stack
Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python, FastAPI
AI Model	Google Gemini API
Communication	REST API (JSON)
Version Control	Git & GitHub
4. System Architecture
+----------------+
|     User       |
+--------+-------+
         |
         v
+----------------+
| Frontend (HTML |
| + JavaScript)  |
+--------+-------+
         |
   HTTP POST
         |
         v
+----------------+
| FastAPI Server |
|   (app.py)     |
+--------+-------+
         |
  Prompt Creation
         |
         v
+----------------+
| Google Gemini  |
|      API       |
+--------+-------+
         |
 AI Generated Analysis
         |
         v
+----------------+
| FastAPI Server |
+--------+-------+
         |
         v
+----------------+
| Frontend UI    |
| Displays Result|
+----------------+
5. Workflow
Step 1

The user pastes source code into the web interface.

Step 2

JavaScript captures the input and sends it as a POST request to the FastAPI backend.

Step 3

The backend validates the request and constructs a carefully designed prompt.

Step 4

The prompt is sent to Google Gemini API.

Step 5

Gemini analyzes the code and returns:

Programming language
Purpose
Bugs or errors
Optimization suggestions
Best practices
Improved version
Step 6

The backend forwards the response to the frontend.

Step 7

The frontend renders the analysis in a clean formatted output.

6. Prompt Design

The prompt was engineered to ensure:

Concise output.
Maximum two bullet points per section.
No unnecessary explanations.
Preservation of original functionality.
No cosmetic-only code modifications.
Return "No significant improvements needed." when appropriate.

This prompt engineering approach improves consistency and reduces hallucinations.

7. Design Decisions and Trade-offs
Why FastAPI?
Lightweight.
Easy REST API creation.
Excellent performance.
Why Gemini API?
Fast response time.
Strong reasoning capability.
Free developer quota.
Why Simple Frontend?

The focus of this project is AI workflow rather than UI complexity. A minimal interface reduces distractions and improves usability.

8. Limitations
Currently supports single code snippet analysis.
No syntax highlighting.
No file upload feature.
Depends on internet connectivity and Gemini API availability.
9. Future Improvements
Multi-file project analysis.
Syntax highlighting.
Authentication system.
PDF export of analysis.
Support for multiple LLM providers.
10. Conclusion

EmbedMind AI demonstrates how a Large Language Model can be integrated into a practical developer tool. The project combines a lightweight web interface, a FastAPI backend, and Google's Gemini API to deliver structured code analysis in real time, making it useful for students and early-career developers.