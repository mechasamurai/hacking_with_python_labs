import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        job TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert mock data
cursor.execute('DELETE FROM users')  # Clear table before inserting new data

users = [
    (1, 'John Doe', 'Software Engineer', 'pass123'),
    (2, 'Jane Smith', 'Data Scientist', 'pass456'),
    (3, 'Alice Johnson', 'Graphic Designer', 'pass789'),
    (4, 'Bob Brown', 'Project Manager', 'pass101')
]

cursor.executemany('INSERT INTO users (id, name, job, password) VALUES (?, ?, ?, ?)', users)

# Commit the transaction
conn.commit()

# Function to get user data by ID
def get_user_by_id(user_id):
    cursor.execute(f'SELECT name, job FROM users WHERE id={user_id}')
    user = cursor.fetchone()
    if user:
        return user
    else:
        return None

# Ask for user ID input
try:
    user_id = input("Enter the user ID to retrieve their name and job title: ")
    user = get_user_by_id(user_id)
    if user:
        print(f"Name: {user[0]}, Job: {user[1]}")
    else:
        print("User not found!")
except ValueError:
    print("Please enter a valid numeric user ID.")

# Close the connection
conn.close()
