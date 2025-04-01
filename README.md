#DBBot
DBBot is an AI-driven Python library that allows users to convert natural language queries into SQL queries using OpenAI’s AutoGen and seamlessly interact with databases. It's designed to help developers and data analysts quickly retrieve and manipulate data by simply asking questions in plain English.

Features
AI-driven query generation: Convert natural language questions into valid SQL queries using AutoGen.

Supports multiple databases: Works with PostgreSQL, MySQL, and MongoDB.

Seamless integration: Easily integrates with your existing Python projects.

Flexible setup: Users can provide their own database and OpenAI credentials.

Extensible: Add support for more databases or customize the AI’s behavior.

Installation
To install DBBot, run the following command:

bash
Copy
Edit
pip install dbqna
Requirements
Python 3.6 or higher

psycopg2 for PostgreSQL, pymysql for MySQL, or pymongo for MongoDB

OpenAI API key (for using the GPT model)

Setup
Database credentials: You'll need to provide the following database connection details:

Host

Port

Database name

User

Password

OpenAI credentials: You’ll need an OpenAI API key, base URL, version, and deployment name for GPT integration.

Environment Variables: Set your credentials in the .env file or provide them directly when initializing the DBBot class.

Usage Example
1. Initialize DBBot with credentials
python
Copy
Edit
from dbqna import DBBot

db_bot = DBBot(
    azure_api_key="your-azure-api-key",
    azure_api_base="your-azure-api-base",
    azure_api_version="ver",
    azure_deployment_name="name"
)

# Query example
query = "how many users signed up this month?"
result = await db_bot.query_database(query)
print(result)
2. Provide Database Credentials
python
Copy
Edit
db_helper = DBHelper(
    host="localhost",
    port="5432",
    database="Database",
    user="postgres",
    password="postgres"
)
3. Query the database using natural language
Simply pass your query as a string to the query_database function.

python
Copy
Edit
result = await db_bot.query_database("how many work orders are there for tenant 1289?")
4. Response Example
bash
Copy
Edit
Result: 
[
    ('work_order_count', 35)
]

Contributing
Feel free to fork this repository, open issues, and submit pull requests. All contributions are welcome!