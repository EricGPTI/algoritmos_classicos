# Algoritmo de Ordenação por Inserção.
def insertion_sort(array: list) -> list:
    for element in range(1, len(array)):
        key = array[element]
        i = element - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array

object_array = input("Informe um array(lista) a ser ordenada. A lista deve ser de Inteiros: ").split(",")
array = []
array = list(map(lambda x: int(x.strip()), object_array))
ordered_array = insertion_sort(array)
print(ordered_array)