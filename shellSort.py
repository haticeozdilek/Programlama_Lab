#bubble,selection,insertion
#of swap,comparison
#3,12,34,2,54 bu algoritmayı insertion ile sıralayalım
def shellShort(arr):
    n=len(arr)
    gap=n//2  #int(n/2)
    karsilastirmaSayisi=0
    yerDegistirmeSayisi=0
    while(gap>0):
        for i in range(gap,n):
            karsilastirmaSayisi+=1
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                karsilastirmaSayisi+=1
                yerDegistirmeSayisi+=1
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap//=2
    return arr,karsilastirmaSayisi,yerDegistirmeSayisi
arr=[12,34,54,2,3]
print(shellShort(arr))
