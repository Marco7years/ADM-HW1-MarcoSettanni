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

# Nested List

n = int(raw_input())
lst = []
for x in range(0, n):
    lst.append([raw_input(), float(raw_input())])
lst = sorted(lst, key=lambda x: x[1]);
for x in range(1, n):
    if(lst[x][1] != lst[x-1][1]):
        score = lst[x][1]
        break
lst = sorted(lst);
for x in range(n):
    if(lst[x][1] == score):
        print lst[x][0]

# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

marks = student_marks.get(query_name)
avg = 0
for i in marks:
    avg+=i

print("{:.2f}".format(avg/len(marks)))

# Lists

test =int(input())
s=[]
for _ in range (test):
    cmd=list(input().split())
    
    if cmd[0]=='insert':
        s.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="remove":
        s.remove(int(cmd[1]))
    elif cmd[0]=="append":
        s.append(int(cmd[1]))
    elif cmd[0]=="sort":
        s.sort()
    elif cmd[0]=="pop":
        s.pop()
    elif cmd[0]=="reverse":
        s.reverse()
    elif cmd[0]=="count":
        v=s.count(int(cmd[1]))
        print(v)
    elif cmd[0]=="index":
        x=s.index(int(cmd[1]))
        print(x)
   
    elif cmd[0]== 'print':
        print(s)
    
# tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

tp = tuple(integer_list)
print(hash(tp))

# sWAP cASE

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':

# String Split and Join

def split_and_join(line):
    # write your code here
    lst = line.split(" ")
    return "-".join(lst)

if __name__ == '__main__':

# What's Your Name

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first, last))

if __name__ == '__main__':

# Mutations

def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    new_string = "".join(lst)
    return new_string

if __name__ == '__main__':

# Find a string

def count_substring(string, sub_string):
    occ = 0
    for i in range(0, len(string)-2):
        if string[i:i+len(sub_string)] == sub_string:
            occ+=1
    return occ

if __name__ == '__main__':

# String Validators

str = input()
arr = [False]*5

for letter in str:
	if letter.isalnum():
		arr[0] = True
	if letter.isalpha():
		arr[1] = True
	if letter.isdigit():
		arr[2] = True
	if letter.islower():
		arr[3] = True
	if letter.isupper():
		arr[4] = True       

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

# Text Alignment (Solution provided)

thickness = int(input()) #This must me an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Capitalize!

n = input().split(' ')
for i in n:
    print(i.capitalize(),end = " ")

# Exceptions

lines = int(input())
for _ in range(lines):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)

# Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max = 0
    for i in candles:
        if i > max:
            max = i

    total = 0
    for i in candles:
        if i == max:
            total+=1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    
    if((x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1)):
        return "NO"
    
    if(x1 < x2):
        while((x1-x2) < 0):
            x1+=v1
            x2+=v2
            if(x1 == x2):
                return "YES"
        return "NO"
    
    if(x2 < x1):
        while((x2-x1) < 0):
            x1+=v1
            x2+=v2
            if(x1 == x2):
                return "YES"
        return "NO"
    if(x1 == x2):
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for i in range(1,n+1):
        liked = shared//2
        cumulative+=liked
        shared = liked*3
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def digsum(x):
    return str(sum((int(i) for i in list(x))))

def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit( digsum(x) )
    
def superDigit(n, k):
    a = digsum(n)
    return sup_digit(str(int(a)*k))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# Introduction to sets

def average(array):
    total = 0
    set_value = set(array)
    for i in set_value:
        total+=i
    return round(total/len(set_value), 3)

if __name__ == '__main__':

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
first_inp = input()
m = input()
second_inp = input()

first_set = set(first_inp.split())
second_set = set(second_inp.split())

final_set = {}
first_inter = set(first_set.difference(second_set))
second_inter = set(second_set.difference(first_set))
final_set =  set(first_inter.union(second_inter))

lst = list(final_set)
lst.sort()

for i in lst:
    print(i)

# Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = set()
for i in range(n):
    country = input()
    countries.add(country)

print(len(countries))

# Set .union()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(input().split(" "))

m = int(input())
french = set(input().split(" "))

total = len(french.union(english))
print(total)
