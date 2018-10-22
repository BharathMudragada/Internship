import getpass
import MySQLdb
from texttable import Texttable
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Crypto.Cipher import AES
from os import stat, remove
import json

password = getpass.getpass("Enter Password: ")
obj2 = AES.new(password, AES.MODE_CBC, 'This is an IV456')
fOut = open("client_secret.json", "wb")
with open("client_secret.aes", "rb") as fIn:
    try:
		ciphertext = fIn.read()
		fOut.write(obj2.decrypt(ciphertext))
    except ValueError:
        pass
fOut.close()

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("databases").sheet1
databases = sheet.get_all_records()

print "Select a database"
for i in range(0, len(databases)):
	print i + 1,databases[i]["Database Name"]

db_choosen = -1
while not 1 <= db_choosen <= len(databases):
	db_choosen  = int(raw_input("Enter database number: "))
db_choosen -= 1

conn=MySQLdb.connect(host=databases[db_choosen]["Host"],user=databases[db_choosen]["Username"],passwd=databases[db_choosen]["Password"])
cursor = conn.cursor()
cursor.execute("use " + databases[db_choosen]["Database Name"])
while(1):
	query = raw_input("Enter query: ")
	try:
		t = Texttable()
		cursor.execute(query)
		res = []
		res.append([i[0] for i in cursor.description])
		result = cursor.fetchall()
		for row in result:
			res.append(row)
		t.add_rows(res)
		print t.draw()
	except:
		print "Enter a valid query"