def acceso_usuario(username, password):
    admin_user = "administrador" 
    admin_pass = "1234"
    
    if username == admin_user and password == admin_pass:
        print("Acceso concedido.")
    else:
        print("Usuario o contraseña incorrectos.")

def main():
    username = input("inserte usuario: ")
    password = input("inserte password: ")
  
    acceso_usuario(username, password)

    
main() 
