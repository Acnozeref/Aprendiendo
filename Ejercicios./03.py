# 1️⃣ Verificación de usuario
# Pide un nombre de usuario y una contraseña.
# Solo debe permitir acceso si el nombre no está vacío y la contraseña no es "1234".
# Usa not en la condición.

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese contraseña: ")

if (usuario != "") and (contraseña != "1234"):
    print("Acceso concedido")
else:
    print("Acceso denegado.")

# 2️⃣ Clima y paraguas ☔
# Pide si está lloviendo ("si"/"no") y si llevas paraguas ("si"/"no").
# Si llueve y no llevas paraguas, imprime "Te mojarás".
# Si llueve y llevas paraguas, "Estás protegido".
# Si no llueve, "No hace falta paraguas".

lluvia = input("Está lloviendo?: ").lower()
paraguas = input("Tienes paraguas?: ").lower()

if (lluvia == "si") and (paraguas == "no"):
    print("Te mojarás!")
elif (lluvia == "si") and (paraguas == "si"):
    print("Estas protegido!")
else:
    print("No hace falta paraguas.")

# 3️⃣ Sistema de acceso
# Pide el rol del usuario ("admin", "moderador", "usuario")
# Si es "admin", muestra "Acceso total".
# Si es "moderador", muestra "Acceso limitado".
# Si no es ninguno de esos, muestra "Sin acceso".
# 👉 Usa condiciones anidadas (if dentro de else).

rol = input("Ingrese su rol ([admin][moderador][usuario]): ").lower()

if rol == "admin":
    print("Acceso total.")
else:
    if rol == "moderador":
        print("acceso limitado.")
    else:
        print("Sin acceso!")


# 4️⃣ Verificador de edad y registro
# Pide la edad y si está registrado ("si"/"no").
# Debe imprimir "Acceso permitido" solo si la edad es mayor o igual a 18 y está registrado.
# Si no está registrado, muestra "Debes registrarte primero" (usa not).

edad = int(input("Ingrese su edad:  "))
registro = input("Estas registrado?:    ").lower()

if edad >= 18 and registro == "si":
    print("Acceso permitido.")
else:
    if  not registro == "si":
        print("Debe registrarse primero.")
    else:
        print("Acceso denegado.")


# 5️⃣ Sistema de seguridad
# Pide una clave y si el usuario tiene autorización (True/False).
# Solo permite el acceso si la clave es "segura999" y no tiene autorización falsa.

clave = input("Ingrese clave de autorizacion:   ")
autorizar = input("Tiene autorizacion legitima?:  ")

if clave == "segura999" and autorizar == "si":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")