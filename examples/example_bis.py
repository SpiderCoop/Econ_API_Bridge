# Ejemplo de uso
import sys
import os
import pandas as pd
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api_caller.bis import BIS_API

# Ejemplo de uso de la clase API_Banxico|
bis_api = BIS_API()
serie_id = ['Q.MX.P.A.M.770.A', 'Q.US.P.A.M.770.A']

# Obtener datos de la serie desde 2023-01-01 hasta hoy
serie = bis_api.get_series_data(serie_id)

print(serie.head())
print('\n')