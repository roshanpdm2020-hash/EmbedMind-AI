# EmbedMind AI

An AI-powered code analysis and optimization assistant built for students and early-career developers.

## Features

- Detects programming language automatically (C, C++, Python, Arduino)
- Explains the purpose of the code
- Identifies bugs or errors
- Suggests optimization opportunities
- Recommends coding best practices
- Generates an improved version when necessary
- Uses Google's Gemini API for real-time AI analysis

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Google Gemini API

## Project Structure

```
EmbedMind-AI/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   └── script.js
│
└── .gitignore
```

## Installation

```bash
git clone <repository-url>
cd EmbedMind-AI
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Create a `.env` file inside `backend/`:

```
GEMINI_API_KEY=your_api_key_here
```

Run the backend:

```bash
cd backend
python -m uvicorn app:app --reload
```

Open `frontend/index.html` using Live Server.

## Future Improvements

- Multi-file project analysis
- Drag and drop code upload
- PDF report export
- Deployment on Vercel/Render
- Authentication and user history

## Author

Roshan R