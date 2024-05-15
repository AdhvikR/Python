Python 3.10.0a3 (tags/v3.10.0a3:8bae2a9, Dec  7 2020, 20:13:25) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> range(2,9,3)
range(2, 9, 3)
>>> range(2,9)
range(2, 9)
>>> list(range(step))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(range(step))
NameError: name 'step' is not defined
>>>1 in range(10) #Checking if 1 is part of range 10
'''range(start,end,step) <-- step is 1 if not specified.'''

