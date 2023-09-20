password = input("Type your password")
ben = len(password)
if ben>=8:
    if any(letter.islower()for letter in password):
        if any(letter.isupper()for letter in password):
            if any(letter.isnumeric()for letter in password):
                print ("Your password is valid")
else:
    print ("Your password is invalid")