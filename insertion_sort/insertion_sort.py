# Algoritmo de Ordenação por Inserção.
def list_orderer(array: list) -> list:
    '''
    Função de ordenação de array de inteiros.
    :param: Recebe um array(list object) contendo inteiros não ordenados.
    :type sentences: list.
    :rtype: list
    :return: "Retorna um array(list object) ordenado".
    '''
    for element in range(1, len(array)):
        key = array[element]
        i = element - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array

if __name__ == '__main__':
    object_array = input("Informe um array(lista) a ser ordenada. A lista deve ser de Inteiros: ").split(",")
    array = []
    array = list(map(lambda x: int(x.strip()), object_array))
    ordered_array = list_orderer(array)
    print(ordered_array)
