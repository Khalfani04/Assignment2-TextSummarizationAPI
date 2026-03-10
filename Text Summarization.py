"""
Text Summarization API
======================
Model:   facebook/bart-large-cnn (Hugging Face Transformers)
Server:  FastAPI
Deploy:  Google Cloud Run (Docker)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

# -------------------------------------------------------------------
# App setup
# -------------------------------------------------------------------
app = FastAPI(
    title="Text Summarization API",
    description="Summarizes text using Facebook's BART large CNN model.",
    version="1.0.0"
)

# Load model once on startup (not per request)
print("Loading BART model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("Model loaded.")


# -------------------------------------------------------------------
# Request / Response schemas
# -------------------------------------------------------------------
class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30


class SummarizeResponse(BaseModel):
    original_length: int
    summary: str
    summary_length: int


# -------------------------------------------------------------------
# Routes
# -------------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Text Summarization API is running. Go to /docs to test it."}


@app.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    """
    Accepts a body of text and returns a summarized version.

    - **text**: The input text to summarize (required)
    - **max_length**: Maximum length of the summary (default: 130)
    - **min_length**: Minimum length of the summary (default: 30)
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text field cannot be empty.")

    if len(request.text.split()) < 30:
        raise HTTPException(
            status_code=400,
            detail="Input text is too short to summarize. Please provide at least 30 words."
        )

    try:
        result = summarizer(
            request.text,
            max_length=request.max_length,
            min_length=request.min_length,
            do_sample=False
        )
        summary = result[0]["summary_text"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")

    return SummarizeResponse(
        original_length=len(request.text.split()),
        summary=summary,
        summary_length=len(summary.split())
    )


# -------------------------------------------------------------------
# Run locally (without Docker)
# -------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
