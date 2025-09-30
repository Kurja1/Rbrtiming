import sqlite3

# Connect to the database
conn = sqlite3.connect('resources/raceStatDB.sqlite3')
cursor = conn.cursor()

# Query the F_RallyResult table to retrieve the latest entry
cursor.execute("""
    SELECT *
    FROM F_RallyResult
    ORDER BY RaceDate DESC, RaceDateTime DESC
    LIMIT 1;
""")

# Fetch the query result
result = cursor.fetchone()

# Print the newest result
if result:
    print("Newest Result:")
    for column in result:
        print(f"{column}")
else:
    print("No latest result found.")

# Close the connection
conn.close()