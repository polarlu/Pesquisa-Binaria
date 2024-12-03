def merge_sort_strings(strings):
    """Ordena uma lista de palavras usando Merge Sort."""
    if len(strings) <= 1:
        return strings

    # Dividir a lista em duas partes
    mid = len(strings) // 2
    left = merge_sort_strings(strings[:mid])
    right = merge_sort_strings(strings[mid:])

    # Combinar as partes ordenadas
    return merge_strings(left, right)


def merge_strings(left, right):
    """Combina duas listas de palavras ordenadas."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Adiciona os elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort_strings(strings):
    """Ordena uma lista de palavras usando Quick Sort."""
    if len(strings) <= 1:
        return strings

    pivot = strings[len(strings) // 2]
    left = [word for word in strings if word < pivot]
    middle = [word for word in strings if word == pivot]
    right = [word for word in strings if word > pivot]

    return quick_sort_strings(left) + middle + quick_sort_strings(right)


def binary_search_strings(strings, target):
    """Realiza Binary Search para verificar se uma palavra está na lista ordenada."""
    left, right = 0, len(strings) - 1

    while left <= right:
        mid = (left + right) // 2
        if strings[mid] == target:
            return mid
        elif strings[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Teste com lista de palavras
words = ["banana", "apple", "orange", "grape", "kiwi", "mango"]
print("Lista original:", words)

# Ordenação com Merge Sort
sorted_words_merge = merge_sort_strings(words)
print("Merge Sort:", sorted_words_merge)

# Ordenação com Quick Sort
sorted_words_quick = quick_sort_strings(words)
print("Quick Sort:", sorted_words_quick)

# Busca binária
target_word = "orange"
index = binary_search_strings(sorted_words_merge, target_word)
if index != -1:
    print(f"A palavra '{target_word}' foi encontrada na posição {index}.")
else:
    print(f"A palavra '{target_word}' não foi encontrada.")
