import pandas as pd  # Importa la librería Pandas

# Leer un archivo CSV y guardarlo en un DataFrame
df = pd.read_csv("ventas.csv")

# ======================================
# EJERCICIO:
# Identificar los pedidos duplicados y eliminarlos.
# ======================================

# Mostrar las primeras 5 filas del DataFrame
print(df.head())

df = df.drop_duplicates() 

# Mostrar estadísticas de las columnas numéricas
print(df.describe())


# Verificar que ya no existan duplicados
print(df.duplicated().sum())


# ======================================
# CONVERTIR TEXTO A MAYÚSCULAS
# ======================================

# Recorre todas las columnas y convierte a mayúsculas
# solo las que contienen texto.
#df = df.apply(
#    lambda col: col.str.upper()
#   if pd.api.types.is_string_dtype(col)
#    else col
#)

# print(df)




# ======================================
# PREGUNTA 2
# ======================================

print('\n \n \n \n  2. unificar los nombres para calular las comiciones')

# ======================================
# CONVERTIR TEXTO A MINÚSCULAS
# ======================================



# aqui estoy normalizado las columnas a minusculas para luego logar unificar aquellas que son completamente igu