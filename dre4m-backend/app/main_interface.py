from models.users import crear_usuario
from models.users import eliminar_usuario
from models.users import listar_usuarios
from models.users import salir


# Diccionario de opciones
menu_options = {
    "1": crear_usuario,
    "2": eliminar_usuario,
    "3": listar_usuarios,
    "4": salir
}

# Bucle del menú
while True:
    print("\n=== Menú de Opciones ===")
    print("1. Crear usuario")
    print("2. Eliminar usuario")
    print("3. Listar usuarios")
    print("4. Salir")

    choice = input("Selecciona una opción: ")
    
    # Ejecutar la opción si existe en el diccionario, de lo contrario mostrar error
    action = menu_options.get(choice)
    if action:
        action()
    else:
        print("⚠ Opción no válida. Intenta de nuevo.")
