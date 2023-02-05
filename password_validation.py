
''' Eric Carstensen - 3070801 - CMPT395 TDD Password Validation
Takes a potential password as a string and validates it against these criteria:

    Must be atleast 8 Chars long
    Must contain atleast 1 capital letter
    Must contain atleast 2 numbers
    Must contain atleast 1 special character

If any of these criteria are not met it will return a string containing an error message for each missed criteria seperated by a \n
If all criteria are met it will return True
'''

def validate(pswd):

    output = ""

    #Enforce type
    if not isinstance(pswd, str):
        return False

    if len(pswd) < 8:
        output += "Password must be at least 8 characters\n"
    
    #Counters for criteria
    nums = 0 
    caps = 0
    special = 0

    for char in pswd:

        #If Char is a number
        if char.isnumeric():
            nums += 1
        #If char is a special character
        elif char in '!@#$%^&*().,[]-=_+`~':
            special += 1
        #If char is uppercase
        elif char.isupper():
            caps += 1
        
    #If counter doesn't meet criteria, append error for each missed case
    if nums < 2:
        output += "The password must contain at least 2 numbers\n"

    if caps < 1:
        output += "password must contain at least one capital letter\n"
   
    if special == 0:
        output += "password must contain at least one special character\n"

    #If no errors are appended, return True
    if len(output) == 0:
        return True
    
    #Else return errors
    return output