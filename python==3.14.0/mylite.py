import sqlite3

#Connecting to a sqlite database
#Will create the file if it does not exist
conn = sqlite3.connect("example.db")

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS employees(
    id Integer Primary Key,
    name Text Not Null,
    age Integer,
    department Text
    )
    """
)

cur.execute(
    "INSERT INTO employees (name, age, department) VALUES (?,?,?)",
    ("Steffan", 23, "Machine Learning Engineer"),
    )

rows = cur.execute("SELECT * FROM employees")

for val in rows:
    print(val)

    
conn.commit()
conn.close()
