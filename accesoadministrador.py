def acceso_usuario():
 
  pass

def main():
  admin_user = "administrador" 
  admin_pass = "1234" 

  user_input_username = input("inserte usuario: ")
  user_input_password = input("inserte password: ")

  if user_input_username == admin_user and user_input_password == admin_pass:
    print("Acceso concedido.")
  else:
    print("Usuario o contraseña incorrectos.")

main() 
