# Object definition for users
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username: str, password: str, role: str):
        super().__init__(username, password)
        self.role = role

class Customer(User):
    def __init__(self, username: str, password: str, email: str):
        super().__init__(username, password)
        self.email = email

# Temporal function definitions
def crear_usuario():
    print("Función para crear usuario...")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    email = input("Correo electrónico: ")
    user = Customer(username, password, email)
    print(f"Usuario {user.username} creado exitosamente.")
    return user

def eliminar_usuario():
    print("Función para eliminar usuario...")

def listar_usuarios():
    print("Función para listar usuarios...")

def salir():
    print("Saliendo del programa...")
    exit()