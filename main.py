import os
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Define the input data structure using Pydantic
class SummarizeInput(BaseModel):
    text: str

# Define the output data structure using Pydantic
class SummaryOutput(BaseModel):
    summary: str

# Initialize the summarization pipeline using the pre-trained BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Create a FastAPI application instance
app = FastAPI()

# Define the API endpoint for summarization
@app.post("/summarize", response_model=SummaryOutput)
async def summarize_text(input_data: SummarizeInput):
    """
    Takes text as input and returns a summarized version.
    """
    summary = summarizer(input_data.text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return SummaryOutput(summary=summary)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Get PORT from environment variable, default to 8000 for local
    uvicorn.run(app, host="0.0.0.0", port=port)