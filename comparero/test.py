import psycopg2
import os
import dotenv
from slugify import slugify

dotenv.load_dotenv()

class DatabaseHandler:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(database=os.environ['DB_NAME'], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"], host=os.environ["DB_HOST"], port=os.environ["DB_PORT"])
        self.cursor = self.connection.cursor()

    def test(self, data, brand_name):
        if brand_name != None:
            self.cursor.execute("select * from \"BikeBrand\" where title=%s;", ('honda',))
            brandData = self.cursor.fetchall()
            if(len(brandData) > 0):
                data['\"brandId\"'] = brandData[0][0]
                print('bike brand')
                print(data['\"brandId\"'])
            self.connection.commit()

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        query = f"Insert into \"LaptopSpecification\" ({columns}) values({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()
        

    def close(self):
        self.cursor.close()
        self.connection.close()

db = DatabaseHandler()
data = {
    'title': 'the title',
    'url': 'the url',
    'slug': 'the-title'
}
db.connect()
db.test(data, 'honda')