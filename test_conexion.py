#Este archivo solo es para probar la conexion a la base de datos y saber qué tablas hay en ella.
from db import conectar

conn = conectar()

if conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        print("📦 Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla)
    conn.close()


