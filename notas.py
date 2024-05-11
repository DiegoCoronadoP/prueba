#Diego Andres Coronado Pava- Calculador de nota final de año
print ("Bienvenido a mi programa que calcula la nota definitiva del año por medio de 3 cortes")
print("A continuacion tendra las indicaciones, el programa se finalizara si registra una nota fuera de (0-5)")
def salirsinofunciona():
    nota1=float(input("digite la primer nota del corte 1: "))
    if nota1 <0.1 or nota1>5.0:
          print("numero no valido, digite un numero dentro de las especificaciones")
          return
    resul1=nota1*0.35
    
    nota2=float(input("Digite la nota del corte 2 : "))
    if nota2<0.1 or nota1>5.0:
          print("numero no valido, digite un numero dentro de las especificaciones")
          return
    resul2=nota2*0.35
    
    
    nota3=float(input("digite la nota del corte 3: "))
    if nota3<0.1 or nota1>5.0:
          print("numero no valido, digite un numero dentro de las especificaciones")
          return 
    resul3=nota3*0.30

    resultado=resul3+resul1+resul2
    
    if resultado>3.0:
          print("Has Pasado Exitosamente, tu nota definitiva es: ", resultado)
    if resultado>2.4 and resultado<3.1: 
          print ("Te encuentras en recuperacion, tu nota definitiva es: ", resultado)
    if resultado<2.5:
          print("Reprobaste tu materia, tu nota definitiva es: ", resultado)
    

salirsinofunciona()
