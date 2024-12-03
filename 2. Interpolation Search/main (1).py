# Pesquisa Interpolada
def pesquisa_interpolada(lista_ordenada, alvo):
    baixo = 0
    alto = len(lista_ordenada) - 1

    while baixo <= alto and alvo >= lista_ordenada[baixo] and alvo <= lista_ordenada[alto]:
        # Estima a posição usando interpolação
        pos = baixo + ((alvo - lista_ordenada[baixo]) * (alto - baixo)) // (lista_ordenada[alto] - lista_ordenada[baixo])

        # Se o alvo for encontrado
        if lista_ordenada[pos] == alvo:
            return pos

        # Ajusta os limites conforme o valor
        if lista_ordenada[pos] < alvo:
            baixo = pos + 1
        else:
            alto = pos - 1

    return -1  # Retorna -1 se o elemento não for encontrado


# Pesquisa Binária
def pesquisa_binaria(lista_ordenada, alvo):
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


# Testando as funções
lista_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista_nao_uniforme = [1, 2, 3, 50, 100, 500, 1000, 5000]

print("Comparação com a Pesquisa Binária - Lista Uniforme:")
print("Pesquisa Binária:", pesquisa_binaria(lista_uniforme, 70))  # Deve retornar 6
print("Pesquisa Interpolada:", pesquisa_interpolada(lista_uniforme, 70))  # Deve retornar 6

print("\nComparação com a Pesquisa Binária - Lista Não Uniforme:")
print("Pesquisa Binária:", pesquisa_binaria(lista_nao_uniforme, 500))  # Deve retornar 5
print("Pesquisa Interpolada:", pesquisa_interpolada(lista_nao_uniforme, 500))  # Deve retornar 5
