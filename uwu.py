def makeItNumber(n):
    try:
        n = int()
    except ValueError:
        n = None
    return n 

def repeatInput():
    start = None
while start == None:
    start = input("Kezdő érték: ")
    if makeItNumber(start):
        print(start)
    else:
        print("Helytelen érték")