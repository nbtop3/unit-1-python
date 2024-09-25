"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
pie = ["cherry","apple","sweat potato pie"]
for x in pie:  #using for loop
    print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
letters = ["a","b","c"] #list for using loop
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
n = "I just want to sleep" #sentence for loop
print(len(n)) #
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""
dictionary = {
    "name": "noid",
    "age":"4",
    "School":"star" ,
    "gender":"male",
}
for key, value in dictionary.items():
    print(f"{key}: {value}")
    
""""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#used dictionary to store date