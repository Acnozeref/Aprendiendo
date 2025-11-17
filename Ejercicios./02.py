# Pide al usuario su edad y si tiene licencia (True/False).
# Si tiene 18 o más años y licencia, imprime "Puedes conducir".
# Si no cumple ambas, imprime "No puedes conducir".

print("Hola, Bienvenid@, datos de admision para conducir. ")

edad = int(input("Ingrese su edad: "))
licencia = input("¿Cuenta con licencia? (si/no): ").lower()

if edad >= 18 and licencia == "si":
    print("Puedes conducir.")
else:
    print("No puedes conducir.")


# Pide el nivel del estudiante ("básico", "intermedio", "avanzado") y si aprobó el examen (True/False).
# Solo puede acceder si el nivel es "intermedio" o "avanzado" y aprobó el examen.

print("Acceso a curso avanzado: ")
print("Ingrese su nivel de estudiante y su calificion final.")

nivel = int(input("Numero 1 para Basico. 2 para intermedio. 3 para avanzado: "))
notas = input("Aprovaste el examen?: ")

if (nivel == 2 or nivel == 3) and notas == "si":
    print("Aprobó el examen.")
else:
    print("Reprobó el examen.")




# 3️⃣ Temperatura segura:
# Pide una temperatura y verifica si está entre 20 y 30 grados o es exactamente 0.
# Si se cumple, imprime "Temperatura segura", de lo contrario "Fuera de rango".

temperatura = int(input("Ingresa una temperatura: "))

if 20 <= temperatura <= 30 or temperatura == 0:
    print("Temperatura segura.")
else:
    print("Fuera de rango.")


# 4️⃣ Ingreso a zona restringida:
# Pide una clave y un rol ("admin", "user", "guest").
# Solo entra si la clave es "secreto123" y el rol no es "guest".

print("Zona restringida. Ingrese cuenta y contraseña.")

rol = input("Cual es su rol? (admin, user, guest. ): ")
clave = input("Ingrese la clave: ")

if rol != "guest" and clave == "secreto123":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")


# 5️⃣ Año bisiesto (reto extra):
# Pide un año y determina si es bisiesto.
# Pista: Un año es bisiesto si es divisible entre 4 y *(no entre 100 o sí entre 400).

print("Bienvenid@, ingrese un año y te diré si es viciesto o no.")

año = int(input("Ingrese un año: "))

if (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0):
    print("Es una año viciesto!")
else:
    print("No es año viciesto")



# Reglas que sigue python

x = 5
y = 10
print(not x > 3 and y > 5)
# Se evalúa así:
# (not (x > 3)) and (y > 5)
# False and True → False
