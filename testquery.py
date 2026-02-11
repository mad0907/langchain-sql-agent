from google.cloud import bigquery
import pandas as pd
from llm import get_llm
from config import GOOGLE_PROJECT_ID, FULL_TABLE_ID
import re

llm = get_llm()
client = bigquery.Client(project=GOOGLE_PROJECT_ID)
FULL_TABLE=FULL_TABLE_ID

SCHEMA = """
Table: orders
Columns:
order_id INTEGER
customer_id INTEGER
customer_name STRING
city STRING
product_category STRING
amount FLOAT
payment_mode STRING
order_date DATE
delivery_days INTEGER
status STRING
"""



def generate_sql(question: str) -> str:
    prompt = f"""
You are a BigQuery SQL expert.

Table Name: {FULL_TABLE}

Columns:
order_id INTEGER
customer_id INTEGER
customer_name STRING
city STRING
product_category STRING
amount FLOAT
payment_mode STRING
order_date DATE
delivery_days INTEGER
status STRING

Rules:
- Always use FULL table name: {FULL_TABLE}
- Revenue column = amount
- Date column = order_date
- BigQuery syntax only
- Return ONLY SQL.

User Question: {question}
"""


    response = llm.invoke(prompt)
    return response.content.strip()



def clean_sql(sql: str) -> str:
    sql = re.sub(r"\bCURRENT_DATE\b(?!\s*\()", "CURRENT_DATE()", sql)

    # Fix interval quotes
    sql = sql.replace("INTERVAL '1 month'", "INTERVAL 1 MONTH")
    sql = sql.replace("INTERVAL '1 MONTH'", "INTERVAL 1 MONTH")

    # Remove accidental double parentheses
    sql = sql.replace("()()", "()")

    # FORCE full table name if LLM forgets
    sql = sql.replace("FROM orders", f"FROM `{FULL_TABLE}`")

    # REMOVE strict last-month filter if present
    if "DATE_SUB(CURRENT_DATE()" in sql.upper():
        sql = re.sub(r"WHERE.*DATE_SUB.*", "", sql, flags=re.IGNORECASE)

    return sql





def run_query_df(question: str) -> pd.DataFrame:
    sql = clean_sql(generate_sql(question))
    print("Generated SQL:\n", sql)

    df = client.query(sql).to_dataframe()
    return df


def run_query_json(question: str):
    df = run_query_df(question)
    return df.to_dict(orient="records")
