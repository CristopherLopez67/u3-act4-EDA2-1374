import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear diccionario con datos de tipos de semillas
tipos_semillas = {
    'id_semilla': [301, 302, 303, 304, 305, 306],
    'cultivo': ['Maiz', 'Trigo', 'Frijol', 'Soya', 'Sorgo', 'Avena'],
    'variedad': ['Hibrido A', 'Trigo duro', 'Negro Jamapa', 'Transgenica B', 'Sorgo forrajero', 'Avena blanca'],
    'proveedor': ['Semillas MX', 'AgroGlobal', 'Semillas MX', 'BioTech', 'AgroGlobal', 'Semillas MX'],
    'precio_kg': [150, 80, 120, 200, 60, 70],
    'germinacion_porcentaje': [95, 90, 85, 98, 88, 92],
    'ciclo_dias': [120, 150, 90, 110, 100, 130],
    'stock_kg': [500, 300, 200, 150, 400, 250],
    'tratamiento': ['Fungicida', 'Ninguno', 'Insecticida', 'Herbicida', 'Ninguno', 'Fungicida'],
    'lote': ['L23-01', 'L23-02', 'L23-03', 'L23-04', 'L23-05', 'L23-06']
}

print("Análisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis por Cristopher Lopez Nc 1374 ")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(tipos_semillas)
print("\n--- TABLA ORIGINAL DE TIPOS DE SEMILLAS ---")
print(df)

# 3. Exportar los datos a CSV
print("-+-+-+ Convertir el DataFrame en archivo CSV")
df.to_csv(
    'tipos_semillas_1374.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("-+-+-+ 8. Leer los datos desde el archivo CSV -+-+-+-+")
print("tipos_semillas_1374.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('tipos_semillas_1374.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("+--+-+9. Análisis Exploratorio de Datos (EDA)-++++--+")

# 5. Primeros y últimos registros
print("-++-+- \n1. PRIMEROS REGISTROS (Head): -+-+-+")
print(df.head(3))  # Muestra los primeros 3
print("-+-+-+-+ \n2. ÚLTIMOS REGISTROS (Tail): -+-+-+-+")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("-+-+-+-+ 6. Dimensiones y estructura -++--+-+")
print(df)  # mostrar tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("-*-*-*+- \n7. ESTADÍSTICAS DESCRIPTIVAS:-+*+-*+-*")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Proveedores únicos:", df['proveedor'].unique())

# 8. Análisis específico
print(df)
print("--------------------------------------------------------")
print("\n11. SEMILLAS POR PROVEEDOR:")
print(df['proveedor'].value_counts())

print("\n12. PROMEDIO DE PRECIO POR KG: $", df['precio_kg'].mean())
print("13. PRECIO MÁXIMO POR KG: $", df['precio_kg'].max())
print("14. PRECIO MÍNIMO POR KG: $", df['precio_kg'].min())

# 9. Ordenamiento, filtrado y agrupación
print("-+-+-+-+ 9. Ordenamiento, filtrado y agrupación -++--+-+")
print(df)
print("--------------------------------------------------------")
print("-++-+-+\n15. SEMILLAS ORDENADAS POR PRECIO (Mayor a menor):--+-++-")
print(df.sort_values(by='precio_kg', ascending=False))

print("\n16. SEMILLAS CON PRECIO MAYOR A $100:")
filtro = df[df['precio_kg'] > 100]
print(filtro)

print("\n17. RESUMEN POR PROVEEDOR:")
resumen = df.groupby('proveedor').agg(
    semillas=('id_semilla', 'count'),
    precio_promedio=('precio_kg', 'mean'),
    precio_maximo=('precio_kg', 'max')
)
print(resumen)

# 18. Gráfica de barras: Semillas por proveedor
print("# 18. Gráfica de barras: Semillas por proveedor")
conteo = df['proveedor'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Tipos de semillas por proveedor Cristopher Lopez NC 1374')
plt.xlabel('Proveedor')
plt.ylabel('Cantidad de semillas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Precio por kg por cultivo
plt.figure(figsize=(8, 5))
plt.bar(df['cultivo'], df['precio_kg'], color='lightgreen')
plt.title('Precio por kg por cultivo EDA Cristopher Lopez Nc 1374')
plt.xlabel('Cultivo')
plt.ylabel('Precio por kg en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de ciclos en días
plt.figure(figsize=(8, 5))
plt.hist(df['ciclo_dias'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de ciclos de cultivo (días) EDA Cristopher Lopez NC 1374')
plt.xlabel('Ciclo (días)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Germinación (%) vs Precio por kg
plt.figure(figsize=(8, 5))
plt.scatter(df['germinacion_porcentaje'], df['precio_kg'], color='red', s=100)
plt.title('Relación entre germinación (%) y precio por kg EDA Cristopher Lopez NC 1374')
plt.xlabel('Porcentaje de germinación (%)')
plt.ylabel('Precio por kg')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de precios por kg
plt.figure(figsize=(7, 5))
plt.boxplot(df['precio_kg'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de precios por kg (Boxplot) EDA Cristopher Lopez nc 1374')
plt.ylabel('Precio por kg')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Cristopher Lopez Nc 1374')
plt.tight_layout()
plt.show()