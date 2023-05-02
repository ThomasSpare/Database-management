import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
#cursor.execute('SELECT "Name" FROM "Artist"')

# Query 2 - select 
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["94"])

# Query myown 1
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Jimi Hendrix"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(results)