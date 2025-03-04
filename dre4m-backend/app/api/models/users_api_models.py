# Object definition for users
class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class Admin(User):
    def __init__(self, email: str, password: str, role: str):
        super().__init__(email, password)
        self.role = role


class Customer(User):
    def __init__(self, email: str, password: str):
        super().__init__(email, password)
        self.email = email

# Temporal function definitions


def crear_usuario():
    print("Función para crear usuario...")
    email = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    email = input("Correo electrónico: ")
    user = Customer(email, password)
    print(f"Usuario {user.email} creado exitosamente.")
    return user


def eliminar_usuario():
    print("Función para eliminar usuario...")


def listar_usuarios():
    print("Función para listar usuarios...")


def salir():
    print("Saliendo del programa...")
    exit()
