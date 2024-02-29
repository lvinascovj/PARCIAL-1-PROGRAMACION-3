from unidecode import unidecode
import pandas as pd
from modulo_imprimir import imprimir_datos

departamento_nombre = input("\nIngrese el departamento sobre el cual quiere extraer los datos: ")#!NO LLAMAR LA FUNCION  CON ESTE
numero_registros = int(input("\nIngrese el numero de registros que desea observar: "))

if 'ñ' in departamento_nombre.lower():
    imprimir_datos(numero_registros, 'NARIÑO')
else:
    departamento_tildes = unidecode(departamento_nombre)#* ESTO ES PARA  NORMALIZAR EL STRING
    departamento_llamado = departamento_tildes.upper()#*ESTE  VA  A SER EL  STRING QUE SE  LLAMA EN LA FUNCION

    imprimir_datos(numero_registros, 'NARIÑO')





