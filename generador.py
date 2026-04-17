def GenerarCadenas (alfabeto, max_len):
    #resultado ← lista con elemento ""
    resultado = [""]

    #PARA i DESDE 1 HASTA max_len HACER
    for i in range(1, max_len +1):
        nuevas = []
        for cadena in resultado:
            for simbolo in alfabeto:
                nueva_cadena = cadena + simbolo
                nuevas.append(nueva_cadena)
        resultado.extend(nuevas)
    
    final = []
    for elemento in resultado:
        if elemento not in final:
            final.append(elemento)
            
    return final

#prueba
"""prueba = GenerarCadenas(['a', 'b', 'c'], 3)
print(prueba)"""


# Ejercicio 2: Pertenencia
def Pertenece(cadena, lenguaje):
    for elemento in lenguaje:
        if elemento == cadena:
            return True
    return False

#prueba
"""lenguaje = ['a', 'b', 'c']
print(Pertenece('ab', lenguaje)) # False
print(Pertenece('abc', lenguaje)) # False
print(Pertenece('c', lenguaje)) # True
print(Pertenece('b', lenguaje)) # True"""

# Ejercicio 3: Unión
def Union(L1, L2):
    resultado = L1.copy()
    for elemento in L2:
        if elemento not in resultado:
            resultado.append(elemento)
    
    return resultado 

#prueba
"""L1 = ['a', 'b', 'c', 'd']
L2 = ['e', 'b', 'c', 'a']
print(Union(L1, L2)) # ['a', 'b', 'c', 'd', 'e']"""

# Ejercicio 4: Concatenación
def Concatenacion(L1, L2):
    resultado = []
    for x in L1:
        for y in L2:
            nueva = x + y
            resultado.append(nueva)
    return resultado

#prueba
"""L1 = ['a', 'b']
L2 = ['c', 'd']
print(Concatenacion(L1, L2)) 
"""

# Ejercicio 5: Clausura de Kleene
def kleeneStar(L, max_iter):
    resultado = [""]
    actual = [""]
    
    for i in range(1, max_iter +1):
        nuevo = []
        for x in actual:
            for y in L:
                cadena = x + y
                nuevo.append(cadena)
        for elemento in nuevo:
            if elemento not in resultado:
                resultado.append(elemento)
        actual = nuevo
    return resultado

"""#prueba
L = ['a', 'b']
print(kleeneStar(L, 2)) """

# Kleene Plus 
def kleenePlus(L, max_iter):
    ks = kleeneStar(L, max_iter)
    resultado = []
    for elemento in ks:
        if elemento != "":
            resultado.append(elemento)
    return resultado

#prueba
"""L = ['a', 'b']
print(kleenePlus(L, 2))"""

# Ejercicio 7: Crecimiento del Lenguaje 
def analizar_crecimiento(L):
    #PARA i DESDE 1 HASTA 5 HACER
    for i in range(1, 6): 
        resultado = kleeneStar(L, i)
        print(f"Iteración: {i}")
        print(f"Cantidad: {len(resultado)}")

#prueba
"""L = ['a', 'b', 'c']
analizar_crecimiento(L)"""