''' Eric Carstensen - 3070801
Takes an integer or a string numeric
returns "Fizz" if input is divisable by 3
        "Buzz" if input is divisable by 5
        "FizzBuzz" if input is divisable by both 3 and 5
        string input if divisable by neither
        False if invalid input
'''

def fizzbuzz(i):
    #Check for invalid input
    if not str(i).isnumeric():
        return False

    #Enforce type
    i=int(i)
    output = ""

    if i % 3 == 0:
        output = output + "Fizz"

    if i % 5 == 0:
        output = output + "Buzz"

    if len(output) == 0:
        output = str(i)

    return output


