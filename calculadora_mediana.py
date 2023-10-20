class CalculadoraMediana:
    @staticmethod
    def calcular_mediana(numeros):
        numeros_ordenados = sorted(numeros)
        tamanho = len(numeros_ordenados)
        if tamanho % 2 == 0:
            meio = tamanho // 2
            mediana = (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
        else:
            meio = tamanho // 2
            mediana = numeros_ordenados[meio]
        return mediana
