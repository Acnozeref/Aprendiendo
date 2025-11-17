# --- F-STRINGS EN PYTHON ---
# (Versión profesional + explicación educativa)

# --------------------------------------------------
#  PRO (comentario profesional)
# --------------------------------------------------
# Las f-strings permiten insertar variables dentro de un texto
# usando la sintaxis: f"texto {variable} más texto".
# Son la forma más limpia y moderna de formatear cadenas.

# Ejemplo sintético (ignorar variable no definida):
print(f"Texto {variable} más texto")  # type: ignore

# Ejemplo real con variables:
nombre = "Kevin"
edad = 20

print(f"Hola, me llamo {nombre} y tengo {edad} años.")


# --------------------------------------------------
#  EDUCATIVO (comentario nivel aprendizaje)
# --------------------------------------------------
# Las f-strings sirven para "pegar" texto y variables sin usar comas ni +.
# Solo escribes una f antes de las comillas y dentro pones {variable}.
# Ejemplo:
#   f"Tengo {edad} años"
# Python sustituye {edad} por el valor que tenga esa variable.
# Es la forma más clara, rápida y usada para mostrar texto dinámico.
