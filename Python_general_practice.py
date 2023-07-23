import sys
import datetime
from math import pi
import calendar
from dateutil import relativedelta

#Write a Python program to find out what version of Python you are using. 
print(sys.version)
#Write a Python program to display the current date and time.
print(datetime.datetime.now().strftime("%H:%M:%S - %d/%h/%Y"))
#Write a Python program that calculates the area of a circle based on the radius entered by the user. 
print(format(pi*(int(input('Enter Radius: '))^2),'.2f'))
#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. 
lst = [3,5,7,9]
new_lst = [str(i) for i in lst]
new_tpl = tuple(lst)
print(new_lst,'\n',new_tpl)
#Write a Python program that accepts a filename from the user and prints the extension of the file. 
filename = input('Input File name: ')
extension = filename.split('.')
print(extension[-1:])
#Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])
#Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
print(" %i / %i / %i"%exam_st_date)

print(calendar.month(int(input('Enter Year: ')), int(input('Enter Month: '))))
print(calendar.calendar(1999))

start_date = datetime.date(1997,5,15)
end_date = datetime.date(2023,6,30)
diff = end_date-start_date
print(diff.days)
d1 = '15/5/1997'
d2 = '30/6/2023'
start_date = datetime.datetime.strptime(d1, "%d/%m/%Y")
end_date = datetime.datetime.strptime(d2, "%d/%m/%Y")
diff = relativedelta.relativedelta(end_date,start_date)
print(diff.year,diff.month,diff.day)

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
n = int(input('Enter a number: '))
sum_ = 0
for i in range(n+1):
    sum_ += (i**i)
print(sum_)

#Test whether a number is within 100 of 1000 or 2000
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))

#Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
def triples(a,b,c):
    if a==b==c:
        return a*3
    return a+b+c
print(triples(2,4,5))
print(triples(11,11,11))

#Get a new string from a given string where 'Is' has been added to the front. If the given string already begins with 'Is' then return the string unchanged
condition = ['is','Is','IS']
def add_is(my_str):
    if my_str[:2] not in condition:
        return 'Is '+my_str
    return my_str
print(add_is('this morning?'))
print(add_is('Is this evening?'))
print(add_is('is this bottle?'))

#Get a string which is n (non-negative integer) copies of a given string
def repeater(text, n):
    return text*n
print(repeater('hello ',3))
print(repeater('Hi ',10))

#Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user. 
def odd_eve(number):
    if number%2==0:
        return "{} is Even".format(number)
    return '{} is Odd'.format(number)
print(odd_eve(22))
print(odd_eve(23))

#Count the number of occurrences in a list
def counter(my_list, n):
    count = 0
    for i in my_list:
        if i == n:
            count +=1
    return '{} repeated {} times'.format(n,count)
print(counter([1, 4, 6, 7, 4],4))
print(counter([5, 3, 9, 5, 7, 5],5))

#Write a Python program to test whether a passed letter is a vowel or not. 
vowel = 'aeiou'
def vowel_finder(x):
    return x in vowel
print(vowel_finder('a'))
print(vowel_finder('b'))

#Write a Python program to create a histogram from a given list of integers. 
def hist_plot(my_list):
    print('-'*(max(my_list)+10))
    for i in my_list:
        print('|'*i,i)
    print('-'*(max(my_list)+10))
hist_plot([20,15,18,9,6,17,4,19])

#Concatenate all elements in a list into a string
def concatenate(my_list):
    string = ''
    for i in my_list:
        string +=str(i)
    return string
concatenate([1, 5, 12, 2])
concatenate(['Hello', 'World', 'Good', 'Morning'])

#Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.  Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67,
  104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
even_list = []
def even_nums(my_list):
    for i in my_list:
        if i<237:
            if i%2==0:
                even_list.append(i)
    return even_list
print(even_nums(numbers))

#Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2. 
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
def color(color_1,color_2):
     print(color_1.difference(color_2))
     print(color_2.difference(color_1))
     print(color_1.symmetric_difference(color_2))
color(color_list_1,color_list_2)

#Write a Python program that will accept the base and height of a triangle and compute its area.
def area_of_triangle(height, base):
    return "Triagle's Area is: {}".format(((height*base)/2))

