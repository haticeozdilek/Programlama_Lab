def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

import random
def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    return numWins/numTrials


# for i in range(1,36):
#     print("deneme{} xd {}".format(i,checkPascal(i)))
a=checkPascal(10000)
print(a)


class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0, 0, 0 #dpLosses means don't pass Losses
    def playHand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break
    def passResults(self):
        return (self.passWins, self.passLosses)
    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)


c=CrapsGame()
for i in range(100000):
    c.playHand()
print(c.passResults())
print(c.dpResults())