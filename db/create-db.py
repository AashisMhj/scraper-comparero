import sqlite3

conn = sqlite3.connect('data.db')

conn.execute('''
CREATE TABLE laptop (ID INT PRIMARY KEY NOT NULL, title TEXT NOT NULL, brand TEXT, cpu TEXT, graphics TEXT )
''')