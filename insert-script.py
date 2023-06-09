import DatabaseHandler as db
from slugify import slugify
import json
import dotenv
import re

dotenv.load_dotenv()


itti_f = open('itti.json')
neostore_f = open('neostore.json')
db = db.DatabaseHandler()
db.connect()

itti_data = json.load(itti_f)
neostore_data = json.load(neostore_f)

laptop_brands = db.getLaptopBrands()
smartphone_brands = db.getSmartPhoneBrands()

def extractInt(data):
    value = re.search(r'\d+', data)
    if value == None:
        return None
    return int(value.group())
    
def insertIttiData():
    for item in itti_data:
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


def insertNeoStoreData():
    for item in neostore_data:
        brandId = 1
        if 'brand' in item:
            for i in smartphone_brands:
                if isinstance(item['brand'], str):
                    if i[0] == item['brand'].lower():
                        brandId = i[1]

        insert_data = {
            "title": item['title'],
            "url": item['url'][0],
            "\"brandId\"": brandId,
            # "category": item['category'] if 'category' in item else '-',
            "resolution": item['display'] if 'display' in item else '-',
            # "battery": item['battery'] if 'battery' in item else '-',
            "internal_storage": extractInt(item["internal_storage"] if "internal_storage" in item else '-'),
            "back_camera": extractInt(item["back_camera"] if "back_camera" in item else '-'),
            "front_camera":extractInt( item["front_camera"] if "front_camera" in item else '-'),
            "chip": item["chip"] if "chip" in item else '-',
            "os": item["os"] if "os" in item else '-',
            "processor": item["processor"] if "processor" in item else '-',
            "sim_type": item["sim_type"] if "sim_type" in item else '-',
            "slug": slugify(item['title'][0]),
        }

        db.insert_smartphone_data(insert_data)

insertNeoStoreData()