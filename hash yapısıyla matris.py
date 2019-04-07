# 3x2'lik matrisi hash yapısını kullanarak oluşturuyoruz
#Matrisin tüm elemanları -1

def my_function_1(m: int, n: int):
    my_list = []

    for i in range(m):
        my_list.append([])
        for j in range(n):
            my_list[i].append(-1)
    return my_list


def my_function_convert_to_hash(myList):#Matrisi hash'e dönüştürüyor
    my_dict = {}
    m = len(myList)
    n = len(myList[0])
    for i in range(m):
        for j in range(n):
            my_dict[(i, j)] = myList[i][j]
    return my_dict


def my_function_print_hash(myHashList):#son olarak hash fonksiyonu yazdırılıyor
    print(" ")
    for key in myHashList:
        print(myHashList[key], end=" ")


new_array = my_function_1(3, 2)
new_dict = my_function_convert_to_hash(new_array)
my_function_print_hash(new_dict)