print(area_of_triangle(int(input('Enter Height of the Triangle: ')),int(input('Enter Base of the Triangle: '))))

#Write a Python program that computes the greatest common divisor (GCD) of two positive integers. 
from math import gcd
def math_gcd(a,b):
    return gcd(a,b)
print(math_gcd(12,17))
print(math_gcd(12,48))
def find_gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if (a>b):
        return find_gcd(a-b,b)
    return find_gcd(a,b-a)
print(print(find_gcd(12,48)))
print(print(find_gcd(13,17)))
print(print(find_gcd(335,480)))

#Write a Python program to find the least common multiple (LCM) of two positive integers. 
from math import lcm
def math_lcm(a,b):
    return lcm(a,b)
print(math_lcm(12,17))
print(math_lcm(12,48))
def find_lcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    while 1:
        if (greater % a==0) and (greater % b==0):
            return greater
        greater +=1
print(find_lcm(12,17))
print(find_lcm(12,48))

#Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero. 
def critical_addition(a,b,c):
    if a==b or b==c or c==a:
        return 0
    else:
        return a+b+c
print(critical_addition(2,4,5))
print(critical_addition(2,4,2))

#Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20. 
def thresh_sum(a,b):
    sum_ = a+b
    if sum_>=15 and sum_<=20:
        sum_ =  20
    return sum_
print(thresh_sum(5,18))
print(thresh_sum(8,8))
print(thresh_sum(5,8))

#Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5. 
def find_five(a,b):
    if (a==b) or (a+b==5) or (a-b==0):
        return True
    return False
print(find_five(2,5))
print(find_five(2,3))

#Write a Python program to add two objects if both objects are integers. 
def add_numerics(a,b):
    if not((isinstance(a,int)) and isinstance(b, int)):
        return 'Error input integer not found to do Addition'
    return a+b
print(add_numerics(2,5))
print(add_numerics(2,'5'))

#Write a Python program to solve (x + y) * (x + y)
def equation(a,b):
    return ((a+b)**2)
print(equation(4,3))
print(equation(8,7))

#Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years. 
def compound_interet(p,i,t):
    return (p*((1+(0.01*i))**t))
print(compound_interet(10000,3.5,7))

#Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2). 
from math import sqrt
def distance_calc(x1,y1,x2,y2):
    return sqrt(((x2-x1)**2)+((y2-y1)**2))
print('Distance between two points is: {:.3f} units.'.format(distance_calc(2,4,6,8)))

#Write a Python program to check whether a file exists. 
import os
def find_file(f_name):
    return os.path.isfile(f_name)
print(find_file('Hero_part.py'))
print(find_file('main.py'))

#Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. 
import platform 
print(platform.architecture())

#Write a Python program to get OS name, platform and release information. 
import os, platform
print(os.name)
print(platform.system())
print(platform.release())

#Write a Python program to locate Python site packages.
import site
print(site.getsitepackages())

#Write a Python program that calls an external command. 
from subprocess import call
call('cmd')

#Get the path and name of the file that is currently executing
import os
print(os.path.realpath(__file__))

#Write a Python program to find out the number of CPUs used.
import multiprocessing
print(multiprocessing.cpu_count())

#Write a Python program to parse a string to float or integer. 
x = 2.453531
print('Float:',float(x), '\nInteger:',int(x))

#Write a Python program to list all files in a directory.
import os
files_list = os.listdir(r'C:\\Users\\HP\\Pictures')
for i in files_list:
    if ('.' not in i):
        print(i)

#Write a Python program to print without a newline or space
for i in range(10):
    print('a',end="")

#Write a Python program to determine the profiling of Python programs.
#Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module
import cProfile
def loop():
    for i in range(1,2000):
        if i==1999:
            print(i)
cProfile.run('loop()')

#Write a Python program to access environment variables
import os
print(os.environ['PATH'])

#Write a Python program to get the current username.
import getpass
print(getpass.getuser())

#Write a Python program to find local IP addresses using Python's stdlib. 
import os
print(os.system('ipconfig'))
import socket
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))

#Write a Python program to get the height and width of the console window
import os
print(os.get_terminal_size())

