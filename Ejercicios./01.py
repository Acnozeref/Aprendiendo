"""Ejercicios"""
# Tu edad
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad < 64:
    print("Eres mayor de edad")
elif edad > 65:
    print("Eres adulto mayor")

# Contraseña

contraseña = input("Ingrese la contraseña: ")

if contraseña == "python123":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")


# Temperatura

temp = int(input("Ingrese la temperatura: "))

if temp < 15:
    print("Hace frío.")
elif 15 <= temp <= 25:
    print("Clima agradable.")
elif temp > 25:
    print("Hace calor.")