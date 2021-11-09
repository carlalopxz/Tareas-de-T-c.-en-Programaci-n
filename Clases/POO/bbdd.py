import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "pruebasentencias"
)

cursor = mydb.cursor()

cursor.execute("Show tables") 
# "Show tables" es para consultar las tablas que tengo en mi base de datos

for i in cursor:
    print(i)

sql = "insert into cliente (nombre) values (%s)"
value = [
        ("Carina",),
        ("Graciela",),
        ("Rolando",),
        ("Juan Ignacio",),
        ("Bruno",)
]  
print(value)
# cursor.execute(sql,value) = Para ingresar un registro
cursor.executemany(sql, value) # = Para ingresar varios registros 

#mydb.commit()

# print(cursor.rowcount, "registro insertado.")

#print(cursor.rowcount, "was inserted.")

sql = "INSERT INTO cliente (nombre) VALUES (%s)"
value = ("ALANA",)

cursor.execute(sql,value)

mydb.commit()

print("1 record inserted, ID:", cursor.lastrowid)