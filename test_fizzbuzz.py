
from FizzBuzz import fizzbuzz


def whenGivenMultipleOfThree_shouldOutputFizz():
    assert fizzbuzz(3) == "Fizz"

def whenGivenMultipleOfThree_shouldOutputBuzz():
    assert fizzbuzz(5) == "Buzz"

def whenGivenMultipleOfThreeAndFize_shouldOutputFizzBuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def whenGivenNonMultipleOfThreeOrFive_shouldOutputNumber():
    assert fizzbuzz(1) == "1"

