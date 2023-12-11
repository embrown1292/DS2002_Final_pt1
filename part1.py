import json
import sqlite3

# Bringing in the JSON file created
with open('api_data_test.json') as json_file:
    data = json.load(json_file)

# Making the SQLite db
db_conn = sqlite3.connect('part1_api_data.db')
cursor = db_conn.cursor()

# Making the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS your_table (
        timestamp TEXT PRIMARY KEY,
        factor INTEGER,
        pi REAL,
        time TEXT
    )
''')

# Putting in the data here
for timestamp, entry in data.items():
    cursor.execute('''
        INSERT INTO your_table (timestamp, factor, pi, time)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, entry['factor'], entry['pi'], entry['time']))

# Making my changes and closing the connection
db_conn.commit()
db_conn.close()
