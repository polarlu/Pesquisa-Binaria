def bucket_sort(notas):
    """Ordena uma lista de notas usando o algoritmo Bucket Sort."""
    # Cria os baldes (arrays) para armazenar as notas
    buckets = [[] for _ in range(10)]

    # Distribui as notas nos baldes
    for nota in notas:
        index = int(nota // 10)
        buckets[index].append(nota)

    # Ordena as notas dentro de cada balde
    for i in range(len(buckets)):
        buckets[i].sort()

    # Junta as notas ordenadas dos baldes
    sorted_notas = []
    for bucket in buckets:
        sorted_notas.extend(bucket)

    return sorted_notas

def interpolation_search(notas, target):
    """Realiza a busca por Interpolation Search para encontrar uma nota específica."""
    low = 0
    high = len(notas) - 1

    while low <= high and target >= notas[low] and target <= notas[high]:
        if low == high:
            if notas[low] == target:
                return low
            return -1

        # Calcula a posição de busca usando a fórmula de interpolação
        pos = low + ((target - notas[low]) * (high - low)) // (notas[high] - notas[low])

        # Verifica se a posição é válida
        if notas[pos] == target:
            return pos
        elif notas[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Lista de notas dos alunos
notas = [88, 92, 95, 85, 70, 100, 56, 74, 61, 82, 96]

# Ordena as notas usando Bucket Sort
notas_ordenadas = bucket_sort(notas)
print("Notas ordenadas:", notas_ordenadas)

# Procura uma nota específica usando Interpolation Search
nota_procurada = 95
indice = interpolation_search(notas_ordenadas, nota_procurada)

if indice != -1:
    print(f"A nota {nota_procurada} foi encontrada na posição {indice}.")
else:
    print(f"A nota {nota_procurada} não foi encontrada.")
