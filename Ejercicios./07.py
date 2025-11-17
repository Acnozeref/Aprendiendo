# 1) Normalizar nombre
nombre = input("Ingrese su nombre completo: ").strip().title()
print(nombre)


# 2) Verificador de correo simple
correo = input("Ingrese un correo electrónico: ")

if "@" in correo and (correo.endswith(".com") or correo.endswith(".mx")):
    print("Correo válido!")
else:
    print("Correo inválido.")


# 3) Sensor de palabras prohibidas
texto = input("Ingrese un texto: ").lower().strip()

if "spam" in texto:
    print("Contenido bloqueado.")
else:
    print("Contenido limpio.")


# 4) Convertidor de guiones
frase = input("Ingrese una frase: ").lower().split()
print("-".join(frase))


# 5) Enmascarador de contraseñas
contraseña = input("Ingrese una contraseña: ")
print("*" * len(contraseña))


# 6) Contador de vocales
texto = input("Ingrese un texto: ").lower()

print("a:", texto.count("a"))
print("e:", texto.count("e"))
print("i:", texto.count("i"))
print("o:", texto.count("o"))
print("u:", texto.count("u"))


# 7) Detector de extensión de archivo
archivo = input("Ingrese un archivo: ")

if archivo.endswith(".py"):
    print("Archivo Python.")
elif archivo.endswith(".txt"):
    print("Archivo de texto.")
else:
    print("Tipo desconocido.")
