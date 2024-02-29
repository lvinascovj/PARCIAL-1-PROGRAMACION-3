from tabulate import tabulate
import pandas as pd
from modulo_api import extraccion_datos

def imprimir_datos(cantidad_registros, departamento):
    print(tabulate(extraccion_datos(cantidad_registros, departamento), tablefmt='github', headers=('NUMERO DEL REGISTRO','DEPARTAMENTO', 'CIUDAD', 'EDAD', 'TIPO', 'ESTADO')))


