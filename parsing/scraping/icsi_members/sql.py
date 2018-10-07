import sqlite3

conn = sqlite3.connect('emails.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE emails IF NOT EXISTS
             (email text unique)''')

# Insert a row of data
def add_to_db(email):
	try:
		c.execute("INSERT INTO emails VALUES ('vaibhavmule135@gmail.com')")
	except sqlite3.IntegrityError as e:
		pass

# Save (commit) the changes
conn.commit()

conn.close()
