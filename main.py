
def getInput():
    '''
    input: void
    output: tuple (str, int)
    '''
    Y = input("Please enter ISBN-10: ")
    print("Please Pick Error Detection Strategy: \n 1. getting a digit wrong \n 2. interchanging two (unequal) digits")
    type = input()
    return Y, int(type)


def Syndrome(Y):
    '''
    ipnut: str
    output: int
    Returns checksum value of code Y
    '''
    Sum = 0
    for i in range(10):
        if Y[i] == 'X':
            Sum += 10*(i+1)
        else:
            Sum += int(Y[i])*(i+1)
    return Sum % 11

def main():
    userInput = getInput()
    Y, t = userInput
    Sy = Syndrome(Y)
    print("S(y) = ", Sy)
    if Sy == 0:
        print("This is a valid ISBN-10")
    elif t == 1:
        place = 0
        print("type1 error to do")
    elif t == 2:
        k = 0
        l = 1
        for k in range(9):
            for l in range(1, 10):
                yk, yl = Y[k], Y[l]
                if yl == 'X': yl = 10
                if k != l and Sy == ((k-l)*(int(yl)-int(yk)))%11:
                    print("Error found: swap places ", k, " and ", l )
                    return
    else:
        print("Error: cannot correct error")
    return

if __name__ == "__main__":
    main()