# Função de Bucket Sort para números inteiros em um intervalo maior
def bucket_sort_inteiros(lista, k):
    # Encontrar o valor máximo da lista para determinar a quantidade de baldes necessários
    max_val = max(lista)
    
    # Criar k baldes vazios
    baldes = [[] for _ in range(k)]
    
    # Distribuir os elementos nos baldes
    for num in lista:
        balde_idx = num * k // (max_val + 1)  # Determina o balde baseado no valor
        baldes[balde_idx].append(num)
    
    # Ordenar cada balde
    for i in range(k):
        baldes[i].sort()  # Podemos usar sort() já que o número de elementos em cada balde é pequeno
    
    # Concatenar todos os baldes em uma única lista ordenada
    resultado = []
    for balde in baldes:
        resultado.extend(balde)
    
    return resultado

# Testando o Bucket Sort com números inteiros
def testar_bucket_sort_inteiros():
    lista = [42, 32, 53, 61, 17, 28, 39, 91, 83]
    k = 10  # Número de baldes
    print("Lista original de números inteiros:", lista)
    lista_ordenada = bucket_sort_inteiros(lista, k)
    print("Lista ordenada de números inteiros:", lista_ordenada)

# Executa o teste
testar_bucket_sort_inteiros()
