# Langchain-sql-agent
LangChain SQL Agent that converts natural language questions into SQL queries and fetches results from BigQuery. Easy-to-use, beginner-friendly example of AI-powered database automation.
# LangChain SQL Agents for BigQuery

This repository demonstrates how to build **SQL Agents using LangChain** that can convert natural language questions into SQL queries and fetch results from **Google BigQuery**.  
It includes examples using **Llama** and **Gemini** as the language models.

---

## Features

- Llama-based SQL Agent with LangChain + BigQuery  
- Gemini-based SQL Agent with LangChain + BigQuery  
- Converts user questions in natural language to SQL queries  
- Fetches query results directly from BigQuery  
- Beginner-friendly, easy to run in Jupyter Notebook  

---

## Requirements

Install the dependencies via `requirements.txt`:


pip install -r requirements.txt
Make sure you have a Google Cloud service account JSON key and BigQuery access.

Setup
Set your environment variables

Create a .env file in the root directory with:

GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
PROJECT_ID="your-gcp-project-id"
DATASET="your_bigquery_dataset"
Open the Jupyter Notebook

jupyter notebook
Run the cells in the notebook step by step.

Llama SQL Agent Example
Uses Llama via LangChain to generate SQL queries from natural language questions.

Fetches data from BigQuery.

Example usage in notebook:

question = "Show total sales last month"
result = llama_agent.run(question)
print(result)
Gemini SQL Agent Example
Uses Gemini model via LangChain to generate SQL queries from natural language questions.

Fetches data from BigQuery.

Example usage in notebook:

question = "List top 5 products by revenue"
result = gemini_agent.run(question)
print(result)
Notes
Make sure your BigQuery dataset and table names are correct.

Recommended to run in a Python 3.10+ environment.

Notebook is beginner-friendly and includes step-by-step instructions.
