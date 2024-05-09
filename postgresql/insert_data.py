import csv
import psycopg2
from config import load_config

def _format_row(row):
    def cast(row_str):
        try:
            return int(float(row_str))
        except ValueError:
            return 0 # NOTE: Questionable return here, considering this is empty data, not actually zero
        
    return [row[0], cast(row[1]), cast(row[2]), cast(row[3]), cast(row[4])]

def insert_data():
    data_dir = r'C:/Users/cam/Desktop/Workspaces/Data/HmData/'
    file_ext = ".csv"
    filenames = ["27", "28", "97", "98", "99"]

    filepaths = []
    for filename in filenames:
        filepaths.append(data_dir + filename + file_ext)
    

    sql_commands = []
    for filename, filepath in zip(filenames, filepaths):
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row
            
            for row in reader:
                sql_commands.append(
                    ("INSERT INTO vendor_clients (vendor_id, arrival_time, order_time, wait, payment, total_time) VALUES (%d, '%s', %d, %d, %d, %d)" %
                    (int(filename), *_format_row(row)))
                )
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in sql_commands:
                    cur.execute(command)
                
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    insert_data()