# Trabajo Practico 0 

## Este es el Trabajo Practico numero 0 de la materia Algoritmos y Programacion I.

De caracter individual. Fue entregado el dia 19 mayo de 2020.
A continuacion se describe el enunciado y el el repositorio bajo el nombre "Carmona_106483.py" se encuentra el mismo archivo que yo entregue. El trabajo obtuvo la condicion de aprobado y solo se corrijo el error de usar parentesis "()" para encerrar la devlucion de un return.


### El trabajo:

Alumnos, a continuación encontrarán el enunciado e indicaciones de como deben proceder.

Por favor, lean con atención.

1) La entrega deben realizarla antes de las 19:00 hs., del martes 19 de mayo, mediante una actividad que estará habilitada en el campus a tal fin.

2) Para que la entrega sea válida, deben respetar las condiciones de entrega que se estipulan en este mail, y las que figuren en el campus.

--3) Primero, copien y peguen en su editor de programa, todo lo que está en este mail entre las líneas # ++++++++++++++++++++++++++++++++

--4) Al archivo le deben dar como nombre su apellido, seguido por un guión bajo, y luego su número de padrón, por ejemplo: Perez_105435.py

--5) Sólo pueden subir el programa al campus, si pasó los casos de prueba, que están recibiendo junto con el enunciado.

--6) No deben alterar en nada, el código que cortaron y pegaron, sólo agregar las líneas de código de la función donde está indicado.


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
Aqui coloca tu Padron:
Aqui coloca tu Apellido y Nombre:
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
   
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#




#-------------------------------- Bloque Principal -----------------------------#

import doctest
doctest.testmod()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
