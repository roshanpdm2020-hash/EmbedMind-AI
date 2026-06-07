from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ==========================
# Load Environment Variables
# ==========================

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================
# Load Gemini Model
# ==========================

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================
# FastAPI App
# ==========================

app = FastAPI(
    title="EmbedMind AI",
    description="AI Powered Embedded Code Assistant",
    version="1.0"
)

# ==========================
# Enable CORS
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Input Model
# ==========================

class CodeRequest(BaseModel):
    code: str

# ==========================
# Home Route
# ==========================

@app.get("/")
def home():
    return {
        "project": "EmbedMind AI",
        "status": "Backend Running Successfully"
    }

# ==========================
# Analyze Route
# ==========================

@app.post("/analyze")
def analyze(data: CodeRequest):

    prompt = f"""
You are an expert Embedded Systems and Software Engineer.

Analyze the following source code.

Automatically identify whether it is:
- C
- C++
- Python
- Arduino

Return ONLY in this exact format.

Programming Language:
- <language>

Purpose:
- One short bullet.

Bugs or Errors:
- Mention errors if any.
- Otherwise write: None.

Optimization Suggestions:
- Maximum 2 short bullets.

Best Practices:
- Maximum 2 short bullets.

Improved Version:
- If no significant improvements are needed, write exactly:
  No significant improvements needed.
- Otherwise, return only the improved source code.
- Preserve the original functionality and logic.
- Do not make cosmetic or style-only changes.
- Do not remove code that improves readability.
- Do not include explanations or markdown code fences.

Rules:
- Keep the response concise.
- Keep the descriptive sections under 150 words total.
- Do not write introductions or conclusions.
- Do not explain every line of code.
- Only suggest meaningful optimizations.
- Preserve the original behavior and logic.
- Avoid over-engineering simple examples.
- Do not recommend changes based solely on personal coding style.
- If the code is already clean and correct, explicitly state: "No significant improvements needed."
- In that case, do NOT return the code again in the Improved Version section.

Source Code:

{data.code}
"""

    response = model.generate_content(prompt)

    return {
        "analysis": response.text
    }