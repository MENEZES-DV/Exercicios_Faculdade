# Os algoritmos de ordenação foram uilizados com objetivo de análisar, comparar e compreender o funcionamento e sua eficiência prática

#****************************************#
# Quicksort (ordenação em forma crescente)
import time

melhor_caso_quick = [1,10,13,14,20,37]
caso_medio_quick = [29,10,14,37,13,1]
pior_caso_quick = [37,29,14,13,10,1]

l = 0
r = 5

def trocar_elementos(array, a, b):
    aux = array[a]
    array[a] = array[b]
    array[b] = aux

def partition(array, l, r):

    # Seleciona l como pivo
    pivo = array[l]
    j = l
    print(f"\nIndice [{l}] ao [{r}] / pivo = {pivo}")
    
    for i in range(l+1, r+1):
        if array[i] <= array[l]:
            j = j + 1
            trocar_elementos(array, i, j)

    trocar_elementos(array, l, j)
    print(f"Pivo {pivo} colocado na posição [{j}]")
    print(f"Array após partition: {array} \n")
    return j #retorna j como pivo

def quick_sort(array, l, r):
    
    if l < r:
        pivo = partition(array, l, r)
        quick_sort(array, l, pivo-1)
        quick_sort(array, pivo +1, r)

#***************************************#
# Mergesort (ordena de forma decrescente)

melhor_caso_merge = [37,29,14,13,10,1]
caso_medio_merge = [29,10,14,37,13,1]
pior_caso_merge = [1,10,13,14,29,37]

# l representa o primeiro indice do vetor e r representa o ultimo indice do vetor
l = 0
r = 5
meio_vetor = None

def mergesort(array ,l ,r):

    if l<r:
        meio_vetor = l + (r - l) // 2
        print(f"Divisão: {array[l:r+1]} \n")
        mergesort(array, l , meio_vetor)
        mergesort(array, meio_vetor + 1, r )
        merge(array, l, meio_vetor, r)

def merge(array, l, meio_vetor, r):

    #i = j = k = None
    n1 = meio_vetor - l + 1
    n2 = r - meio_vetor

    # Separa o vetor em duas metades
    esquerda = [None] * n1
    direita = [None] * n2

    for i in range(0, n1):
        esquerda[i] = array[l + i]

    for j in range(0, n2):
        direita[j] = array[meio_vetor + 1 + j]

    i = j = 0 
    k = l
    print(f"Merge para ordenação: {esquerda} + {direita} \n")

    while i < n1 and j < n2:

        # Condicional para verificar o maior valor para ordenação, garante que a ordenação seja feita de forma decrescente
        if esquerda[i] >= direita[j]:
            array[k] = esquerda[i]
            i += 1 
        
        else: 
            array[k] = direita[j]
            j += 1
        k += 1 

    while i < n1:
        array[k] = esquerda[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = direita[j]
        j += 1
        k +=1

def main():
    #Quick_Sort
    print ("***APLICAÇÃO DO QUICK_SORT PARA ORDENAÇÃO CRESCENTE***\n")
    print("***ORDENANDO MELHOR CASO [1,10,13,14,20,37]***\n ")
    quick_sort(melhor_caso_quick, l ,r)
    print(f"MELHOR CASO ORDENADO DE FORMA CRESCENTE: {melhor_caso_quick} \n\n")
    time.sleep(8)

    print("----------------------------------------- \n\n ***ORDENANDO CASO MÉDIO [29,10,14,37,13,1]*** \n")
    quick_sort(caso_medio_quick, l ,r)
    print(f"CASO MÉDIO ORDENADO DE FORMA CRESCENTE: {caso_medio_quick} \n\n")
    time.sleep(8)

    print("\n ----------------------------------------- \n\n ***ORDENANDO PIOR CASO [37,29,14,13,10,1]*** \n")
    quick_sort(pior_caso_quick, l ,r)
    print(f"PIOR CASO ORDENADO DE FORMA CRESCENTE: {pior_caso_quick} \n\n ***FIM*** \n")
    time.sleep(8)
    
    #Merge_Sort
    print ("\n ***APLICAÇÃO DO MERGE_SORT PARA ORDENAÇÃO DECRESCENTE*** \n")
    print("\n ***ORDENANDO MELHOR CASO [37,29,14,13,10,1]*** \n")
    mergesort(melhor_caso_merge, l ,r)
    print(f"MELHOR CASO ORDENADO DE FORMA DECRESCENTE: {melhor_caso_merge} \n")
    time.sleep(8)

    print("----------------------------------------- \n\n ***ORDENANDO CASO MÉDIO [29,10,14,37,13,1]*** \n")
    mergesort(caso_medio_merge, l ,r)
    print(f"CASO MÉDIO ORDENADO DE FORMA DECRESCENTE: {caso_medio_merge} \n")
    time.sleep(8)

    print("\n ----------------------------------------- \n\n ***ORDENANDO PIOR CASO [1,10,13,14,29,37]*** \n")
    mergesort(pior_caso_merge, l ,r)
    print(f"PIOR CASO ORDENADO DE FORMA DECRESCENTE: {pior_caso_merge} \n\n ***FIM*** \n")
    time.sleep(8)
    
main()