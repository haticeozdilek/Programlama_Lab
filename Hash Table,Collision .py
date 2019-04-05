import random
#TABLOYU OLUŞTUR İÇERİĞİNE 0 ATA
def createMyHashTable(N):
    #ASSERT n SHOULD BE PRİME
    myTable=[]
    for i in range(N):
        myTable.append(0)
    return myTable
myTable = createMyHashTable(23)
print(createMyHashTable(23))

def my_hash(size,numberToBeInserted):
    return numberToBeInserted%size

def insertMyHashTable(myTable,numberToBeInserted):#Hash tablosuna bu sayıyı ekle
    isCollision=False
    index=my_hash(len(myTable),numberToBeInserted)
    if(myTable[index]==1):
        isCollision=True
    else:
        myTable[index]=1
        #myTable[index]=numberToBeInserted
    return isCollision
insertMyHashTable(myTable,100)
print(myTable)

m_h_1=createMyHashTable(30)
print((insertMyHashTable(m_h_1,17),insertMyHashTable(m_h_1,30)))
print((insertMyHashTable(m_h_1,20)))

#TABLOYU DOLAŞIP KAÇ KEZ COLLISION OLDUĞUNU BULUYOR
def myTest(size=13,numberOfInsert=10):#10 DEFA BU TABLOYA YAZ
    m_h_1=createMyHashTable(size)
    c=0#kaç defa collision oldu
    for s in range(numberOfInsert):
        #number=random.choice([0,1,2,3,4,5,6,7,8,9])
        number=random.randint(0,10000)
        if(insertMyHashTable(m_h_1,number)==True):
           c=c+1
    return c
print(myTest(703,50))