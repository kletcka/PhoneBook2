import sqlite3

def start():
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute(f"CREATE TABLE IF NOT EXISTS  'book' (\
		'name' TEXT,\
		'surname' TEXT,\
		'patronymic' TEXT,\
		'phone' TEXT,\
		'email' TEXT,\
		'note' TEXT)")
	db.commit()
	db.close()
    