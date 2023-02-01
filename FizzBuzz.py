




def fizzbuzz(i):

    output = ""

    if i % 3 == 0:
        output = output + "Fizz"

    if i % 5 == 0:
        output = output + "Buzz"

    if len(output) == 0:
        output = output + str(i)

    return output


def whenGivenMultipleOfThree_shouldOutputFizz():
    assert fizzbuzz(3) == "Fizz"

def whenGivenMultipleOfThree_shouldOutputBuzz():
    assert fizzbuzz(5) == "Buzz"

def whenGivenMultipleOfThreeAndFize_shouldOutputFizzBuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def whenGivenNonMultipleOfThreeOrFive_shouldOutputNumber():
    assert fizzbuzz(1) == "1"
