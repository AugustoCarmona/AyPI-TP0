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

    pos, vocales, mayusculas, minusculas = 0, 0, 0, 0
    devolver = False

    if (clave.isalpha()) and (clave[-1].islower()) and (4 <= len(clave) <= 10):

        for i in range(0 , len(clave)):

            if clave[i] in 'aeiouAEIOU':
                vocales += 1
            
            elif not clave[i].islower():         
                mayusculas += 1
            
            elif clave[i].islower():
                minusculas += 1

            pos += 1

        if (minusculas > mayusculas) and (vocales <= 2):
            devolver = True

    return(devolver)

# -------------------------------- Bloque Principal -----------------------------#

import doctest
doctest.testmod()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++