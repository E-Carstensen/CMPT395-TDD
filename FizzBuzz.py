

def fizzbuzz(i):
    
    if not str(i).isnumeric():
        return False

    i=int(i)
    output = ""

    if i % 3 == 0:
        output = output + "Fizz"

    if i % 5 == 0:
        output = output + "Buzz"

    if len(output) == 0:
        output = str(i)

    return output


