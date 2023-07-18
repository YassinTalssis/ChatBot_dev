import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a query to retrieve data from a table
cursor.execute('SELECT * FROM db')

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Process the rows
for row in rows:
    # Access individual columns in the row
    column1_value = row[0]
    column2_value = row[1]
    # ... continue accessing other columns as needed

    # Process the values as per your requirement
    # For example, you can print the values
    print(f'Column 1: {column1_value}, Column 2: {column2_value}')

# Close the database connection
conn.close()

