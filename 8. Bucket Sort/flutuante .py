# Função de Insertion Sort para ordenar cada balde
def insertion_sort(balde):
    for i in range(1, len(balde)):
        chave = balde[i]
        j = i - 1
        while j >= 0 and balde[j] > chave:
            balde[j + 1] = balde[j]
            j -= 1
        balde[j + 1] = chave

# Função de Bucket Sort para números flutuantes no intervalo [0, 1)
def bucket_sort_flutuantes(lista):
    n = len(lista)
    
    # Criar n baldes vazios
    baldes = [[] for _ in range(n)]
    
    # Distribuir os elementos nos baldes
    for i in range(n):
        balde_idx = int(lista[i] * n)  # Determina o balde baseado no valor
        baldes[balde_idx].append(lista[i])
    
    # Ordenar cada balde
    for i in range(n):
        insertion_sort(baldes[i])
    
    # Concatenar todos os baldes em uma única lista ordenada
    resultado = []
    for balde in baldes:
        resultado.extend(balde)
    
    return resultado

# Testando o Bucket Sort com números flutuantes
def testar_bucket_sort_flutuantes():
    lista = [0.42, 0.32, 0.53, 0.61, 0.17, 0.28, 0.39]
    print("Lista original de números flutuantes:", lista)
    lista_ordenada = bucket_sort_flutuantes(lista)
    print("Lista ordenada de números flutuantes:", lista_ordenada)

# Executa o teste
testar_bucket_sort_flutuantes()
