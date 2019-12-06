import psycopg2

# THIS FILE IS A SIMPLE DATABASE CONNECTION IN PYTHON FOR YOU TO SEE
# Install psycopg2 by typing pip3 install psycopg2
# If your computer doesn't have pip3, try pip instal psycopg2
# If you get lots of errors there: try psycopg2-binary instead! :)
# Want to build a server to work with this? look at Flask or our next repository

# Create the DB found in the Database.sql file

# Connect to db
# Start sesion
connection = psycopg2.connect(
    host = "127.0.0.1",
    database="python_test",
)

# create a cursor - this is a vessel to connect with database
cursor = connection.cursor()

# Insert into and commit to save the transaction
cursor.execute("INSERT INTO santa_list (name,is_nice) VALUES(%s,%s)",('Iris','TRUE'))
connection.commit()

# Get all items.
cursor.execute("SELECT id, name FROM santa_list")

rows = cursor.fetchall()

# get back array of tuples [(0,"dave"),(1,"evan")]
for row in rows:
    print (f"id {row[0]} name {row[1]}")


# Close cursor
cursor.close()
# Close Connection
connection.close()