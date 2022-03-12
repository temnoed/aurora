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

cur.execute("SELECT admission, name, age, course, department from STUDENT")

rows = cur.fetchall()
for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")


# con.commit()
con.close()
