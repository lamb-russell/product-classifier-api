from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Create a logger object
logger = logging.getLogger(__name__)

# FastAPI instance
app = FastAPI()

# Enable CORS middleware to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. For production, specify allowed origins.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# Pydantic model for input validation
class ClassificationRequest(BaseModel):
    description: str
    categories: List[str]
    model_name: str = "llama3.1"


# Function to classify a product using the local Ollama LLM
def classify_product(description: str, categories: List[str], model_name: str = "llama3.1") -> str:
    llm = OllamaLLM(model=model_name)

    prompt_template = """
    You are an expert product classifier. Given the following product description and list of categories, choose the most appropriate category for the product.
    Since this output will be used by other automated processing, only respond with the category name that matches the product description.

    Product Description: {description}

    Categories: {categories}

    The best category for the product is:
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    categories_str = ", ".join(categories)

    response = chain.run({
        "description": description,
        "categories": categories_str
    })

    logger.info(f"Product Description: {description}")
    logger.info(f"Categories: {categories}")
    logger.info(f"Model Response: {response}")

    return response.strip()


# FastAPI endpoint to classify products
@app.post("/classify")
async def classify_product_endpoint(request: ClassificationRequest):
    try:
        category = classify_product(request.description, request.categories, request.model_name)
        return {"category": category}
    except Exception as e:
        logger.error(f"Error classifying product: {e}")
        return {"error": str(e)}
