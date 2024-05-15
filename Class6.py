#Swapping of two variables
var1=int(input("Enter first number: "))
var2=int(input("Enter second number: "))
#Before Swapping
print("Before Swapping: ")
print("var1= ", var1, "\tvar2: ", var2)

#Swapping logic (with the help of third variable, var3)
var3=var1
var1=var2
var2=var3

#After Swapping
print("After Swapping: ")
print("var1= ", var1, "\tvar2: ", var2)