#Write a Python program to get the execution time of a Python method. 
import time
def time_calc():
    s_time = time.time()
    sum_ = 0
    for i in range(1,100):
        sum_ +=i
    e_time = time.time()
    print('Sum is:', sum_)
    return e_time-s_time
print(time_calc())

#Write a Python program to sum the first n positive integers. 
def sum_series(x):
    return (x*(x+1))/2
print(sum_series(10))

#Write a Python program to convert height (in feet and inches) to centimeters.
def to_cm(height, unit):
    if unit == 'ft':
        print('Height is {}cm'.format(30.48*height))
    elif unit == 'i':
        print('Height is {}cm'.format(2.54*height))
    else:
        print('Wrong input!')
print("Enter the height with unit as ft or i eg: 10 and 'ft' or 'i'")
to_cm(float(input('Enter hegiht: ')),input('Enter Unit: '))

#Write a Python program to calculate the hypotenuse of a right angled triangle. 
from math import sqrt
def len_hypo(ab,bc):
    return sqrt(ab**2+bc**2)
print(round(len_hypo(4,12),3),'Units')

#Convert all units of time into seconds
def any_to_sec(t,u):
    if u == 'm':
        return t*60
    if u == 'hr':
        return t*(60**2)
    if u == 'd':
        return t*((60**2)*24)
print(any_to_sec(30,'m'))
print(any_to_sec(12,'hr'))
print(any_to_sec(2,'d'))

#Write a Python program to get an absolute file path.
import os
def get_abs_path(file):
    return os.path.abspath(file)
print(get_abs_path('Hero_parts.py'))

#Get file creation and modification date/times
import os, time
print(time.ctime(os.path.getmtime('Hero_part.py')))
print(time.ctime(os.path.getctime("Hero_part.py")))
print(time.strftime('%A-%b-%d  %H:%M:%S %p',time.localtime()))

#Write a Python program that converts seconds into days, hours, minutes, and seconds.
def sec_multi(sec_):
    min_ = round(sec_/60,4)
    hrs = round(sec_/(60**2),4)
    days = round(sec_/((60**2)*24),4)
    return min_,hrs,days
mylst = list(sec_multi(int(input('Enter the number of seconds: '))))
print('For the given seconds Minutes is {}, Hours is {} and days is {}'.format(mylst[0],mylst[1],mylst[2]))

#Write a Python program to calculate the body mass index.
def bmi(h, w):
    h  = h/100
    return round(w/(h**2),3)
print("Your BMI is:",bmi(float(input('Enter your Height in Cm: ')),float(input('Enter Your wegiht in Kg: '))))

#Write a Python program to calculate sum of digits of a number.
number = 274
d1 = number//100
d2 = (number - d1*100)//10
d3 = number - d1*100 - d2*10 
print(d1+d2+d3)

#Write a Python program to sort three integers without using conditional statements and loops.
my_list = [4,8,2]
my_list = [23,65,12]
sorted_list = [min(my_list), sum(my_list) - (min(my_list) + max(my_list)), max(my_list)]
print(sorted_list)
sorted_list.clear

#Write a Python program to get the details of the math module.
import math
print(dir(math))

#Write a Python program to calculate the midpoints of a line.
def midpoint(x1,y1,x2,y2):
    mid = ((x1+x2)/2) + ((y1+y2)/2)
    return mid
print(midpoint(2,4,8,16))

#Write a Python program to hash a word.
integer = 132
floats = 32.312
string = 'hello'
print('Hash of int is', hash(integer))
print('Hash of float is', hash(floats))
print('Hash of string is', hash(string))

#Write a Python program to get the copyright information and write Copyright information in Python code.
print(copyright)
__author__ = 'Mullaivendhan'
__copyright__ = 'Mullai DIY Projects'
__license__ = 'Public Domine'
__version__ = '1.2'

#Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. 
import sys 
print(len((sys.argv)))
print(sys.argv[0])

# Write a Python program to test whether the system is a big-endian platform or a little-endian platform. 
import sys
if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    print("Big-endian platform.")

#Write a Python program to find the available built-in modules. 
import sys
print(sys.builtin_module_names)

