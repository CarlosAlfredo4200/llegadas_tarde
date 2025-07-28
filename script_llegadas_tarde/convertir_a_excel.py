import pandas as pd
import json

# Cargar los datos del archivo JSON con codificación UTF-8
with open('./llegadastardePeriodo3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Crear una lista de diccionarios con los datos deseados
processed_data = []

for item in data:
    # Concatenar el nombre completo
    nombre_completo = f"{item['primer_nombre']} {item['segundo_nombre']} {item['primer_apellido']} {item['segundo_apellido']}"
    
    # Unir las fechas en una sola cadena
    fechas = ", ".join(item['fechas'])
    
    # Agregar los datos procesados a la lista
    processed_data.append({
        "Nombre": nombre_completo,
        "Número de Identificación": item["num_identificacion"],
        "Grupo": item["grupo"],
        "Grado": item["grado"],
        "Fechas": fechas
    })

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(processed_data)

# Guardar los datos en un archivo Excel
output_file = "llegadas_tarde.xlsx"
df.to_excel(output_file, index=False)

print(f"Archivo Excel generado: {output_file}")
