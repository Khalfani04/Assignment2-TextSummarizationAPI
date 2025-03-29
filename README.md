# Text Summarization API

## Overview

This project implements a simple API for text summarization. It uses a pre-trained BART model from Hugging Face Transformers, served using FastAPI and deployed on Google Cloud Run.

## Setup Instructions (for local testing with Docker)

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd <YOUR_REPOSITORY_DIRECTORY>
    ```
    (Replace `<YOUR_REPOSITORY_URL>` and `<YOUR_REPOSITORY_DIRECTORY>` with your actual repository details)

2.  **Ensure Docker is installed:** You need to have Docker installed on your system to run the container locally.

3.  **Build the Docker image:**
    ```bash
    docker build -t text-summarization-api .
    ```

4.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 text-summarization-api
    ```
    This will start the API server inside the container, mapping port 8000 of the container to port 8000 on your local machine.

5.  **Access the API documentation:** Once the container is running, you can access the automatically generated API documentation at:
    `http://localhost:8000/docs`

## API Users

* **Target users:** Developers and applications that need to quickly summarize text content. This could include content aggregators, news platforms, or any application dealing with large amounts of textual data.
* **Expected daily request volume:** Moderate, estimated to be in the range of a few hundred to a few thousand requests per day, depending on the integration and usage.
* **User requirements:** Users expect real-time summarization with reasonable accuracy and conciseness. The API should be able to handle various lengths of input text within a reasonable timeframe.

## Architecture

![image](https://github.com/user-attachments/assets/c0c75376-e954-4e13-a7dd-d9df5d2f68b9)


The Text Summarization API follows a simple architecture:

1.  A client (user or application) sends a **POST request** to the `/summarize` endpoint of the deployed API.
2.  The API is hosted on **Google Cloud Run**, which manages the containerized application.
3.  The backend of the API, built with **FastAPI**, receives the request containing the text to be summarized.
4.  It utilizes a **pre-trained BART model** (`facebook/bart-large-cnn`) from the Hugging Face Transformers library to perform the summarization.
5.  The summarized text is then returned to the client as a **JSON response**.

## Deployment

The API was deployed to Google Cloud Run using the following steps:

1.  A Docker image was built using the provided `Dockerfile`.
2.  The Docker image was tagged and pushed to Google Cloud Artifact Registry in the `northamerica-northeast2` region under the project `text-summarization-api-455107` and repository `text-summarization-repo`.
3.  The service was deployed to Cloud Run using the following command:
   ```bash
   gcloud run deploy text-summarization-api \
       --image=northamerica-northeast2-docker.pkg.dev/text-summarization-api-455107/text-summarization-repo/text-summarization-api:latest \
       --platform=managed \
       --region=northamerica-northeast2 \
       --allow-unauthenticated \
       --memory=4Gi