#Get the size of an object in bytes
import sys
x = 54
print(sys.getsizeof(x),'Bytes')

#Write a Python program to get the current value of the recursion limit. 
import sys
print(sys.getrecursionlimit())

#Write a Python program to concatenate N strings. 
n_string = ['Red', 'Green', 'Blue']
print('Joint string is: '+'-'.join(n_string))

#Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary). 
lists = [10,20,30]
dicts = {'a': 100, 'b':200, 'c':300, 'd':120}
tuples = {7, 4, 9, 1, 3, 2}
sets = (7, 4, 9, 1, 3, 2)

print('Sum of the list {} is: {}'.format(lists,sum(lists)))
print('Sum of the dictionary  {} is: {}'.format(dicts,sum(dicts.values())))
print('Sum of the tuples {} is: {}'.format(tuples,sum(tuples)))
print('Sum of the set {} is: {}'.format(sets,sum(sets)))

#Write a Python program to test whether all numbers in a list are greater than a certain number. 
num = [2, 3, 4, 5]
print(all(i>1 for i in num))

#Write a Python program to count the number of occurrences of a specific character in a string. 
my_str = input('Enter a String: ')
print("Number of '{}' in the given string is: {}".format(x:=input('Enter the letter you want to count: '),my_str.count(x)))

#Write a Python program to check whether a file path is a file or a directory. 
import os
def finder(filename):
    if os.path.isdir(filename):
        return (filename+' is a Folder')
    elif os.path.isfile(filename):
        return (filename+' is a File')
    else:
        return 'It may be a special file'
print(finder('Python_general_practice.py'))

#Write a Python program to get the ASCII value of a character. 
print("ASCII of '{}' is {}".format(char :=input('Enter a Charater: '), ord(char)))

#Write a Python program to get the size of a file. 
import os
print('Size of the file is: {} Bytes'.format(os.path.getsize('Python_general_practice.py')))

#Given variables x=30 and y=20, write a Python program to print "30+20=50". 
x = 30
y = 20
print('%d+%d=%d'%(x,y,x+y))

#Write a Python program to perform an action if a condition is true.
#Given a variable name, if the value is 1, display the string "First day of a Month!" 
#and do nothing if the value is not equal.
i = 1
if i == 1:
    print('First day of a Month!')

#Write a Python program to create a copy of its own source code. 
import os
def get_code(file_path):
    open('trial.py','w')
    with open(file_path) as f:
        with open('trial.py','w') as t:
            t.write(f.read())
    f.close()
    t.close()

get_code('Python_general_practice.py')

#Write a Python program to swap two variables. 
a = 30
b = 20
print('Before swapping: a={}, b={}'.format(a,b))
a,b=b,a
print('After swapping: a={}, b={}'.format(a,b))

#Write a Python program to define a string containing special characters in various forms.
print(" !@#$%^&*()<>?{}|~"'"'" ")

#Write a Python program to get the Identity, Type, and Value of an object. 
a = 5
print("Identity: ",a)
print("Type: ",type(a))
print("Value: ",id(a))

#Write a Python program to convert the bytes in a given string to a list of integers. 
a = 'hello'
print(list(ord(i)for i in a))
a = b'hello'
print(list(a))

#Write a Python program to check whether a string is numeric. 
a = '123'
print(a.isdigit())

#Write a Python program to print the current call stack. 
import traceback
print(traceback.print_stack())

#Write a Python program to get system time.
#Note : The system time is important for debugging, network information, random number seeds, or something as 
#simple as program performance.
import time
print(time.ctime())

# Write a Python program to clear the screen or terminal. 
import os
os.system('cls')

#Write a Python program to get the name of the host on which the routine is running.
import socket
print('Host Name:',socket.gethostname())
print('Host IP:',socket.gethostbyname(socket.gethostname()))

#Write a Python program to access and print a URL's content to the console. 
from http.client import HTTPConnection
connector = HTTPConnection('www.google.com')
connector.request('GET','/')
result = connector.getresponse()
print(result.read())

#Write a Python program to get system command output. 
import subprocess
print(subprocess.check_output('dir',shell=True,universal_newlines=True))

