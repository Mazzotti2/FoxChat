import mysql.connector

def connect():
	return mysql.connector.connect(host = "localhost", database = "foxchat", user = "root", password = "root")

def login(username, password):
	my_dtb = connect()

	cursor = my_dtb.cursor()

	sql = "SELECT id FROM foxchat.users where username = %s and password = %s;"
	val = (username, password)
	cursor.execute(sql, val)

	result = cursor.fetchone()

	if result != None:
		return result[0]
	else:
		return -1

def register(username, password):
	try:	
		my_dtb = connect()

		cursor = my_dtb.cursor()

		sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s);"
		val = (username, password)
		cursor.execute(sql, val)

		my_dtb.commit()

		return True
	except mysql.connector.Error:
		return False