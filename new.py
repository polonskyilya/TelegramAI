from pythonping import ping
import sys
import mysql.connector
import os
dbname=os.environ.get('DB_NAME')
mydb = mysql.connector.connect(host=os.environ.get('MYSQL_IP'),user=os.environ.get('MYSQL_ROOT_USER'),
          password=os.environ.get('MYSQL_ROOT_PASSWORD'))
mycursor = mydb.cursor()
query = f"SELECT link_download FROM {dbname} WHERE search_phrase = 'strangeshithappened'"
mycursor.execute(query)
with open('/img/file.txt', 'w') as sys.stdout:
    print(f'FROM ENV\n{os.environ.get("MYSQL_IP")}\n{os.environ.get("MYSQL_ROOT_USER")}\n'
          f'{os.environ.get("MYSQL_ROOT_PASSWORD")}\n{os.environ.get("API")}\n')
    print(f'GOOGLE PING\n{ping("8.8.8.8")}')
    print(f'SQL PING\n{ping("192.168.20.200")}')
    print(f'FROM SQL\n{mycursor.fetchone()}')