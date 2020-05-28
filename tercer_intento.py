def validar_clave(clave):

    """ Casos de Prueba:

    >>> validar_clave("florencia25")
    False
    >>> validar_clave("eAEIOui")
    False
    >>> validar_clave("97532")
    False
    >>> validar_clave("1AE5b2")
    False
    >>> validar_clave("dia")
    False
    >>> validar_clave("dias")
    True
    >>> validar_clave("LuneS")
    False
    >>> validar_clave("Lunes")
    True
    >>> validar_clave("aBcdeio")
    False
    >>> validar_clave("aBcdenm")
    True
    >>> validar_clave("AUGUSTO")
    False
    >>> validar_clave("Abarth")
    True
    >>> validar_clave("pepinillos")
    False
    >>> validar_clave("Glovo")
    True
   
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#

    pos, vocales, minusculas = 0, 0, 0
    devolver = False

    if (clave.isalpha()) and (clave[-1].islower()) and (4 <= len(clave) <= 10):

        while (pos < len(clave)) and (vocales <= 2):    # opté por un ciclo while para que en caso de encontrar más de 2 vocales deje de recorrerse la clave 

            if clave[pos] in 'aeiouAEIOU':
                vocales += 1
            
                elif clave[pos].islower():
                minusculas += 1
            
            elif not clave[pos].islower():      # si hay menos minúsculas que mayúsculas el contador será negativo, y, si la cantidad de mayúsculas y minúsculas es igual el contador será igual a cero
                minusculas -= 1

            pos += 1

        if (len(clave) == pos) and (minusculas > 0):   # si cuando terminó el ciclo se recorrió toda la clave y la cantidad de minúsculas es positiva la variable pasará a ser True
            devolver = True

    return(devolver)

# -------------------------------- Bloque Principal -----------------------------#

import doctest
doctest.testmod()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++