from calculadora_estatistica import CalculadoraEstatistica
from calculadora_mediana import CalculadoraMediana

numeros = [12, 8, 15, 5, 9, 21, 17, 42]
media = CalculadoraEstatistica.calcular_media(numeros)
mediana = CalculadoraMediana.calcular_mediana(numeros)

print(f"Números: {numeros}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
