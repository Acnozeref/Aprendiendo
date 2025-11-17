# Validar si o no.

resp = input("¿Continuar? (si/no): ").lower()

while resp != "si" and resp != "no":
    print("Respuesta inválida.")
    resp = input("¿Continuar? (si/no): ").lower()

print("Respuesta registrada.")

# Verificador de edad con bucle.

edad = int(input("Ingrese una edad: "))
while edad <= 0 or edad > 120:
    edad = int(input("Vuelva a ingresar una edad: "))
print("Edad registrada!") 


# Sistema de acceso simple

usuario = input("Ingrese su usario: ")

while usuario == "":
    usuario = input("Ingrese un usuario valido: ")

print(f"Hola, {usuario}!, Bienvenid@.")


# Contraseña de 6 caracteres.

password = input("Crea tu contraseña: ")

while len(password) < 6:
    password = input("Debe tener al menos 6 caracteres. Intente de nuevo: ")

print("Contraseña guardada.")


