#MATRİS OLUŞTURMA

satir=0
sutun=0
matris=[]

satir=int(input("Matrisin satir sayisini giriniz :"))
sutun=int(input("Matrisin sutun sayisini giriniz :"))

for i in range(satir): #KULLANICIDAN İSTEDİĞİ BOYUTTA MATRİS OLUŞTURULUYOR
    matris+=[[0]*sutun]

for i in range(satir):#KULLANICIDAN MATRİSE DEĞER ATANIYOR
    for j in range(sutun):
        sayi=int(input("%s.satir %s.sütun elemanını giriniz :" %(i+1,j+1)))
        matris[i][j] =sayi

for i in range(satir):  #matris ekrana yazdırıldı
    for j in range(sutun):
        print (matris[i][j])
    print










