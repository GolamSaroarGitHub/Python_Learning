import sqlite3

import pprint
conn = sqlite3.connect('example.db')
c = conn.cursor()



ce=c.execute("SELECT * FROM stocks")

for row in ce:
    print(row)

conn.close()