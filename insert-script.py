import DatabaseHandler as db
from slugify import slugify
import json
import dotenv

dotenv.load_dotenv()


f = open('itti.json')
db = db.DatabaseHandler()
db.connect()

data = json.load(f)

laptop_brands = db.getLaptopBrands()

print(len(data))
for item in data:
    # TODO make default null in brand id
    brandId = 1
    if 'brand' in item:
        for i in laptop_brands:
            if isinstance(item['brand'], str):
                if i[0] == item['brand'].lower():
                    brandId = i[1]
                
    insert_data = {
        "title": item['title'],
        "url": item['url'],
        "\"brandId\"": brandId,
        "cpu": item['cpu'] if 'cpu' in item else '-',
        "graphics": item['graphics'] if 'graphics' in item else '-',
        "generation": item['title'] if 'title' in item else '-',
        "slug": slugify(item['title']),
        # "display_size": item['display'] if 'display' in item else '-',
        # "storage": item['storage'] if 'storage' in item else '-'
    }
    db.insert_laptop_data(insert_data)