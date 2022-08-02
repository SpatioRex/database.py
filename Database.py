import sqlite3 as sl 
conn = sl.connect('Services_database')
c = conn.cursor() 
with conn:
    c.execute('''CREATE TABLE USER (id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTERGER );
    ''')


sql = 'INSERT ONTO USER (id, name, age) values(?,?,?)'
data = [ 
    (1, 'Alice', 21)
    (2, 'Joe', 22)
    (3, 'Mack', 26)
]
with conn:
    conn.executemany(sql, data)