from auth import login

def menu_admin(info):
    print(f"\n🔐 Bienvenido Administrador {info['nombre']}")
    # Aquí se incluirán las funciones específicas para el administrador
    pass

def menu_profesor(info):
    print(f"\n📚 Bienvenido Profesorr {info['nombre']}")
    # Aquí se incluirán las funciones específicas para el profesor
    pass

def menu_estudiante(info):
    print(f"\n🎓 Bienvenido Estudiante {info['nombre']}")
    # Aquí se incluirán las funciones específicas para el estudiante
    pass

def main():
    print("=== Sistema Académico ===")
    user = login()
    if user:
        print(f"\n✅ Inicio de sesión exitoso como {user['rol']}")
        if user['rol'] == "admin":
            menu_admin(user)
        elif user['rol'] == "profesor":
            menu_profesor(user)
        elif user['rol'] == "estudiante":
            menu_estudiante(user)
    else:
        print("❌ Credenciales inválidas. Intente nuevamente.")

if __name__ == "__main__":
    main()
