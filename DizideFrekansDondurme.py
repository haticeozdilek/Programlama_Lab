#kendisine aktarılan bir listenin, frekans tablosunu bulup geri gönderen 
#bir fonksiyon yazınız.

liste=[2,3,2,5,8,2,4,3,3,2,8,5,2]
#sözlük şeklindeyse
def frequency(list):
    frequency_dict={}
    for item in list:
        if (item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
           frequency_dict[item] = 1
    return frequency_dict

print(frequency(liste))

#liste şeklindeyse

def frequency2(list_1):
    freq=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(freq)):
            if (list_1[i]==freq[j][0]):
                freq[j][1]=freq[j][1]+1
                s=True 
           
        if (s==False):
            freq.append([list_1[i],1])  #indis[0[1] +=1
    return freq

print(frequency2(liste))



