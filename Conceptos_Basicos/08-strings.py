# Strings
# Quita los espacios al inicio y al final de cada texto
"   hola   ".strip() #


texto = "   hola   "
# quita solo los espacios del inicio (left)
texto.lstrip()   #→ "hola   "
# quita solo los espacios del final (right)
texto.rstrip()   #→ "   hola"


# Ejemplo:
nombre = input("Nombre: ").strip()
print(nombre)

# Mayusculas
"hola".upper()   # "HOLA"

# Convierte solo la primera letra en mayuscula.
"hola mundo".capitalize()   # "Hola mundo"

# Convierte cada palabra en mayus inicial
"hola mundo".title()   # "Hola Mundo"



# Ejemplo con caracter especial

palabra = "___Python___"
resultado = palabra.strip("_")


# Combinaciones

respuesta = input("¿Continuar? (si/no): ").strip().lower()


# Revisa si empieza con algo
"python".startswith("py")   # True

# Revisa si termina con algo
"archivo.txt".endswith(".txt")   # True

# Reemplaza texto 
"hola kevin".replace("hola", "hi")   # "hi kevin"


# Devuelve la posición donde aparece algo.
# Si no existe, devuelve -1.
"python".find("th")   # 2


# Cuenta cuantas veces aparece algo
"banana".count("a")   # 3


# Divide un string en listas separadas por espacios (o lo que le digas).
"hola mundo".split()  
# ["hola", "mundo"]

# Usa elementos con un separador
"-".join(["hola", "mundo"])
# "hola-mundo"




#.isdigit() devuelve True si la cadena contiene solamente dígitos.

# Ejemplos:

"123".isdigit()       # True
"12a3".isdigit()      # False
" 123 ".isdigit()     # False  (por espacios)
"00123".isdigit()     # True


# .isalpha()

# Devuelve True solo si la cadena tiene solo letras (a-z).
# No permite números, espacios ni símbolos.

"Kevin".isalpha()       # True
"Kevin22".isalpha()     # False
"Kevin López".isalpha() # False (por el espacio)



# .isalnum()

# Devuelve True si hay letras y/o números, pero sin espacios ni símbolos.

"Python123".isalnum()  # True
"1234".isalnum()       # True
"hola-mundo".isalnum() # False (el guion lo arruina)
"hola mundo".isalnum() # False (espacio)
