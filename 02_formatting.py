"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
correct_password = utopia
password = input("type password")
if correct_password == password:  #using if else statements
    print("continue")
else:
    print(incorrect)



"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
string = input("enter a string")

if string == "":
    print("invalid")

else:
    print("valid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""