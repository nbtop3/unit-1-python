'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
n = int(input("type a number:"))
if n >= 10:
    print("true")
else:
    print("false")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age = int(input("type your age:"))
if age <= 18:
    print("pay $10")
elif age >= 18:
  print("pay $20")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruits = {"apples","grapes","mangos","oranges",}
user_input = input ("type a fruit:")
if user_input in fruits:
    print ("Yes, that fruit is in the list.")
else:
     print("No, That fruit is not in the list.")
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year= input("type a year:")
if year % 100:
    print("it's a century year")
elif year % 400:
    print("it's a leap year")
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''