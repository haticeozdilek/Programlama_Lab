import random
def generate_array(n):
    my_array=[]
    for i in range(n):
        a=random.randint(0,100)
        my_array.append(a)
    return my_array

my_array=generate_array(10)
print(my_array)

def bubble_sort(my_array):
    for i in range(len(my_array)-1,0,-1):
        for j in range(i):
            if (my_array[j]>my_array[j+1]):
                t=my_array[j]
                my_array[j]=my_array[j+1]
                my_array[j+1]=t

bubble_sort(my_array)
print (my_array)

def search(my_array,item):
    for i in range(len(my_array)):
        found = False
        if (item == my_array[i]) :
            found = True
            break
    return found

print(search(my_array,42))
