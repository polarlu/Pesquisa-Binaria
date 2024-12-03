# Implementação do Binary Search
def binary_search(lista, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == target:
            return mid
        elif lista[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Implementação do Ternary Search
def ternary_search(lista, low, high, target):
    while high >= low:
        # Calculando os três pontos de divisão
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        # Verificando se encontramos o elemento
        if lista[mid1] == target:
            return mid1
        elif lista[mid2] == target:
            return mid2
        
        # Se o alvo for menor que mid1, a busca vai para a primeira parte
        elif target < lista[mid1]:
            high = mid1 - 1
        
        # Se o alvo for maior que mid2, a busca vai para a terceira parte
        elif target > lista[mid2]:
            low = mid2 + 1
        
        # Caso contrário, a busca vai para a parte do meio
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1

# Função para testar os algoritmos
def testar_busca():
    lista = [i for i in range(1, 10001)]  # Lista de 1 a 10000
    
    target = 5555  # Elemento a ser buscado
    
    # Testando Binary Search
    print("Testando Binary Search...")
    binary_result = binary_search(lista, 0, len(lista) - 1, target)
    print(f"Elemento {target} encontrado no índice (Binary Search): {binary_result}")
    
    # Testando Ternary Search
    print("Testando Ternary Search...")
    ternary_result = ternary_search(lista, 0, len(lista) - 1, target)
    print(f"Elemento {target} encontrado no índice (Ternary Search): {ternary_result}")

# Executar os testes
testar_busca()
