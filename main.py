def afiseaza_meniu():
    print(" ")
    print("1. Citire lista.")
    print("2. Afisarea partii intregi a tuturor numerelor din lista.")
    print("3. Afisarea tuturor numerelor care apartin unui interval deschis citit de la tastatura")
    print("4. Afisarea tuturor numerelor a caror parte intrega este divizor al partii fractionare")
    print("5. Afisarea listei obtinute din lista initiala in care numerele sunt inlocuite cu un string format din"
          "cuvinte care le descriu caracter cu caracter.")
    print("x. Exit")


def citeste_lista() -> list[float]:
    lst = []
    lst_str = input("Dati numerele separate prin spatiu: ")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(float(num_str))
    return lst


def parte_intreaga(lst):
    """
    Determinare partea intreaga a tuturor numerelor din lista
    :param lst: lista de float-uri
    :return: o lista care contine partea intreaga a tuturor numerelor din lista initiala
    """
    result = []
    for num in lst:
        intreg = int(num)
        result.append(intreg)
    return result


def test_parte_intreaga():
    assert parte_intreaga([2.5, 3.6, 14.256, 8.25]) == [2, 3, 14, 8]
    assert parte_intreaga([]) == []
    assert parte_intreaga([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert parte_intreaga([1, 2.3, 3.25]) == [1, 2, 3]
    assert parte_intreaga([-1, -2.3, -3.25]) == [-1, -2, -3]


def interval_deschis(lst, capat1, capat2):
    """
    Creeaza o lista cu numerele cuprinse in intervalul deschis format din capat1 si capat2
    :param lst: lista de float-uri
    :param capat1: primul capat al intervalului deschis
    :param capat2: al doilea capat al intervalului deschis
    :return: lista de numere cuprinse in intervalul deschis
    """
    result = []
    for num in lst:
        if num > capat1 and num < capat2:
            result.append(num)
    return result


def test_interval_deschis():
    assert interval_deschis([1.5, -3.3, 8, 9.8, 3.2], -4, 5) == [1.5, -3.3, 3.2]
    assert interval_deschis([3.2, -5, -2.6, 6], -3, 0) == [-2.6]
    assert interval_deschis([], -4, 5) == []
    assert interval_deschis([1, 2.2, 3.3, 4.4], 1.2, 4.4) == [2.2, 3.3]


def divizor(num):
    """
    determina divizorii unui numar
    :param num:
    :return:
    """
    result = []
    for i in range(2, int(num)//2 +1):
        if int(num) % i == 0:
            result.append(i)
    return result

def fractionar(num):
    """
    determina partea fractioanara a unui numar
    :param num: numarul caruia i se calculeaza partea fractioanara
    :return: partea fractioanra a numarului
    """
    return str(num).split('.')[1]


def test_fractionar():
    assert fractionar(1.2) == "2"
    assert fractionar(1.45) == '45'
    assert fractionar(20.652) == '652'


def intreg_este_div_pt_fract(lst):
    """
    Determina daca partea intreaga a numerelor din lista este divizor al partii fractionare a numarului
    :param lst: lista de float-uri
    :return: o lista de numere a caror parte intreaga este divizor al partii fractionare a numarului
    """
    result = []
    for num in lst:
        intreg = int(num)
        fract = fractionar(num)
        if intreg in (divizor(fract)):
            result.append(num)
    return result


def test_intreg_este_div_pt_fract():
    assert intreg_este_div_pt_fract([1.2, 3.6, 5.7, 9.18]) == [1.2, 3.6, 9.18]
    assert intreg_este_div_pt_fract([]) == []
    assert intreg_este_div_pt_fract([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert intreg_este_div_pt_fract([-1.2, -2.8, -3.5, -7.12]) == [-1.2, -2.8]


def inlocuire_lista(lst):
    """
    Inlocuieste numerele din lista cu caractere
    :param lst: lista de float-uri
    :return: lista de caractere
    """
    pass


def test_inlocuire_lista():
    assert inlocuire_lista([1.5, 2.3, 6.7]) == [unuvirgulacinci, doivirgulatrei, sasevirgulasapte]
    assert inlocuire_lista([]) == []
    assert inlocuire_lista([2.3, 6.7]) == [doivirgulatrei, sasevirgulasapte]


def main():
    lst = []

    while True:
        afiseaza_meniu()
        opt = input("Introduceti optiunea: ")
        if opt == "1":
            lst = citeste_lista()
        elif opt == "2":
            print("Partea intrega a tuturor numerelor din lista: ",
                  parte_intreaga(lst))
        elif opt == "3":
            capat1 = float(input("Introduceti primul capat al intervalului deschis: "))
            capat2 = float(input("Introduceti al doilea capat al intervalului deschis: "))
            rezultat = interval_deschis(lst, capat1, capat2)
            print("Numerele cuprinse intre " + str(capat1) + " si " + str(capat2) + " sunt: ", rezultat)
        elif opt == "4":
            print(intreg_este_div_pt_fract(lst))
        elif opt == "5":
            pass
        elif opt == "x":
            break
        else:
            print("Optiune invalida!")


if __name__ == '__main__':
    #test_intreg_este_div_pt_fract()
    #test_inlocuire_lista()
    test_fractionar()
    test_interval_deschis()
    test_parte_intreaga()
    main()
