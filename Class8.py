#Menu based Calc

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

#Displaying info for the user
print("Enter '+' for addition \nEnter '-' for subtraction \nEnter '*' for multiplication \nEnter '/' for division")

#Taking user choice
operator=input("Please enter your choice: ")

if operator=="+":
    print("The result is: ", num1+num2)
elif operator=="-":
    print("The result is: ", num1-num2)
elif operator=="*":
    print("The result is: ", num1*num2)
elif operator=="/":
    print("The result is: ", num1/num2)
else:
    print("Invalid input, please re-run the program.")
'''

#Looping - Used to repeat similar task based on the number of times. (Finite/Infinite)

#Two types of loops: 'for loop' and 'while loop'

#range(): is an inbuilt func that generates numbers from 0 to n

#Ex: Display your name 10 times, print all numbers from 1 to ten


#Inefficient way

'''
'''
print("Adhvik")
print("Adhvik")
print("Adhvik")
print("Adhvik")
print("Adhvik")
print("Adhvik")
print("Adhvik")
print("Adhvik")
print("Adhvik")
print("Adhvik")
'''

#Inefficient way

'''
print("Adhvik\nAdhvik\nAdhvik\nAdhvik\nAdhvik\nAdhvik\nAdhvik\nAdhvik\nAdhvik\nAdhvik\n")
'''

#Efficient way


#Syntax for 'for loop'
'''
for (var) in range/sequence:            #<-- sequence can be list/string/tuple
    statement
'''
'''
for name in range(10):          #   <-- range(10) equals (0,1,2,3,4,5,6,7,8,9)
    print("Adhvik")
'''
'''
for i in range(11):
    print(i)
'''
'''
for i in range(0,11,2):         #   <--gives all even numbers 
    print(i)
'''

'''
for i in range(0,11,3):         #   <--gives all odd numbers
    print(i)
'''
