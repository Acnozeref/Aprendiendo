# --- MÉTODOS DE STRINGS EN PYTHON ---
# (Versión profesional + explicación educativa)

# --------------------------------------------------
#  PRO (comentario profesional)
# --------------------------------------------------
# Métodos esenciales para manipular cadenas de texto:
# strip()     → quita espacios al inicio y final
# lstrip()    → quita espacios al inicio
# rstrip()    → quita espacios al final
# upper()     → convierte a mayúsculas
# capitalize()→ primera letra mayúscula
# title()     → mayúscula por palabra
# startswith()→ verifica si inicia con...
# endswith()  → verifica si termina con...
# replace()   → reemplaza texto
# find()      → busca texto y devuelve posición
# count()     → cuenta apariciones
# split()     → divide en lista
# join()      → une elementos
# isdigit()   → solo dígitos
# isalpha()   → solo letras
# isalnum()   → letras y/o números sin espacios


# --------------------------------------------------
#  EJEMPLOS
# --------------------------------------------------
"   hola   ".strip()            # "hola"
texto = "   hola   "
texto.lstrip()                   # "hola   "
texto.rstrip()                   # "   hola"

nombre = input("Nombre: ").strip()
print(nombre)

"hola".upper()                   # "HOLA"
"hola mundo".capitalize()        # "Hola mundo"
"hola mundo".title()             # "Hola Mundo"

palabra = "___Python___"
resultado = palabra.strip("_")   # "Python"

respuesta = input("¿Continuar? (si/no): ").strip().lower()

"python".startswith("py")        # True
"archivo.txt".endswith(".txt")  # True
"hola kevin".replace("hola", "hi")  # "hi kevin"
"python".find("th")              # 2
"banana".count("a")              # 3
"hola mundo".split()             # ["hola", "mundo"]
"-".join(["hola", "mundo"])     # "hola-mundo"

"123".isdigit()                  # True
"Kevin".isalpha()                 # True
"Python123".isalnum()            # True


# --------------------------------------------------
#  EDUCATIVO (comentario nivel aprendizaje)
# --------------------------------------------------
# Estos métodos permiten limpiar texto, transformarlo y analizarlo.
# Son fundamentales para validación de datos, procesamiento de entradas
# y construcción de programas que interactúan con usuarios.
# La práctica con estos métodos te prepara para manejar strings
# en proyectos más grandes y profesionales.
