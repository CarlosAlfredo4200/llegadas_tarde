
# 📄 Script de Conversión de Excel a JSON por Identificación

Este script en Python permite procesar un archivo Excel que contiene identificaciones (`num_identificacion`) y fechas, convirtiendo las fechas a formato ISO 8601, agrupándolas por identificación, y exportando el resultado a un archivo JSON.

---

## 🚀 Funcionalidad

- Lee un archivo Excel (`.xlsx`) con columnas `num_identificacion` y `fechas`.
- Convierte las fechas a formato ISO 8601 (`YYYY-MM-DDTHH:MM:SS.000Z`).
- Agrupa todas las fechas por número de identificación.
- Genera un archivo `output.json` con la estructura agrupada.

---

## 📦 Requisitos

Asegúrate de tener instalado Python 3 y las siguientes dependencias:

```bash
pip install pandas openpyxl
```

> `openpyxl` es necesario para poder leer archivos `.xlsx` con `pandas`.

---

## 📁 Estructura esperada del archivo Excel

El archivo `base.xlsx` debe contener al menos las siguientes columnas:

| num_identificacion | fechas           |
|--------------------|------------------|
| 123456789          | 2024-05-15       |
| 123456789          | 2024-06-10       |
| 987654321          | 2024-05-22       |

---

## 🛠️ Uso

1. Coloca tu archivo Excel en el mismo directorio del script y nómbralo como `base.xlsx` (o cambia el valor de `ARCHIVO_EXCEL` en el código).
2. Ejecuta el script:

```bash
python llegadas_tarde_excel_json.py
```

3. Se generará un archivo llamado `output.json` con la siguiente estructura:

```json
[
    {
        "num_identificacion": "123456789",
        "fechas": [
            "2024-05-15T00:00:00.000Z",
            "2024-06-10T00:00:00.000Z"
        ]
    },
    {
        "num_identificacion": "987654321",
        "fechas": [
            "2024-05-22T00:00:00.000Z"
        ]
    }
]
```

---

## 📂 Salida

- **`output.json`**: archivo generado con los datos agrupados y transformados.

---

## 🧑‍💻 Autor

**Alfredo Montoya**  
Correo: [TuEmail@ejemplo.com]  
GitHub: [@CarlosAlfredo4200](https://github.com/CarlosAlfredo4200)

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](LICENSE).
