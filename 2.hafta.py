def selection_sort(my_array):
    swap_sayisi=0
    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(1,i+1):
            print("location: ",location,"i: ",i,end="\n")
            if (my_array[location] > my_array[positionOfMax]):
                positionOfMax = location
        temp = my_array[location]
        my_array[location] = my_array[positionOfMax]
        my_array[positionOfMax] = temp
        swap_sayisi +=1
    return my_array,swap_sayisi




def binary_search(my_array,item):
    counter=0
    first=0
    last=len(my_array)-1
    found=False
    while(first <= last and not found):
        midpoint=(first+last)//2
        if (my_array[midpoint]==item):
            found=True
        else:
            if (item < my_array[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
        counter +=1
    return midpoint,found,counter

def fibonacci_iter(n):
    a,b=0,1
    if (n==0):
        return 0
    for i in range(n-1):
        a,b=b,a+b
    return a

def fibonacci_recursive(n):
    if (n<2):
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def factorial(n):
    s=1
    for i in range(1,n):
        s=s*i
    return s

def factorial_recursive(n):
    if (n==1):
        return 1
    else:
        return n*factorial_recursive(n-1)

def power(m,n):
    if n==0:
        return 1
    if ((n%2)==0):
        return power(m,n//2)**2
    else:
        return m*power(m,(n-1))



my_array=[21,23,13,44,25,2,7,16,14,12,11]
print(selection_sort(my_array))
print(binary_search(my_array,14))
print(factorial_recursive(5))
print(power(356,23))
