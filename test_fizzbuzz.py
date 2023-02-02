
from FizzBuzz import fizzbuzz
import pytest

def test_whenGivenMultipleOfThree_shouldOutputFizz():
    assert fizzbuzz(3) == "Fizz"

def test_whenGivenMultipleOfThree_shouldOutputBuzz():
    assert fizzbuzz(5) == "Buzz"

def test_whenGivenMultipleOfThreeAndFize_shouldOutputFizzBuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_whenGivenNonMultipleOfThreeOrFive_shouldOutputNumber():
    assert fizzbuzz(1) == "1"

def test_whenGivenNonInteger_shouldReturnFalse():
    assert fizzbuzz("a") == False

def test_whenGivenString_shouldConvertToIntIfNumeric():
    assert fizzbuzz("15") == "FizzBuzz"

def test_whenGivenIncorrectDataType_shouldReturnFalse():
    assert fizzbuzz([3, 5, 15]) == False


