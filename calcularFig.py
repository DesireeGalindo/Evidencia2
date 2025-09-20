import pandas as pd
from figuras import triangulo, circulo, rectangulo


df = pd.read_csv("figuras.csv")  # lee el archivo
print(df)


for index, row in df.iterrows():
    figura = row['FIGURA']
    base = row['MEDIDA1']
    altura = row['MEDIDA2']

    # calculamos según la figura
    if figura == 't':  # triángulo
        area, perimetro = triangulo(base, altura)
    elif figura == 'c':  # círculo
        area, perimetro = circulo(base) #es radio pero lo tomamos como base
    elif figura == 'r':  # rectángulo
        area, perimetro = rectangulo(base, altura)
    else:
        area, perimetro = None, None

    # print final con todo
    print(f"Fila {index}; FIGURA={figura}, MEDIDA1={base}, MEDIDA2={altura}, AREA={area}, PERIMETRO={perimetro}")