#Write a Python program to extract the filename from a given path. 
import os
print(os.path.basename(r'D:\Practive Programs and Files\Python_general_practice.py'))

# Write a Python program to get the users environment. 
import os
print(os.environ)

# Write a Python program to divide a path by the extension separator. 
import os 
print(os.path.splitext('Python_general_practice.py'))

# Write a Python program to retrieve file properties. 
import os, time
print('Access time: ',time.ctime(os.path.getatime('Python_general_practice.py')))
print('Modified time: ',time.ctime(os.path.getmtime('Python_general_practice.py')))
print('Change time: ',time.ctime(os.path.getctime('Python_general_practice.py')))
print('File Size: ',time.ctime(os.path.getsize('Python_general_practice.py')))

#Write a Python program to find the path to a file or directory when you encounter a path name.
import os
file = 'Python_general_practice.py'
print('File        :', file)
print('Absolute    :', os.path.isabs(file))
print('Is File?    :', os.path.isfile(file))
print('Is Dir?     :', os.path.isdir(file))
print('Is Link?    :', os.path.islink(file))
print('Exists?     :', os.path.exists(file))
print('Link Exists?:', os.path.lexists(file))

#Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
my_list = [45, 55, 60, 37, 100, 105, 220]
div_by_15 = list(filter(lambda x: (x%15==0),my_list)) #'filter' Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.
print(div_by_15)

#Write a Python program to make file lists from the current directory using a wildcard.
import glob
print(glob.glob('*'))
print(glob.glob('*txt'))

#Write a Python program to remove the first item from a specified list. 
color = ["Red", "Black", "Green", "White", "Orange"]
del color[0]
print(color)

#Write a Python program that inputs a number and generates an error message if it is not a number. 
try:
    x = int(input('Enter something: '))
except ValueError:
    print('Error value not numaric')

#Write a Python program to filter positive numbers from a list. 
my_list = [34, 1, 0, -23, 12, -88]
print(list(filter(lambda x:(x>0),my_list)))

#Write a Python program to compute the product of a list of integers (without using a for loop).
from functools import reduce
nums = [10, 20, 30,]
print(reduce(lambda x,y:x*y,nums))

# Write a Python program to print Unicode characters. 
my_str = u'\u0050\u0079\u0074\u0068\u006f\u006e'
print(my_str)

#Write a Python program to prove that two string variables of the same value point to the same memory location. 
str1 = "abc"
str2 = "abc"
print("Memory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))

#Write a Python program to create a bytearray from a list. 
my_list = [10, 20, 56, 35, 17, 99]
byte_lst = bytearray(my_list)
for i in byte_lst: 
    print(i)

#Write a Python program to round a floating-point number to a specified number of decimal places. 
float_val = 23.123124
print(float_val)
print('%.2f'%float_val)
print(format(float_val,'.2f'))
print('{:.2f}'.format(float_val))
print(round(float_val,2))

#Python: Format a specified string limiting the length of a string
my_str = 'Hello World'
print(my_str)
print('%.5s'%my_str)
print('{:.7s}'.format(my_str))

#Write a Python program to determine if a variable is defined or not.
try:
    x = 1
    #x
    print('Varible defined!')
except ValueError:
    print('Variable Not defined')

#Write a Python program to empty a variable without destroying it. 
x = 200
print(type(x)()) #type() returns the type of an object, which when called produces an 'empty' new value.
print(x)

#Write a Python program to determine the largest and smallest integers, longs, and floats. 
import sys
print(sys.maxsize)
print(sys.int_info)
print(sys.float_info)

#Write a Python program to check whether multiple variables have the same value
a = 10
b = 10
c = 10
if a==b==c:
    print('Yes they are same!')

#Write a Python program to sum all counts in a collection.
import collections
my_list = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(my_list).values()))

#Write a Python program to get the actual module object for a given object.
from inspect import getmodule
from time import ctime
print(getmodule(ctime))

#Write a Python program to check whether an integer fits in 64 bits. 
a = 10
if a.bit_length()<64:
    print('Yaa its 64bit')

