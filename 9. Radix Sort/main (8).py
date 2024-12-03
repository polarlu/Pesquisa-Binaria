# Função de Counting Sort, que é usada como sub-rotina no Radix Sort
def counting_sort(lista, exp):
    n = len(lista)
    resultado = [0] * n  # Lista para armazenar os números ordenados
    contagem = [0] * 10  # Contagem de dígitos (base 10)
    
    # Contar a frequência de cada dígito
    for i in range(n):
        index = (lista[i] // exp) % 10
        contagem[index] += 1
    
    # Calcular a posição de cada dígito
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]
    
    # Construir o resultado ordenado
    i = n - 1
    while i >= 0:
        index = (lista[i] // exp) % 10
        resultado[contagem[index] - 1] = lista[i]
        contagem[index] -= 1
        i -= 1
    
    # Copiar o resultado de volta para a lista original
    for i in range(n):
        lista[i] = resultado[i]

# Função de Radix Sort
def radix_sort(lista):
    # Encontrar o maior número para saber até quantos dígitos precisamos ordenar
    max_num = max(lista)
    
    # Aplicar o Counting Sort para cada dígito (de exp = 1 para a unidade até exp = maior potência de 10)
    exp = 1
    while max_num // exp > 0:
        counting_sort(lista, exp)
        exp *= 10

# Testando o Radix Sort com números de diferentes tamanhos
def testar_radix_sort():
    lista_2_digitos = [34, 23, 12, 45, 98]
    lista_5_digitos = [52347, 12345, 98765, 23456, 54321]
    lista_10_digitos = [9876543210, 1234567890, 2345678901, 3456789012, 4567890123]

    print("Lista original (2 dígitos):", lista_2_digitos)
    radix_sort(lista_2_digitos)
    print("Lista ordenada (2 dígitos):", lista_2_digitos)
    
    print("Lista original (5 dígitos):", lista_5_digitos)
    radix_sort(lista_5_digitos)
    print("Lista ordenada (5 dígitos):", lista_5_digitos)
    
    print("Lista original (10 dígitos):", lista_10_digitos)
    radix_sort(lista_10_digitos)
    print("Lista ordenada (10 dígitos):", lista_10_digitos)

# Executar o teste
testar_radix_sort()
