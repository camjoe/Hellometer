import psycopg2
from config import load_config

def execute_commands(commands):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)