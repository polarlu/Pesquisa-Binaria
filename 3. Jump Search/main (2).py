import math
import time

# Função de Pesquisa Binária
def binary_search(lista_ordenada, alvo):
    esquerdo = 0
    direito = len(lista_ordenada) - 1

    while esquerdo <= direito:
        meio = (esquerdo + direito) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            esquerdo = meio + 1
        else:
            direito = meio - 1

    return -1

# Função de Pesquisa Interpolada
def jump_search(lista_ordenada, alvo):
    n = len(lista_ordenada)
    salto = int(math.sqrt(n))  # Determina o tamanho do salto
    anterior = 0

    # Faz saltos até encontrar o intervalo certo
    while anterior < n and lista_ordenada[min(salto, n) - 1] < alvo:
        anterior = salto
        salto += int(math.sqrt(n))
        if anterior >= n:
            return -1

    # Pesquisa linear dentro do intervalo
    for i in range(anterior, min(salto, n)):
        if lista_ordenada[i] == alvo:
            return i

    return -1  # Retorna -1 se o elemento não for encontrado

# Função para comparar os algoritmos
def comparar_algoritmos():
    tamanhos = [10**3, 10**4, 10**5, 10**6]
    alvo = 500

    for tamanho in tamanhos:
        lista_ordenada = list(range(tamanho))

        # Medindo o tempo do Jump Search
        inicio_jump = time.time()
        jump_search(lista_ordenada, alvo)
        tempo_jump = time.time() - inicio_jump

        # Medindo o tempo do Binary Search
        inicio_binary = time.time()
        binary_search(lista_ordenada, alvo)
        tempo_binary = time.time() - inicio_binary

        print(f"Tamanho da lista: {tamanho}")
        print(f"Tempo do Jump Search: {tempo_jump:.6f} segundos")
        print(f"Tempo do Binary Search: {tempo_binary:.6f} segundos")
        print("-" * 40)

# Chama a função para comparar os algoritmos
comparar_algoritmos()
