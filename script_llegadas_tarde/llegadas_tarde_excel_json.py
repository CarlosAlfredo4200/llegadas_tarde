"""
Este script carga un archivo Excel con identificaciones y fechas,
convierte las fechas a formato ISO 8601, agrupa las fechas por identificación
y guarda el resultado en un archivo JSON.
"""

import json
from collections import defaultdict
import pandas as pd



# Cargar el archivo Excel, asegurando que num_identificacion sea tratado como string
ARCHIVO_EXCEL = "./base.xlsx"  # Reemplázalo con el nombre de tu archivo
df = pd.read_excel(ARCHIVO_EXCEL, dtype={"num_identificacion": str})

# Convertir la columna de fechas a formato ISO 8601 (con formato de fecha y hora)
df["fechas"] = pd.to_datetime(df["fechas"]).dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")

# Agrupar fechas por num_identificacion
data = defaultdict(list)
for _, row in df.iterrows():
    data[row["num_identificacion"]].append(row["fechas"])

# Convertir a formato JSON deseado
json_output = [{"num_identificacion": k, "fechas": v} for k, v in data.items()]

# Guardar el JSON en un archivo
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(json_output, f, indent=4, ensure_ascii=False)

print("Archivo JSON generado correctamente.")
