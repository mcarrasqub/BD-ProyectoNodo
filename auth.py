# auth.py
from db import conectar

def login():
    email = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")

    conn = conectar()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM adminis WHERE email=%s AND contrasena=%s", (email, contrasena))
            admin = cursor.fetchone()
            if admin:
                admin["rol"] = "admin"
                return admin

            cursor.execute("SELECT * FROM profesor WHERE email=%s AND contrasena=%s", (email, contrasena))
            prof = cursor.fetchone()
            if prof:
                prof["rol"] = "profesor"
                return prof

            cursor.execute("SELECT * FROM estudiante WHERE email=%s AND contrasena=%s", (email, contrasena))
            est = cursor.fetchone()
            if est:
                est["rol"] = "estudiante"
                return est

            print("❌ Usuario o contraseña incorrectos.")
            return None
    finally:
        conn.close()

