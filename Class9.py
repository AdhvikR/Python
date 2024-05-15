#for loop

'''
var="Hello"
for ch in var:
    print(ch)
'''
#'ch' is a reserved term.


#for gap between
'''
var="Hello"
for ch in var:
    print(ch, end=" ")
'''

#similarly,
'''
var="Hello"
for ch in var:
    print(ch, end="+")
'''
#
'''
var="Hello"
n=len(var) # -->This should return 5
for i in range(n):
    print(i)  #--> should return (0,1,2,3,4)
'''


#for loop using range()
'''
var="Hello"
n=len(var) #length of var
for i in range(n):
    print(i)
    print(var[i]) #var[0]=H, var[1]=e, var[2]=l, var[3]=l, var[4]=o
#The above program gives you both og val and index val
'''


#for intended result to be in format 0=H
'''                                  #1=e...
var="Hello"
n=len(var) #length of var
for i in range(n):
    print(i,"=>",var[i])
'''


#Display all odd numbers between 1 and 10
'''
var="Hello"
for i in range(1,10):       #-->Have to give both start and end val of sequence
    if i%2!=0:
        print(i)
'''

#Display all even numbers between 1 and ten
'''
var="Hello"
for i in range(1,10):       #-->Have to give both start and end val of sequence
    if i%2==0:
        print(i)
'''

#Display all numbers that are divisible by 3 and 5 between 10 and 100
'''
for i in range(10,100):
    if (i%3==0 and i%5==0):
        print(i)
'''

#Display numbers in descending order between 1 and 10
for i in range(10,0,-1):       #-->hint: negative index
    print(i)
