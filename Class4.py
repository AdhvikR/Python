'''
n1=int(input("Enter First No: "))
n2=int(input("Enter Second No: "))
n3=int(input("Enter Third No:"))
res1=n1>n2 and n1>n3
res2=n1<n2 and n1>n3
res3=n1!=n2 or n1==n3
print("Result 1:", res1)#
print("Result 2:", res2)#
print("Result 3:", res3)#
'''
str1=input("Enter any String: ")
str2=input("What do you want to search?")
res1=str2 in str1

print("The result is: ", res1)
