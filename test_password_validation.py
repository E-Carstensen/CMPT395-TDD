from password_validation import validate

#Test minimum length criteria
def test_whenGivenLengthLessThan8_shouldReturnErrorMessage():
    assert "Password must be at least 8 characters" in validate("A11!")

#Test 2 digit criteria
def test_whenGivenLessThanTwoNumbers_shouldReturnErrorMessage():
    assert "The password must contain at least 2 numbers" in validate("A1!AAAAaAa")

#Test Multiple errors returns multiple error messages
def test_whenGivenMultipleErrors_shouldReturnAllMessage():
    assert "Password must be at least 8 characters\nThe password must contain at least 2 numbers" in validate("A!")

#Test capital letter criteria
def test_whenGivenNoCapitals_shouldReturnErrorMessage():
    assert "password must contain at least one capital letter" in validate("a11!5678")

#Test special char criteria
def test_whenGivenNoSpecialChar_shouldReturnErrorMessage():
    assert "password must contain at least one special character" in validate("A1234567")

#Test valid password returns True
def test_whenGivenValidPassword_shouldReturnTrue():
    assert validate("A1234567!") == True