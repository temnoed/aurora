import requests
import datetime
import psycopg2

r = requests.get('https://services.swpc.noaa.gov/text/ace-magnetometer.txt')
textByStrings = r.text.splitlines()

current_date = datetime.datetime.now()
s_date = current_date.strftime("%d-%m-%y %H:%M:%S")

f = open("/home/dmitriy/temp/aurora.log", "a")
f.write(s_date + ":\n")
f.write(textByStrings[20] + "\n")
f.close()

con = psycopg2.connect(
    database="aurora",
    user="temnoed",
    password="Hannanamiti1",
    host="127.0.0.1",
    port="5432"
)

print("Database opened successfully")

cur = con.cursor()
# cur.execute('''CREATE TABLE STUDENT
#      (ADMISSION INT PRIMARY KEY NOT NULL,
#      NAME TEXT NOT NULL,
#      AGE INT NOT NULL,
#      COURSE CHAR(50),
#      DEPARTMENT CHAR(50));''')

cur.execute('''INSERT INTO magnetometr ("YR", "Bz") VALUES (2022, 12.3)''')
con.commit()

cur.execute('''SELECT * from magnetometr ORDER BY "id" DESC LIMIT 5''')




rows = cur.fetchall()
for row in rows:
    print(*row)

cur.close()
con.close()
