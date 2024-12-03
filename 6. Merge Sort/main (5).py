# Função para mesclar duas sublistas ordenadas
def merge(lista_esquerda, lista_direita):
    resultado = []
    i = j = 0

    # Mescla as duas listas comparando seus elementos
    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] < lista_direita[j]:
            resultado.append(lista_esquerda[i])
            i += 1
        else:
            resultado.append(lista_direita[j])
            j += 1

    # Se houver elementos restantes em lista_esquerda
    while i < len(lista_esquerda):
        resultado.append(lista_esquerda[i])
        i += 1

    # Se houver elementos restantes em lista_direita
    while j < len(lista_direita):
        resultado.append(lista_direita[j])
        j += 1

    return resultado

# Função de Merge Sort para ordenar números inteiros
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])  # Ordena a metade esquerda
    direita = merge_sort(lista[meio:])  # Ordena a metade direita

    # Mescla as duas metades ordenadas
    return merge(esquerda, direita)

# Função de Merge Sort modificada para ordenar strings em ordem alfabética
def merge_sort_strings(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort_strings(lista[:meio])  # Ordena a metade esquerda
    direita = merge_sort_strings(lista[meio:])  # Ordena a metade direita

    # Mescla as duas metades ordenadas
    return merge(esquerda, direita)

# Função para testar a ordenação de números inteiros
def testar_merge_sort_numeros():
    numeros = [34, 7, 23, 32, 5, 62]
    print("Lista original de números:", numeros)
    numeros_ordenados = merge_sort(numeros)
    print("Lista ordenada de números:", numeros_ordenados)

# Função para testar a ordenação de strings
def testar_merge_sort_strings():
    palavras = ["banana", "maçã", "laranja", "abacaxi", "kiwi"]
    print("Lista original de palavras:", palavras)
    palavras_ordenadas = merge_sort_strings(palavras)
    print("Lista ordenada de palavras:", palavras_ordenadas)

# Executa os testes
testar_merge_sort_numeros()
testar_merge_sort_strings()
