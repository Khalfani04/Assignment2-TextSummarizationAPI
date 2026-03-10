# 📝 Text Summarization API

> A production-deployed REST API that summarizes text using a pre-trained BART model — containerized with Docker and hosted on Google Cloud Run.

---

## Overview

This project builds and deploys a text summarization API using Facebook's `bart-large-cnn` model from Hugging Face Transformers. The API is served with FastAPI, containerized with Docker, and deployed to Google Cloud Run for scalable, real-world use.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud_Run-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

---

## Architecture

![Architecture Diagram](https://github.com/user-attachments/assets/f6000452-55aa-467f-bd8e-001bf4337a65)

1. Client sends a **POST request** to the `/summarize` endpoint
2. Request is received by **Google Cloud Run** (containerized, auto-scaling)
3. **FastAPI** backend processes the request
4. **BART model** (`facebook/bart-large-cnn`) generates the summary
5. Summarized text is returned as a **JSON response**

---

## How to Run Locally (Docker)

```bash
# 1. Clone the repository
git clone https://github.com/Khalfani04/text-summarization-api
cd text-summarization-api

# 2. Build the Docker image
docker build -t text-summarization-api .

# 3. Run the container
docker run -p 8000:8000 text-summarization-api
```

Once running, open your browser and go to:

```
http://localhost:8000/docs
```

This opens the auto-generated FastAPI documentation where you can test the API directly.

---

## API Usage

**Endpoint:** `POST /summarize`

**Request body:**
```json
{
  "text": "Your long text here..."
}
```

**Response:**
```json
{
  "summary": "Condensed version of your text."
}
```

---

## Deployment (Google Cloud Run)

```bash
# Tag and push image to Artifact Registry
docker tag text-summarization-api \
  northamerica-northeast2-docker.pkg.dev/text-summarization-api-455107/text-summarization-repo/text-summarization-api:latest

docker push \
  northamerica-northeast2-docker.pkg.dev/text-summarization-api-455107/text-summarization-repo/text-summarization-api:latest

# Deploy to Cloud Run
gcloud run deploy text-summarization-api \
  --image=northamerica-northeast2-docker.pkg.dev/text-summarization-api-455107/text-summarization-repo/text-summarization-api:latest \
  --platform=managed \
  --region=northamerica-northeast2 \
  --allow-unauthenticated \
  --memory=4Gi
```

| Setting | Value |
|---|---|
| Platform | Google Cloud Run |
| Region | northamerica-northeast2 |
| Memory | 4Gi |
| Auth | Public (unauthenticated) |

---

## Target Users

This API is designed for developers and applications that need fast, accurate text summarization — including content aggregators, news platforms, and any system processing large volumes of text.

---

## What I Learned

- How to serve a Hugging Face model as a REST API using FastAPI
- How to containerize a Python ML application with Docker
- How to deploy and scale a containerized API on Google Cloud Run

---

## Contact

**Khalfani Norman** · [LinkedIn](https://www.linkedin.com/in/YOUR-LINKEDIN) · [GitHub](https://github.com/Khalfani04)
