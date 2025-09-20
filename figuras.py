# Cálculo de figuras
import math


# Figura de triángulo
def triangulo(base, altura):
    """Calcula el área y perímetro del triángulo (rectángulo)"""
    area = (base * altura) / 2
    hipotenusa = math.sqrt(base ** 2 + altura ** 2)
    perimetro = base + altura + hipotenusa
    return area, perimetro

    
# Figura del círculo
def circulo(radio):
    """Calcula el área y perímetro del círculo"""
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    return area, perimetro


# Figura de rectángulo
def rectangulo(base, altura):
    """Calcula el área y perímetro del rectángulo"""
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro  



