# Say "Hello, World!" With Python
if __name__ == '__main__':
    print "Hello, World!"

# Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())

if n%2!=0:
    print("Weird")
elif n<=5 and n>=2:
    print("Not Weird")
elif n<=20 and n>=6:
    print("Weird")
elif n>20 and n%2==0:
    print("Not Weird")

# Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)

# Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)

# Loops

if __name__ == '__main__':
    n = int(input())

numbers = [x for x in range(n) if x<=n]
for i in numbers:
    print(i**2)

# Write a function

def is_leap(year):
    if year%4==00:
        if year%400==0 or year%100!=0:
            return True
    else:
        return False

year = int(input())
print(is_leap(year))

# Print Function
if __name__ == '__main__':
    n = int(input())

numbers = [x for x in range(1, n+1)]
print_word = ""

for i in numbers:
    print_word += (str(i))

print(print_word)

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list_x = [i for i in range(x+1)]
list_y = [i for i in range(y+1)]
list_z = [i for i in range(z+1)]
    
print([[x,y,z] for x in list_x for y in list_y for z in list_z if (x+y+z)!=n])

# Find the Runner-Up Score!
'''Yes, it's not the best solution but it's nearly midnight and I have to work tomorrow'''
if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))

arr.reverse()
position = [x for x in arr if x!=arr[0]]
print(position[0])

