#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Escribir una función para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres alfabeticos, inclusive.
- Estar formada por mayor cantidad de letras minusculas que mayusculas.
- El ultimo caracter, debe ser una letra minuscula.
- La clave puede tener como maximo 2 caracteres que sean vocales.

*******************************************************************************
Aqui coloca tu Padron: 106483
Aqui coloca tu Apellido y Nombre: Carmona Perez, Augusto
*******************************************************************************
"""

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
    """
    Notas:

    El profesor recomendo en clase que intentemos acostumbrarnos a escribir código en inglés (ya que es el standar de la industria), pero a su vez
    que es preferible mantener un mismo idioma en todo el código. 
    Como el ejercicio y el nombre de la función estaban en español, respete el español como lenguaje en todo el programa para declarar las variables.

    En el caso de que no recordara el método .islower() podría utilizar el código: elif clave[pos] in 'abcdefghijklmnñopqrstuvwxyz'

    """
    pos, vocales, minusculas = 0, 0, 0
    devolver = False

    if (clave.isalpha()) and (clave[-1].islower()) and (4 <= len(clave) <= 10):

        while (pos < len(clave)) and (vocales <= 2):        # opté por un ciclo while para que en caso de encontrar más de 2 vocales deje de recorrerse la clave
            
            if clave[pos] in 'aeiouAEIOU':
                vocales += 1
            
            elif clave[pos].islower():
                minusculas += 1
            
            elif not clave[pos].islower():      # si hay menos minúsculas que mayúsculas el contador será negativo, y, si la cantidad de mayúsculas y minúsculas es igual el contador será igual a cero
                minusculas -= 1
            
            pos += 1

        if (len(clave) == pos) and (minusculas > 0):        # si cuando terminó el ciclo se recorrió toda la clave y la cantidad de minúsculas es positiva la variable pasará a ser True
            devolver = True

    return(devolver)

# -------------------------------- Bloque Principal -----------------------------#

import doctest
doctest.testmod()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++