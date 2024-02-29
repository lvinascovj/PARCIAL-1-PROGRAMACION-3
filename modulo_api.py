import pandas as pd
from sodapy import Socrata

def extraccion_datos(limite_registros, nombre_departamento):
    client = Socrata ("www.datos.gov.co",None)

    results = client.get ("gt2j-8ykr", limit=limite_registros,departamento_nom=nombre_departamento)
    results_df = pd.DataFrame.from_records (results)
    subset = results_df[['departamento_nom', 'ciudad_municipio_nom', 'edad', 'tipo_recuperacion', 'estado']]
    return subset






