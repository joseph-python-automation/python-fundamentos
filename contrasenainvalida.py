      #Crea un programa que:
#Pida una contraseña
#Solo permita 3 intentos
#Si acierta → “Acceso concedido”
#Si falla 3 veces → “Cuenta bloqueada”



contraseñacorrecta = "Joseph2506"
contador = 0   

while True:
  contraseña = input("Introduzca su contraseña: ")

  if contraseña == contraseñacorrecta:
    print("Acceso concedido")
    break

  else: 
    contador += 1
    print("contraseña incorrecta")
 
  
    if contador == 3:
      print("Cuenta bloqueada")        
      break