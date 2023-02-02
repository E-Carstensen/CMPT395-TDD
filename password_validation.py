
'''
Takes a potential password as a string and validates it against these criteria:
    Must be atleast 8 Chars long
    Must contain atleast 1 capital letter
    Must contain atleast 2 numbers
    Must contain atleast 1 special character



'''

def validate(pswd):

    output = ""

    if not isinstance(pswd, str):
        return False

    if len(pswd) < 8:
        output += "Password must be at least 8 characters\n"
    
    nums = 0 
    caps = 0
    special = 0

    for char in pswd:

        if char.isnumeric():
            nums += 1

        elif char in '!@#$%^&*().,[]-=_+`~':
            special += 1

        elif char.isupper():
            caps += 1
        
    if nums < 2:
        output += "The password must contain at least 2 numbers\n"

    if caps < 1:
        output += "password must contain at least one capital letter\n"
   
    if special == 0:
        output += "password must contain at least one special character\n"

    if len(output) == 0:
        return True
    
    return output