import pandas as pd
from figuras import triangulo, circulo, rectangulo



df = pd.read_csv("figuras.csv") #lee el archivo
print(df)


for index, row in df.iterrows():
	print(f"Fila {index}; FIGURA={row['FIGURA']}, MEDIDA1={row['MEDIDA1']}, MEDIDA2={row['MEDIDA 2']}")

