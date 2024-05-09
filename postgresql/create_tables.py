from utilities import execute_commands

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
    
    execute_commands([command])

if __name__ == '__main__':
    create_tables()