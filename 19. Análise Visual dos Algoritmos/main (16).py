import matplotlib.pyplot as plt
import numpy as np

# Função para plotar o estado atual da lista
def plot_list(arr, title):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(title)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

# Merge Sort com visualização das etapas
def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(arr, depth=0):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid], depth + 1)
        right = merge_sort_recursive(arr[mid:], depth + 1)
        merged = merge(left, right)
        plot_list(merged, f'Merge Sort Passo {depth}')
        return merged

    return merge_sort_recursive(arr)

# Quick Sort com visualização das etapas
def quick_sort(arr):
    def partition(low, high, arr):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(low, high, arr, depth=0):
        if low < high:
            pi = partition(low, high, arr)
            plot_list(arr, f'Quick Sort Passo {depth}')
            quick_sort_recursive(low, pi - 1, arr, depth + 1)
            quick_sort_recursive(pi + 1, high, arr, depth + 1)

    quick_sort_recursive(0, len(arr) - 1, arr)

# Selection Sort com visualização das etapas
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plot_list(arr, f'Selection Sort Passo {i + 1}')

# Lista de exemplo
arr = [64, 34, 25, 12, 22, 11, 90]

# Gerando gráficos para Merge Sort
print("Visualizando Merge Sort")
merge_sort(arr.copy())

# Gerando gráficos para Quick Sort
print("Visualizando Quick Sort")
quick_sort(arr.copy())

# Gerando gráficos para Selection Sort
print("Visualizando Selection Sort")
selection_sort(arr.copy())
