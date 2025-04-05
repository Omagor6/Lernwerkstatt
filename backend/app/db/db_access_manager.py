import psycopg2
from psycopg2 import DatabaseError, OperationalError
from psycopg2.extras import RealDictCursor
import json
from fastapi import HTTPException, status


def __load_db_config():
    config_file = "app\\db\\config.json"
    try:
        with open(config_file, "r") as file:
            return json.load(file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error loading database configuration. Please try again later.",
        )

# used to persist / update 
def execute_query(query, params=None):
    db_config = __load_db_config()
    try:
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                connection.commit()
                affected_rows = cursor.rowcount
                return affected_rows
    except OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection error. Please try again later."
        )
    except DatabaseError as e:        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while executing the query. Please try again later."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred. Please try again later."
        )

# used to fetch data from db
def fetch_query_results_as_dict(query, params=None):
    db_config = __load_db_config()
    try:
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                results = cursor.fetchall()
                return results
    except OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection error. Please try again later.",
        )
    except DatabaseError as e:
        print(e)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching query results. Please try again later.",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred. Please try again later.",
        )
