df["vendedor"] = df["vendedor"].str.lower()
df["region"] = df["region"].str.lower()

print(f'\n \n{df}')

# Buscar filas duplicadas (devuelve True o False)
# print(df.duplicated())

# Contar cuántas filas duplicadas existen
print(f'\nDuplicatos iniciales existentes: {df.duplicated().sum()}')

# Eliminar las filas duplicadas
df.drop_duplicates()
print(f'Duplicados actuales: {df.duplicated().sum()}')

df.groupby("vendedor")["cantidad"].sum()

print(df)