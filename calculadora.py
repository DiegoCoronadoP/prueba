print("Hola, Soy Diego Andres Coronado Pava, Esta es mi calculadora")
while True:
    numerousar= int(input("Bienvenido a este programa que suma, resta, multiplica o divide \npara sumar digite (1), para restar digite (2), para multiplicar digite (3), para dividir digite (4), si digita un numero distinto se asumira que deseas buscar la salida :) "))
    if numerousar== 1:
        print("Bienvenido a este programa que suma ")
        num1=int(input("porfavor digite el primer numero "))
        num2=int(input("porfavor digite el segundo numero "))
        resul=num1+num2
        print("el resultado de la suma de los dos numeros es: ", resul)
    if numerousar== 2:
        print("Bienvenido a este programa que resta ")
        num1=int(input("porfavor digite el primer numero "))
        num2=int(input("porfavor digite el segundo numero "))
        resul=num1-num2
        print("el resultado de la resta de los dos numeros es: ", resul)
    if numerousar== 3:
        print("Bienvenido a este programa que multiplica ")
        num1=int(input("porfavor digite el primer numero "))
        num2=int(input("porfavor digite el segundo numero "))
        resul=num1*num2
        print("el resultado de la multiplicacion de los dos numeros es: ", resul)
    if numerousar== 4:
        print("Bienvenido a este programa que divide ")
        num1=int(input("porfavor digite el primer numero "))
        num2=int(input("porfavor digite el segundo numero "))
        resul=num1/num2
        print("el resultado de la division de los dos numeros es: ", resul)
    
    continuar= input("Desea realizar otra operacion?, digite cualquier cosa menos 'no' o 'n' si es asi, de lo contrario digite no: ")
    continuar=continuar.upper()
    if continuar == "N" or continuar == "NO":
        break
    print("gracias por usar mi calculadora hasta pronto")
    
    
    

    
