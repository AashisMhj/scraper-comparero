import psycopg2
import os

class DatabaseHandler:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(database=os.environ['DB_NAME'], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"], host=os.environ["DB_HOST"], port=os.environ["DB_PORT"])
        self.cursor = self.connection.cursor()

    def getLaptopBrands(self):
        sql = 'Select title, id from \"LaptopBrand\"'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def getCarBrands(self):
        sql = 'select title, id from \"CarBrand\"'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def getBikeBrands(self):
        sql = 'select title, id from \"BikeBrand\"'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def getSmartPhoneBrands(self):
        sql = 'select title, id from \"SmartPhoneBrand\"'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def insert_laptop_data(self, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        query = f"Insert into \"LaptopSpecification\" ({columns}) values({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def insert_smartphone_data(self, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        query = f"Insert into \"SmartPhoneSpecification\" ({columns}) values({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()