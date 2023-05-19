import psycopg2
import os

class DatabaseHandler:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(database=os.environ['DB_NAME'], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"], host=os.environ["DB_HOST"], port=os.environ["DB_PORT"])
        self.cursor = self.connection.cursor()

    def insert_laptop_data(self, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        query = f"Insert into \"Laptop\" ({columns}) values({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def insert_smartphone_data(self, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        query = f"Insert into \"SmartPhone\" ({columns}) values({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()