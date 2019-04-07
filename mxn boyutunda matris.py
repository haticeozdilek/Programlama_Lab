#mxn boyutlarında bütün elemanları -1 olan bir liste

def my_function_1(m:int ,n:int):
    my_list = []

    for i in range(m):
        my_list.append([])
        for j in range(n):
            my_list[i].append(-1)

    return my_list

def my_function_print(myList):
    m = len(myList)
    n = len(myList[0])
    for i in range(m):
        for j in range(n):
            print(myList[i][j],end=" ")
        print()
new_array = my_function_1(3,4)
my_function_print(new_array)