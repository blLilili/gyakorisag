import random

def isitPerfect():
    pass

def randomGen(s, e, a):
    numbers = list()
    for i in range(a):
        numbers.append(random.randint(s, e))
    return numbers

def makeNum(text):
    #isitPerfect = False
    while True:    #not isitPerfect:
        n = input(text)
        try:
            n = int(n)
            #isitPerfect = True
            return
        except ValueError:
            print("Helytelen érték")


startMessage = "Kezdő érték: "
endMessage = "Végérték: "
amountMessage = "Értékek száma: "


start = makeNum(startMessage)
end = makeNum(endMessage)
amount = makeNum(amountMessage)

randomGen(start, end, amount)
