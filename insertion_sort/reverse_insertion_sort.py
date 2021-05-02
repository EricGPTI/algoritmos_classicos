'''
O desafio aqui é recriar o algorítmo de inserção ordenando
do maior para o menor.
'''
def inverse_list_orderer(array: list) -> list:
    '''
    Função de ordenação reversa de array de inteiros.
    :param: Recebe um array(list object) contendo inteiros não ordenados.
    :type sentences: list.
    :rtype: list
    :return: "Retorna um array(list object) inversamente ordenado".
    '''

    for element in range(1, len(array)):
        key = array[element]
        i = element - 1
        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array

if __name__ == '__main__':
    object_array = input("Informe um array(lista) a ser ordenada. A lista deve ser de Inteiros: ").split(",")
    array = []
    array = list(map(lambda x: int(x.strip()), object_array))
    ordered_array = inverse_list_orderer(array)
    print(ordered_array)
