# Mínimo 6 caracteres
# Que no sea solo números
# Que no contenga espacios

contraseña = input("Ingrese una contraseña: ").lower()

while not len(contraseña) >= 6 and not contraseña.isdigit() and " " not in contraseña:
    contraseña = input("Error, ingrese 6 caracteres o mas, no SOlO numeros y sin espacios: ")

print("Contraseña guardada.")