from dbqna import DBQnA
from dbqna.db_helper import DBHelper

# Set up Database Connection
db_helper = DBHelper(
    host="localhost",
    port="5432",
    database="DatabaseName",
    user="postgres",
    password="yourpassword"
)

# Set up AI Connection
dbqna = DBQnA(
    azure_api_key="your-azure-api-key",
    azure_api_base="your-azure-api-base",
    azure_api_version="your-azure-api-version",
    azure_deployment_name="your-azure-deployment-name"
)

# Example Query
query = "Show all employees"
result = dbqna.query_database(query)

print("Result:", result)
