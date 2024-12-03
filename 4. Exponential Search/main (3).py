import math
import time

# Função de Pesquisa Binária
def binary_search(lista_ordenada, alvo, baixo, alto):
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

# Função de Pesquisa Exponencial
def exponential_search(lista_ordenada, alvo):
    # Se o alvo é o primeiro elemento
    if lista_ordenada[0] == alvo:
        return 0

    # Encontre o intervalo de busca usando um salto exponencial
    tamanho = len(lista_ordenada)
    indice = 1
    while indice < tamanho and lista_ordenada[indice] < alvo:
        indice *= 2

    # Realize a busca binária no intervalo encontrado
    return binary_search(lista_ordenada, alvo, indice // 2, min(indice, tamanho - 1))

# Função para testar o Exponential Search
def testar_exponential_search():
    lista_ordenada = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    alvo = 128

    # Chama o Exponential Search
    resultado = exponential_search(lista_ordenada, alvo)
    
    if resultado != -1:
        print(f"Elemento {alvo} encontrado na posição {resultado}.")
    else:
        print(f"Elemento {alvo} não encontrado.")

# Função para comparar os tempos de Exponential Search e Binary Search
def comparar_desempenho_exponential():
    tamanhos = [10**3, 10**4, 10**5, 10**6]
    alvo = 500

    for tamanho in tamanhos:
        lista_ordenada = list(range(tamanho))

        # Medindo o tempo do Exponential Search
        inicio_exp = time.time()
        exponential_search(lista_ordenada, alvo)
        tempo_exp = time.time() - inicio_exp

        # Medindo o tempo do Binary Search
        inicio_bin = time.time()
        binary_search(lista_ordenada, alvo, 0, len(lista_ordenada)-1)
        tempo_bin = time.time() - inicio_bin

        print(f"Tamanho da lista: {tamanho}")
        print(f"Tempo do Exponential Search: {tempo_exp:.6f} segundos")
        print(f"Tempo do Binary Search: {tempo_bin:.6f} segundos")
        print("-" * 40)

# Executa o teste de Exponential Search
testar_exponential_search()

# Executa a comparação de desempenho
comparar_desempenho_exponential()
