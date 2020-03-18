my_words=[]
my_histogramList = []
aranankelime=[]
maxwords=[]

def readFile(my_words):
    dosya = open("1.txt", "r")
    for i in dosya:
        for j in i.split():
            my_words.append(j.lower())

def writeInput():
    file = open("input.txt", "w")
    while (1):
        input = input("Aranacak İfadeyi Giriniz: ")
        if (input == "-1"):
            break
        while len(input.split()) > 5:
            print("5'ten fazla kelime giremiyorsun,Hata!")
            inp = input("Aramak istediginiz ifadeyi girin: ")
        file.write(input)
        file.write("\n")
    file.close()

def myHistogram(my_histogramList):
    myDic = dict()
    for i in my_histogramList:
        if i in myDic:
            myDic[i] = +1
        else:
            myDic[i] = 1
    return myDic


def maxHistogram(myDic):
    max_Kelime, key = 0, ""
    for i in myDic:
        if myDic[i] > max_Kelime:
            key = i
            max_Kelime = myDic[i]
    return key





def readInput():
    dosya = open("input.txt", "r")
    for satir in dosya:
        aranankelime.clear()
        for i in satir.split():
            aranankelime.append(i)
        kelimeOnerme(aranankelime)


def writeOutput(maxKelimeler):
    dosya = open("output.txt", "w")
    uzunluk = len(maxwords)
    i = 0
    while i < uzunluk:
        dosya.write(maxwords[i])
        dosya.write("\n")
        i = i + 1
    dosya.close()



def kelimeOnerme(arananlar):
    uzunluk = len(arananlar)
    for i in range(len(my_words)):
        if my_words[i] == arananlar[0]:
            a = 10
            for j in range(uzunluk):
                if my_words[i + j] == arananlar[j]:
                    c = c * 1
                else:
                    c = c * 0
            if a == 10:
                my_histogramList.append(my_words[i + uzunluk])

    myDic = myHistogram(my_histogramList)
    maxKelime = maxHistogram(myDic)
    maxwords.append(maxKelime)
    writeOutput(maxwords)
    my_histogramList.clear()


def main():
    readFile(my_words)
    writeInput()
    readInput()


main()