#Write a Python program to check whether lowercase letters exist in a string.
my_str = 'A8238i823acdeOUEI'
print(any(i.islower() for i in my_str))

#Write a Python program to add leading zeroes to a string. 
my_str = 'hello'
print(my_str := my_str.ljust(7,'0'))
my_str = 'hello'
print(my_str := my_str.rjust(8,'0'))

#Write a Python program that uses double quotes to display strings. 
my_str = 'hello world'
import json
print(json.dumps(my_str))

#Write a Python program to split a variable length string into variables.
my_list = ['a', 'b', 'c']
x, y, z = (my_list + [None] * 3)[:3]
print(x, y, z)

#Write a Python program to list the home directory without an absolute path. 
import os
print(os.path.expanduser('~'))

#Write a Python program to calculate the time runs (difference between start and current time) of a program. 
import timeit 
start_time = timeit.default_timer()
for i in range(100):
    print(i,end='')
end_time = timeit.default_timer()
print('\nTime taken: ',end_time-start_time)

#Write a Python program to input two integers on a single line.
a,b = (input('Enter two values: ').split())
print(a,b)

#Write a Python program to print a variable without spaces between values. 
# Sample value : x =30
#Expected output : Value of x is "30" 
x = 30
print('Value of x is "{}"'.format(x))

#Write a Python program to find files and skip directories in a given directory.
print(i for i in os.listdir() if os.path.isdir(i))

#Write a Python program to extract a single key-value pair from a dictionary into variables. 
dict_ = {'a':1}
(a,b), = dict_.items()
print(a,b)

#Write a Python program to convert true to 1 and false to 0.
x = True
if x==True:
    print(1)
else: 
    print(0)

#Write a Python program to validate an IP address. 
import socket
try:
    socket.inet_aton('192.168.9.29')
    print('Vaild IP')
except socket.error:
    print('Invalid IP')

#Write a Python program to convert an integer to binary that keeps leading zeros. 
a = 15
print(format(a,'08b'))
print(format(a,'05b'))

#Write a python program to convert decimal to hexadecimal.
a = 232
print(format(a,'2x'))

#Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False. 
str1 = "01010101"
str2 = "000111000111"
def finder(str_):
    str_ = str_.replace('01','')
    return len(str_)==0
print(finder(str1))
print(finder(str2))

#Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system.
import struct
print(struct.calcsize('P')*8)

#Write a Python program to test if a variable is a list, tuple, or set.
#collection = ['a', 'b', 'c', 'd']
collection = {'a', 'b', 'c', 'd'}
#collection = ('tuple', False, 3.2, 1)
if type(collection) is list:
    print('It is a list')
elif type(collection) is set:
    print('It is a set')
else:
    print('It is a tuple')

#Write a Python program to find the location of Python module sources.
import imp
print(imp.find_module('os'))
print(imp.find_module('math'))

#Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.
def div_chk(a,b):
    return True if (a%b)==0 else False

print(div_chk(int(input('Enter Dividend: ')),int(input('Enter Divisor: '))))

#Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 
#Note: Do not use built-in functions.
def finder(my_list):
    max_ = my_list[0]
    min_ = my_list[0]
    for i in my_list:
        if i<min_:
            min_ = i
        elif i>max_:
            max_=i
    return (min_,max_)
print(finder([0, 10, 15, 40, -5, 42, 17, 28, 75]))
print(min([0, 10, 15, 40, -5, 42, 17, 28, 75]),max([0, 10, 15, 40, -5, 42, 17, 28, 75]))

#Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number. 
def make_cube(n):
    sum = 0
    for i in range(1,n):
        sum+=(i**3)
    return sum
print(make_cube(10))

#Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.
def product(my_list):
    for i in my_list:
        for j in my_list:
            if i!=j:
                prod = i*j
                if prod & 1:
                    return True
    return False
print(product([1, 6, 4, 7, 8]))
print(product([2, 4, 6, 8]))

def odd_finder(my_list):
    count = 0
    for i in my_list:
        if i%2==0:
            continue
        else:
            count+=1
    if count>1:
        return True
    else:
        return False
print(odd_finder([1, 6, 4, 7, 8]))
print(odd_finder([2, 4, 6, 8]))
