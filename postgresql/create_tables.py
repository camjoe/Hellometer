import psycopg2
from config import load_config

def create_tables():
    command = """
        CREATE TABLE vendor_clients (
                id SERIAL PRIMARY KEY,
                vendor_id INTEGER NOT NULL,
                arrival_time TIMESTAMP NOT NULL,
                order_time INTEGER NOT NULL,
                wait INTEGER NOT NULL,
                payment INTEGER NOT NULL,
                total_time INTEGER NOT NULL
        )
        """
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()