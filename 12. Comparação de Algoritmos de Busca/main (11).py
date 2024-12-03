import time
import random

# Função para medir o tempo de execução de Binary Search
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

# Função para medir o tempo de execução de Interpolation Search
def interpolation_search(lista, low, high, target):
    while low <= high and target >= lista[low] and target <= lista[high]:
        # Estimando a posição de busca
        pos = low + ((target - lista[low]) * (high - low)) // (lista[high] - lista[low])
        if lista[pos] == target:
            return pos
        elif lista[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Função para medir o tempo de execução de Jump Search
def jump_search(lista, target):
    n = len(lista)
    step = int(n ** 0.5)  # Tamanho do salto
    prev = 0
    while lista[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if lista[i] == target:
            return i
    return -1

# Função para medir o tempo de execução de Exponential Search
def exponential_search(lista, target):
    n = len(lista)
    if lista[0] == target:
        return 0
    i = 1
    while i < n and lista[i] <= target:
        i *= 2
    return binary_search(lista, i // 2, min(i, n - 1), target)

# Função para medir o tempo de execução dos algoritmos
def testar_algoritmos():
    tamanhos = [10, 100, 1000, 10000, 100000]
    resultados = []
    
    for tamanho in tamanhos:
        lista = sorted(random.sample(range(1, 1000000), tamanho))  # Lista aleatória e ordenada
        
        target = lista[tamanho // 2]  # Procurar pelo valor do meio
        
        # Testando Binary Search
        start_time = time.time()
        binary_search(lista, 0, len(lista) - 1, target)
        binary_search_time = time.time() - start_time
        
        # Testando Interpolation Search
        start_time = time.time()
        interpolation_search(lista, 0, len(lista) - 1, target)
        interpolation_search_time = time.time() - start_time
        
        # Testando Jump Search
        start_time = time.time()
        jump_search(lista, target)
        jump_search_time = time.time() - start_time
        
        # Testando Exponential Search
        start_time = time.time()
        exponential_search(lista, target)
        exponential_search_time = time.time() - start_time
        
        resultados.append({
            "Tamanho": tamanho,
            "Binary Search (s)": binary_search_time,
            "Interpolation Search (s)": interpolation_search_time,
            "Jump Search (s)": jump_search_time,
            "Exponential Search (s)": exponential_search_time
        })
    
    # Imprimir a tabela
    print(f"{'Tamanho':<10}{'Binary Search (s)':<20}{'Interpolation Search (s)':<25}{'Jump Search (s)':<20}{'Exponential Search (s)'}")
    for resultado in resultados:
        print(f"{resultado['Tamanho']:<10}{resultado['Binary Search (s)']:<20}{resultado['Interpolation Search (s)']:<25}{resultado['Jump Search (s)']:<20}{resultado['Exponential Search (s)']}")

# Executar os testes
testar_algoritmos()
