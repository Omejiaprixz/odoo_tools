import pandas as pd

# Ruta al archivo Excel
file_path = "ids.xlsx"

# Leer el archivo Excel
try:
    df = pd.read_excel(file_path, sheet_name="Sheet1")
except FileNotFoundError:
    print(f"No se encontró el archivo {file_path}")
    exit(1)
except ValueError:
    print(f"No se encontró la hoja de trabajo 'Sheet1' en el archivo {file_path}")
    exit(1)

# Construir la lista de IDs
try:
    ids = df.iloc[:, 0].dropna().astype(int).tolist()
except ValueError:
    print("Error al convertir los valores de la primera columna a enteros")
    exit(1)

# Imprimir la lista de IDs
print("Lista de IDs:", ids)

# Función para construir el filtro de Odoo
def build_odoo_filter(ids):
    filter_str = "[[\"id\", \"in\", ["
    filter_str += ", ".join(map(str, ids))
    filter_str += "]]]"
    return filter_str

# Construir el filtro de Odoo
odoo_filter = build_odoo_filter(ids)

# Imprimir el filtro de Odoo
print("Filtro de Odoo:", odoo_filter)
