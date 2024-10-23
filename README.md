# LLM Endpoint for Product Classification

This project provides an API for classifying product descriptions into predefined categories using a local instance of the Ollama LLM (`llama3.1`). The API is built with FastAPI and includes a CORS-enabled endpoint for classification, along with a simple test harness for interacting with the API.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Test Harness](#test-harness)
- [Logging](#logging)
- [License](#license)

## Features

- **FastAPI Endpoint**: Provides a `/classify` POST endpoint that accepts a product description, categories, and the model name for classification.
- **LLM Integration**: Utilizes the local Ollama LLM for classification, customizable by specifying the model version (default: `llama3.1`).
- **CORS Support**: Configured to allow cross-origin requests, enabling seamless integration with front-end applications.
- **Test Harness**: A simple HTML/JS front-end to interact with the API.

## Requirements

- Python 3.10 or higher
- FastAPI
- Uvicorn
- `langchain_ollama`
- `langchain_core`
- `pydantic`
- JavaScript (for the test harness)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/llm-endpoint.git
    cd llm-endpoint
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure that Ollama LLM is running locally and accessible.

## Usage

1. **Start the API server**:

    You can run the FastAPI server locally using Uvicorn:

    ```bash
    uvicorn classify:app --reload
    ```

   The server will be accessible at `http://127.0.0.1:8000`.

2. **Test the API**:

   You can use tools like Postman or `curl` to interact with the API:

    ```bash
    curl -X POST "http://127.0.0.1:8000/classify" \
    -H "Content-Type: application/json" \
    -d '{
      "description": "A smartphone with 128GB storage and 6GB RAM.",
      "categories": ["Electronics", "Clothing", "Home Appliances"],
      "model_name": "llama3.1"
    }'
    ```

   This will classify the product description and return the most appropriate category.

## API Documentation

- **Endpoint**: `/classify`
- **Method**: `POST`
- **Request Body**:

  - `description`: A string describing the product.
  - `categories`: A list of categories (strings) to classify the product into.
  - `model_name`: (Optional) The name of the LLM model to use. Default is `llama3.1`.

- **Response**:

  - If successful, the response will contain the classified category:
  
    ```json
    {
      "category": "Electronics"
    }
    ```

  - If there's an error, it will return an error message:

    ```json
    {
      "error": "Error message"
    }
    ```

## Test Harness

A simple HTML/JS-based test harness is included in the `test-harness` directory. This allows you to easily test the API in a browser environment.

To use the test harness:

1. Open `test-harness/test-harness.html` in a browser.
2. Enter the product description, categories, and model name.
3. Click the "Submit" button to send a request to the API.
4. The response from the API will be displayed in the browser.

## Logging

This project includes logging to help track requests and responses during classification.

- Logs are configured at the `INFO` level by default. You can modify the logging level in the script to include `DEBUG` messages if needed:

    ```python
    logging.basicConfig(
        level=logging.INFO,  # Change to DEBUG for more detailed logging
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    ```

Logs are output to the console and include details such as product descriptions, categories, and model responses.
