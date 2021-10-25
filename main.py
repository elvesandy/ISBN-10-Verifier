
def getInput():
    '''
    input: void
    output: tuple (str, str)
    '''
    Y = input("Please enter ISBN-10: ")
    Y = Y.replace("-", "")
    location = input("Please enter the location of suspected error: ")
    return Y, location


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
    Y, error_digit = getInput()
    # print(Y, error_digit)
    Sy = Syndrome(Y)
    print("Syndrome of Y = ", Sy)
    if Sy == 0:
        print("This is a valid ISBN-10")
    else:
        t = 0
        if error_digit == 'X': t = 10
        else: t = int(error_digit)
        x = 0
        if Y[t-1] == 'X': x = 10
        else: x = int(Y[t-1])
        Sy2 = Sy - t*x
        for i in range(11):
            if (Sy2 + i*t)%11 == 0:
                output = str(i)
                if i == 10: output = 'X'
                print("The correct digit is ", i)
                break
            if i == '10':
                print("Error cannot be corrected.")
    return

if __name__ == "__main__":
    main()