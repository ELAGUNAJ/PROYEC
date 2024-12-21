import pandas as pd
import numpy as np

# Cargar datos desde un archivo CSV
# Cambia 'productos.csv' por la ruta de tu archivo
df = pd.read_csv("productos.csv")

# Vista inicial de los datos
print("Datos iniciales:")
print(df.head())

# 1. Eliminar filas duplicadas
df = df.drop_duplicates()
print("\nDatos después de eliminar duplicados:")
print(df.head())

# 2. Manejar valores nulos: reemplazar valores nulos en la columna 'precio' por la media
if df['precio'].isnull().sum() > 0:
    df['precio'].fillna(df['precio'].mean(), inplace=True)

# Reemplazar valores nulos en 'cantidad' por 0
df['cantidad'].fillna(0, inplace=True)

# 3. Limpiar texto: eliminar espacios en blanco adicionales en 'nombre' y 'marca'
df['nombre'] = df['nombre'].str.strip()
df['marca'] = df['marca'].str.strip()

# 4. Crear nuevas columnas (si es necesario)
# Por ejemplo, categorizar productos caros (precio > 200)
df['es_caro'] = np.where(df['precio'] > 200, 'Sí', 'No')

# 5. Transformación de datos: convertir 'precio' y 'cantidad' en enteros si se requiere
df['precio'] = df['precio'].astype(float)
df['cantidad'] = df['cantidad'].astype(int)

# 6. Eliminar columnas innecesarias (si aplica)
# Ejemplo: eliminar la columna 'descripcion'
df.drop(columns=['descripcion'], inplace=True)

# 7. Renombrar columnas para facilitar el manejo
df.rename(columns={'nombre': 'producto', 'marca': 'fabricante'}, inplace=True)

# Vista final de los datos
print("\nDatos limpios y transformados:")
print(df.head())

# Guardar los datos limpios en un nuevo archivo CSV
df.to_csv("productos_limpios.csv", index=False)
