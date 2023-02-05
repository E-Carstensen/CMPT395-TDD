
from FizzBuzz import fizzbuzz
import pytest

#Test for multiples of 3
def test_whenGivenMultipleOfThree_shouldOutputFizz():
    assert fizzbuzz(3) == "Fizz"

#Test for multiples of 5
def test_whenGivenMultipleOfThree_shouldOutputBuzz():
    assert fizzbuzz(5) == "Buzz"

#Test for multiples of both 3 and 5
def test_whenGivenMultipleOfThreeAndFize_shouldOutputFizzBuzz():
    assert fizzbuzz(15) == "FizzBuzz"

#Test for neither multiple or 3 or 5
def test_whenGivenNonMultipleOfThreeOrFive_shouldOutputNumber():
    assert fizzbuzz(1) == "1"

#Test for invalid input type, string
def test_whenGivenNonInteger_shouldReturnFalse():
    assert fizzbuzz("a") == False

#Test for valid input given as string
def test_whenGivenString_shouldConvertToIntIfNumeric():
    assert fizzbuzz("15") == "FizzBuzz"

#Test for invalid input type, list
def test_whenGivenIncorrectDataType_shouldReturnFalse():
    assert fizzbuzz(["Lists should return False", 3, 15]) == False


