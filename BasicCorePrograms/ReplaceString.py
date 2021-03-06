import re

#1.user Input and Replace String Template “Hello <<UserName>>, How are you?”

letter = "Hello <<UserName>>, How are you?"
name = (input("Enter username\n"))
if not re.match("^[a-zA-z]*$", name):
    print("Error! only letters a-z allowed")
else:

    if (len(name) >= 3):
        letter = letter.replace("<<UserName>>", name)
        print(letter)
    else:
        print("the given username less than 3")
