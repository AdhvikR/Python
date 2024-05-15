# input your first name then the last name. Display the full name.
'''
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
full_name=first_name+" "+last_name
print("Hello", full_name)
'''


#Write a program to calculate your age. Take inputs(birth year) from user.
'''
birth_year=int(input("Enter your birth year: "))
current_year=int(input("Enter the current year: "))
age=current_year-birth_year
print("Hello, your age is: ",age)
'''


#Write a program to calculate birth year. Take age from user. HW
'''
age=int(input("Enter your Age: "))
current_year=int(input("Enter the current year: "))
birth_year=current_year-age
print("Hello, your birth year is ", birth_year)
'''


#Hidden Password.
'''
password=input("Please enter your password: ")
password_length=len(password)
hidden_password="*"*password_length
print("Your password is, ",hidden_password)
'''


#Take 2 strings from user using input. Concatenate (+/add) 3rd index value of both strings. HW
'''
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
str3=str1[3]+str2[3]
print("The Third index of both strings added together results in: ", str3)
'''


#Swap 2 numbers without using any conditions (ex: if/else/etc.)
n1=int(input("Enter the first value to be swapped: "))
n2=int(input("Enter the second value to be swapped: "))
n1=n3
n2=n1
n3=n2
print("Before swapping, the values are: ", n2, ", ", n1)
print("After swapping, the values are: ", n1, ", ", n2)


'''
suppose:
n1=10
n2=20
this should become
n1=20
n2=10
display
before swapping: [take 2 #'s]
after swapping: [swapped 2 #'s]
USING 3RD VAR
'''
