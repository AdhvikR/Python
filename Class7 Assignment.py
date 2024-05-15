
#Check if numbers are equal
'''
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1==n2:
    print("Your two numbers are equal")
else:
    print("Your two numbers are not equal")
'''
#Check given number is even or odd.
'''
a=int(input("Enter any number: "))
if(a%2==0):
    print(a, "is even")
else:
    print(a, "is odd")
'''
#Finding the greatest number among three numbers:
'''
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print(num1, "is the greatest")
elif num2>num1 and num2>num3:
    print(num2, "is the greatest")
else:
    print(num3, "is the greatest")
'''
#Calculate the avg mark of a student
'''
sub1=int(input("Enter first mark: "))
sub2=int(input("Enter second mark: "))
sub3=int(input("Enter third mark: "))
sub4=int(input("Enter fourth mark: "))
sub5=int(input("Enter fifth mark: "))

avg= (sub1+sub2+sub3+sub4+sub5)/5
print("the avg mark is: ", avg)
if avg>40:
    print("Congrats, you passed")
else:
    print("Sorry, you failed because your score was below 40")
'''
#check if given number is divisible 3 but not 5
'''
num1=int(input("Enter any number: "))
if (num1%3==0 and num1%5!=0):
    print(num1, "is divisible by 3 bit not 5")
else:
    print(num1, "condition does not match")
'''
#vowel or consonant
'''
char=input("enter any character: ")
if (char=="a" or char=="e" or char=="i" or char=="o" or char=="u"):
    print(char, "is vowel")
else:
    print(char, "is not a vowel")
'''
# number of digits in a number
'''
n1=int(input("Enter any number: "))
if (n1>=0 and n1<=9):
    print("This is a 1 digit number")
elif (n1>=10 and n1<=99):
    print("This is a 2 digit number")
else:
    print("This is a 3 or more digit number")
'''
#HOMEWORK BELOW:------------------------------------------------
#Checking if strings are equal. HW
'''
s1=input("Enter any string: ")
s2=input("Enter the second string: ")
if (s1==s2):
    print("The 2 strings are equal")
else:
    print("The 2 strings are not equal")
'''
#Check if a given number is zero, positive, or negative. HW
'''
n1=int(input("Enter any number: "))
if (n1>=1):
    print("This number is positive.")
elif (n1==0):
    print("The number is zero.")
else:
    print("The number is negative.")
'''
#Test if a given number is in between one and ten. HW
n1=int(input("Enter any number: "))
if (n1>=1 and n1<=10):
    print("This number is between 1 and 10")
else:
    print("This number is not between 1 and 10")
#Program to test the given year is a leap year or not. HW
'''
year=int(input("Enter a year: "))
if (year%4==0):
    print("This is a leap year")
else:
    print("This is not a leap year")
'''
