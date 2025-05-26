import pymysql

def conectar():
    print("📡 Intentando conectar a la base de datos...")
    try:
        conn = pymysql.connect(
            host="localhost",
            port=3307,               
            user="root",
            password="Fito123", # ← Reemplaza con tu contraseña real
            database="sistema_nodo",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("✅ Conexión exitosa.")
        return conn
    except Exception as e:
        print("❌ Error al conectar:")
        print(e)
        return None
