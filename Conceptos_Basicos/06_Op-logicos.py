# --- OPERADORES LÓGICOS EN PYTHON ---
# (Versión profesional + explicación educativa)

# --------------------------------------------------
#  PRO (comentario profesional)
# --------------------------------------------------
# Operadores lógicos:
# and → ambas condiciones deben ser True
# or  → al menos una condición debe ser True
# not → invierte el valor booleano
# Orden de precedencia: not → and → or

# Variables de ejemplo
a = 10
b = 5
c = 7

# Evaluaciones básicas
print(a > b and b < c)   # True and True → True
print(a > b or b > c)    # True or False → True
print(not (a > b))       # not(True) → False


# --------------------------------------------------
#  PRUEBAS RÁPIDAS
# --------------------------------------------------
print(5 > 3 and 2 < 4)     # True and True → True
print(10 == 5 or 3 != 3)   # False or False → False
print(not (7 <= 8))        # not(True) → False


# --------------------------------------------------
#  ORDEN DE OPERADORES
#  not → and → or
# --------------------------------------------------
# Ejemplo explicado:
#   7 <= 8 → True
#   not True → False
print(not (7 <= 8))


# --------------------------------------------------
#  EVALUACIONES COMPLEJAS
# --------------------------------------------------
print(True and False or True)             # (True and False) → False ; False or True → True
print(not (False and True))               # False and True → False ; not(False) → True
print(False or False or True)             # True
print(not (True and False))               # True
print(True and not (False or True))       # not(True) → False ; True and False → False
print(not True or not False)              # False or True → True
print((True or False) and not False)      # True and True → True
print(not (False and True) or (True and False))  # not(False) or False → True
print((True and True) or (False and not True))   # True or False → True
print(not (True or (False and True)))     # not(True or False) → False


# --------------------------------------------------
#  EDUCATIVO (comentario nivel aprendizaje)
# --------------------------------------------------
# and → todas las condiciones deben ser verdaderas para dar True.
# or  → con que una sola sea verdadera, da True.
# not → convierte True en False, y False en True.
# Importante: Python evalúa primero "not", luego "and" y al final "or".
# Este orden es clave para entender expresiones complejas.
