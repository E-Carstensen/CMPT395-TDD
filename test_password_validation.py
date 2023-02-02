from password_validation import validate


def test_whenGivenLengthLessThan8_shouldReturnError():
    assert "Password must be at least 8 characters" in validate("A11!")


def test_whenGivenLessThanTwoNumbers_shouldReturnError():
    assert "The password must contain at least 2 numbers" in validate("A1!AAAAaAa")


def test_whenGivenMultipleErrors_shouldReturnAll():
    assert "Password must be at least 8 characters\nThe password must contain at least 2 numbers" in validate("A!")


def test_whenGivenNoCapitals_shouldReturnError():
    assert "password must contain at least one capital letter" in validate("a11!5678")


def test_whenGivenNeSpecialChar_shouldReturnError():
    assert "password must contain at least one special character" in validate("A1234567")