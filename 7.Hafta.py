class myClass(object):
    def __init__(self, myfile=""):
        f = open("text", "r")
        myContent = (f.read())
        mySentences = myContent.split(".")
        self.myWords = []

        for sentence in mySentences:
            Words = sentence.split(" ")
            for word in Words :
                self.myWords.append(word)
        self.myFrequency_1()
        self.myFrequency_2()
        self.write_frequency_1()
        self.write_frequency_2()

    def myFrequency_1(self):
        self.frequency_list_1 = {}

        for word in self.myWords:
            if (word in self.frequency_list_1):
                self.frequency_list_1[word] += 1
            else:
                self.frequency_list_1[word] = 1

    def write_frequency_1(self):
        for word_1 in self.frequency_list_1:
            print(word_1 + " " + str(self.frequency_list_1[word_1]))
    # def write_frequency_2(self):
    #     pass
    def myFrequency_2(self):
        self.frequency_list_2 = {}
        for i in range(len(self.myWords)-1):
            w_1, w_2 = self.myWords[i], self.myWords[i+1]

            if((w_1, w_2) in self.frequency_list_2):
                self.frequency_list_2[(w_1,w_2)] += 1
            else:
                self.frequency_list_2[(w_1,w_2)] =1
    def write_frequency_2(self):
        for w_1 in self.frequency_list_2:
            print(str(w_1)+" "+str(self.frequency_list_2[w_1]))

    def myFrequency_11(self, words):
        counter = self.myWords.count(words)
        print(words,"sayisi =", counter)

    def myFrequency_22(self, word_1, word_2):
        Freq = 0
        fullword = word_1 + " " + word_2
        for i in range(len(self.myWords)):
            if (self.myWords[i] == word_1 and self.myWords[i+1] == word_2):
                Freq += 1

        print(fullword, "sayisi=",Freq)


my_class = myClass()
#my_class.myFrequency_11("Ismail")
#my_class.myFrequency_22("Ismail", "Altay")