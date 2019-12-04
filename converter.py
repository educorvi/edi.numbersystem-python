# Author: Pascal-Daniel Paul
# Version:  1.0

#------------------------------------------------------------------------------#
# Functions

def start():
    """this function provides several options which are then executed."""

    print("""
    ---------------Wellcomme to the converter 1.0--------------
    --in which form would you like to calculate your number?---
    --------------(Option) 1. converter,----------------
    ---(Infomation) Please enter the number of the option.----""")

    option = input("> ") # waiting for input

    if option == "1":
        converter()
    else:
        print("Incorrect information")
        start()

#------------------------------------------------------------------------------#
def converthex(rest):
    """This function determines if the base is 16 and
    replaces the numbers 10 to 15 in bush letters."""

    converter ={10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    ret = converter[rest]
    return ret

#------------------------------------------------------------------------------#

def rmod(dezimal, basis):
    """in this function the following is calculated."""

    if basis not in [2, 16]:
        return "Error false Basis"

    if not isinstance(dezimal, int):
        return "Error false Dezimal"

    numberlist = [] # create a list

    start = True

    while(start): # This is the way of calculation
        result = dezimal / basis
        result = int(result)
        rest = dezimal - (result * basis)
        rest = int(rest)
        dezimal = result

        if basis == 16:
            if rest > 9:
                rest = converthex(rest)

        numberlist.append(rest)
        if result == 0:
            start = False

    numberlist.reverse() # The list is turned upside down
    return numberlist

#------------------------------------------------------------------------------#
def converter():
    """In this function, a decimal number will be converted to a dual number."""

    print("Please enter a decimal number:")

    dezimal = int(input("dezimalzahl> ")) # here you can enter a number
    basis = int(input("basis> ")) # here can you enter the Basis

    if(dezimal >= 1): # If the number is greater than zero

        zwischenergebnis = rmod(dezimal, basis)
        print(zwischenergebnis)
        result = rmod(dezimal, int(2)) # modulo calculation
        #start()
    elif dezimal == 0:
        print("0") # Print 0
        start()
    else:
        print("error in calculation") # information
        start()

#------------------------------------------------------------------------------#

start()
