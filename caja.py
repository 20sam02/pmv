import mysql.connector
conexion = mysql.connector.connect(user='sam1', password='1234', host='localhost', database='pmvpos', port='3306')
print(conexion)

conn = mysql.connector.connect(conexion)
cursor = conn.cursor()


try: 
    conn = mysql.connector.connect(conexion)
    print("conexión exitosa")
except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")

user = 'admin'
pwd = '1234'

options = ()
print("Ingresa el usuario y contraseña")

print("usuario: ")
user = input(str)
print ("contraseña")
pwd = input(int)

if user == user and pwd == pwd :
    print ("credenciales conrrectas")
else:
    print("usuario o contraseña incorrecta")

print("OPCIONES:")
print("1. Totalizar venta y generar facturas. 2. inventario de bebidas. 3. Inventario. 4. Ver resumen diario.")
options = input(int)


if options == 2 :
    def agg_prod(ID, Nombre, Cantidad):
        query = "INSERT INTO inventario_bebidas (ID, Nombre, Cantidad) VALUES (%s, %s)"
        value = (ID, Nombre, Cantidad)
        cursor.execute(query, value)
        conn.commit()
    def del_prod(ID, Nombre, Cantidad):
        query = "DELETE FROM inventarios_bebidas WHERE ID (%s)"
        value = (ID,)
        cursor.execute(query, value)
        conn.commit()
     


cursor.close()
conn.close()