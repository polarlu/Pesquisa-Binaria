import time
import random
import matplotlib.pyplot as plt

# Funções de busca

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Funções de ordenação

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Função para medir o tempo de execução
def measure_time(func, arr, *args):
    start_time = time.time()
    result = func(arr[:], *args)  # Faz uma cópia da lista para não alterar a original
    end_time = time.time()
    return result, end_time - start_time

# Função para comparação entre diferentes algoritmos de busca e ordenação
def run_program():
    print("Escolha uma opção:")
    print("1. Buscar um elemento")
    print("2. Ordenar uma lista")
    choice = int(input("Digite sua escolha (1 ou 2): "))
    
    # Gerando uma lista aleatória de inteiros
    arr = [random.randint(1, 1000) for _ in range(1000)]
    
    if choice == 1:
        # Escolher algoritmo de busca
        print("\nEscolha o algoritmo de busca:")
        print("1. Busca Binária")
        print("2. Busca Linear")
        print("3. Busca por Interpolação")
        search_choice = int(input("Digite sua escolha (1, 2 ou 3): "))
        
        # Definir o número a ser procurado
        x = int(input("\nDigite o valor a ser buscado: "))
        
        # Medir o tempo de execução de cada algoritmo
        if search_choice == 1:
            result, exec_time = measure_time(binary_search, arr, x)
        elif search_choice == 2:
            result, exec_time = measure_time(linear_search, arr, x)
        elif search_choice == 3:
            result, exec_time = measure_time(interpolation_search, arr, x)
        
        if result != -1:
            print(f"\nElemento {x} encontrado no índice {result}.")
        else:
            print(f"\nElemento {x} não encontrado.")
        print(f"Tempo de execução: {exec_time:.6f} segundos.")
    
    elif choice == 2:
        # Escolher algoritmo de ordenação
        print("\nEscolha o algoritmo de ordenação:")
        print("1. Bubble Sort")
        print("2. Quick Sort")
        print("3. Selection Sort")
        sort_choice = int(input("Digite sua escolha (1, 2 ou 3): "))
        
        # Medir o tempo de execução de cada algoritmo de ordenação
        if sort_choice == 1:
            result, exec_time = measure_time(bubble_sort, arr)
        elif sort_choice == 2:
            result, exec_time = measure_time(quick_sort, arr)
        elif sort_choice == 3:
            result, exec_time = measure_time(selection_sort, arr)
        
        print(f"\nLista ordenada: {result[:10]}...")  # Exibe os primeiros 10 elementos
        print(f"Tempo de execução: {exec_time:.6f} segundos.")
    
    # Comparar o tempo de execução dos algoritmos
    print("\nComparando algoritmos de busca e ordenação:")
    
    # Lista para comparação
    arr_for_comparison = [random.randint(1, 1000) for _ in range(1000)]
    
    search_algorithms = [binary_search, linear_search, interpolation_search]
    sort_algorithms = [bubble_sort, quick_sort, selection_sort]
    
    # Comparando tempo de execução de algoritmos de busca
    search_times = []
    for algo in search_algorithms:
        _, exec_time = measure_time(algo, arr_for_comparison, 500)  # Testa com o número 500
        search_times.append(exec_time)
    
    # Comparando tempo de execução de algoritmos de ordenação
    sort_times = []
    for algo in sort_algorithms:
        _, exec_time = measure_time(algo, arr_for_comparison)
        sort_times.append(exec_time)
    
    # Exibindo os resultados comparativos
    algorithms = ["Busca Binária", "Busca Linear", "Busca por Interpolação", "Bubble Sort", "Quick Sort", "Selection Sort"]
    times = search_times + sort_times
    
    # Criando o gráfico de comparação
    plt.bar(algorithms, times, color=['blue', 'green', 'red', 'purple', 'orange', 'brown'])
    plt.xlabel('Algoritmos')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação de Algoritmos de Busca e Ordenação')
    plt.xticks(rotation=45)
    plt.show()

# Chamar a função principal para rodar o programa
run_program()
