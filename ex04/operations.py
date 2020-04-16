import sys

def showError(err = "", inperr = 0):
    if inperr:
        print ("InputError: ", err,"\n")
    print ("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")

def operations(n1, n2):
    plus = n1 + n2
    minus = n1 - n2
    product = n1 + n2

    if n1 == 0 or n2 == 0:
        quocient = "ERROR (div by zero)"
        remainder = "ERROR (modulo by zero)"
    else:
        quocient = n1 / n2
        remainder =  n1 % n2

    print ("Sum:", plus,"\nDifference:", minus, "\nProduct:", product,"\nQuocient:", quocient,"\nRemainder:", remainder)

if len(sys.argv):
    args = len(sys.argv)
    if args > 3:
        showError("too many arguments", 1)
    elif args < 3:
        showError()
    else:
        if str(sys.argv[1]).isnumeric() and str(sys.argv[2]).isnumeric():
            operations(int(sys.argv[1]), int(sys.argv[2]))
        else:
            showError("only numbers", 1)

    
