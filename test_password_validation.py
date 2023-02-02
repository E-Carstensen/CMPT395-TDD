from password_validation import validate


def test_whenGivenLengthLessThan8_shouldReturnErrorMessage():
    assert "Password must be at least 8 characters" in validate("A11!")


def test_whenGivenLessThanTwoNumbers_shouldReturnErrorMessage():
    assert "The password must contain at least 2 numbers" in validate("A1!AAAAaAa")


def test_whenGivenMultipleErrors_shouldReturnAllMessage():
    assert "Password must be at least 8 characters\nThe password must contain at least 2 numbers" in validate("A!")


def test_whenGivenNoCapitals_shouldReturnErrorMessage():
    assert "password must contain at least one capital letter" in validate("a11!5678")


def test_whenGivenNoSpecialChar_shouldReturnErrorMessage():
    assert "password must contain at least one special character" in validate("A1234567")


def test_whenGivenValidPassword_shouldReturnTrue():
    assert validate("A1234567!") == True