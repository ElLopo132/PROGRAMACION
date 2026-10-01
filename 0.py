print ("¡Bienvenido Al sistema De Calificaciones!")
nombre =input("Ingrese su nombre: ")
cantidada_de_materias = int(input("Ingrese la cantidad de materias: "))
suma_calificaciones = 0.0
print("Captura de calificaciones:")
for i in range(1, cantidada_de_materias + 1):
    calificacion = float(input(f"Ingresa La Calificación de la materia {i}: "))
    suma_calificaciones += calificacion
promedio = suma_calificaciones / cantidada_de_materias
print(f"\n{nombre}, tu promedio es: {promedio:.2f}")

if promedio >= 7.0:
 print("ERES LA VERGA ÑONGA ÑONGA.")
else:
 print("No vales verga.")
input("Presiona Enter para salir...")
