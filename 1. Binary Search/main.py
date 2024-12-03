def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2  # Encontra o índice do meio
        if sorted_list[mid] == target:
            return mid  # Elemento encontrado, retorna o índice
        elif sorted_list[mid] < target:
            left = mid + 1  # Ajusta a busca para a metade direita
        else:
            right = mid - 1  # Ajusta a busca para a metade esquerda

    return -1  # Retorna -1 se o elemento não for encontrado


# Testando o algoritmo
sorted_list = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(sorted_list, target)
if result != -1:
    print(f"Elemento {target} encontrado no índice {result}.")
else:
    print(f"Elemento {target} não encontrado na lista.")
