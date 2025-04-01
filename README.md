# DBBot

DBBot is an AI-driven Python library that converts natural language queries into SQL queries using OpenAI’s AutoGen, enabling seamless interaction with databases. It empowers developers and data analysts to retrieve and manipulate data effortlessly using plain English queries.

## Features
- **AI-Driven Query Generation**: Converts natural language questions into valid SQL queries using AutoGen.
- **Multi-Database Support**: Works with PostgreSQL, MySQL, and MongoDB.
- **Seamless Integration**: Easily integrates with your existing Python projects.
- **Flexible Setup**: Users provide their own database and OpenAI credentials.
- **Extensible**: Allows adding support for more databases or customizing AI behavior.
- **Logging & Debugging**: Built-in features to help troubleshoot queries.

## Installation
Install DBBot using pip:

```bash
pip install dbqna
```

## Requirements
- Python 3.6 or higher
- Required database drivers:
  - `psycopg2` for PostgreSQL
  - `pymysql` for MySQL
  - `pymongo` for MongoDB
- OpenAI API key (for using the GPT model)

## Setup
### Database Credentials
Provide the following details for database connection:
- **Host**
- **Port**
- **Database Name**
- **User**
- **Password**

### OpenAI Credentials
You'll need an OpenAI API key and additional configurations:
- **API Key**
- **Base URL**
- **API Version**
- **Deployment Name**

You can set these as environment variables in a `.env` file or provide them directly in the code.

## Usage
### 1. Initialize DBBot with OpenAI Credentials

```python
from dbqna import DBQnA

db_bot = DBQnA(
    azure_api_key="your-azure-api-key",
    azure_api_base="your-azure-api-base",
    azure_api_version="your-api-version",
    azure_deployment_name="your-deployment-name"
)
```

### 2. Provide Database Credentials

```python
from dbqna import DBHelper

db_helper = DBHelper(
    host="localhost",
    port="5432",
    database="your-database",
    user="postgres",
    password="your-password"
)
```

### 3. Query the Database Using Natural Language

```python
query = "how many work orders are there for tenant 1289?"
result = await db_bot.query_database(query)
print(result)
```

### 4. Example Response

```bash
Result: 
[
    ('work_order_count', 35)
]
```

## Contributing
We welcome contributions! Feel free to fork the repository, open issues, or submit pull requests to enhance DBBot.
