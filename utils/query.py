import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="tIDurBDfmgUuD3TOcscW",
                                  host="containers-us-west-156.railway.app",
                                  port="8035",
                                  database="railway")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    cursor.execute("SET search_path TO sirest")
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
# finally:
#     if (connection):
#         # cursor.close()
#         # connection.close()
#         print("PostgreSQL connection is closed")