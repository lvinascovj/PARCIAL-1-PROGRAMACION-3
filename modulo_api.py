from tabulate import tabulate
import pandas as pd
from sodapy import Socrata

client = Socrata ("www.datos.gov.co",None)

limite_registros=20
nombre_departamento="VALLE"


results = client.get ("gt2j-8ykr", limit=limite_registros,departamento_nom=nombre_departamento)

results_df = pd.DataFrame.from_records (results)

print (results_df.keys(), "\n")

subset = results_df[['departamento_nom', 'ciudad_municipio_nom', 'edad']]


print(tabulate(subset, tablefmt='github', headers=('DEPARTAMENTO', 'CIUDAD', 'EDAD')))





