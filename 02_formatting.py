"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
correct_password = "utpoia"
password = input("type password")
if correct_password == password:  #using if else statements
    print("continue")
else:
    print("incorrect")



"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
string = input("enter a string")

if string == "":   #using more if else statements.
    print("invalid")

else:
    print("valid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
name = "Kr Smith"

new_name = name.replace("K","J") #replacing name
print(new_name)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
age = 14
sentence = "Nehemiah is" + age #printed sentence 
print(sentence)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
