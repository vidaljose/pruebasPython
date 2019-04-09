#nombreUsuario=input("Introduce un nombre de usuario: ")
#print("El nombre es: ",nombreUsuario.capitalize())
edad = input("Introduce la edad: ")
#print(edad.isdigit() == False)

while(edad.isdigit() == False):
    print("Por favor introduce un valor numerico")
    edad=input("Introduce la edad: ")

if(int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")
