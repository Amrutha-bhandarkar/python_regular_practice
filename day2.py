# day 2 coding

#Declare your age as integer variable
age = 25

#Declare your height as a float variable
hght = 165

#Declare a variable that store a complex number
com = 1+4j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = int(input('enter base: '))
h = int(input('enter height: '))
a = 0.5 * b*h
print('area of triangle is ',a )

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input('enter side a: '))
b = int(input('enter side b: '))
c = int(input('enter side c: '))
p = a+b+c
print('the perimeter of triangle is ', p)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
l = int(input('length:'))
b = int(input('width:'))
a = l*b
p = 2 * (l+b)
print('area of rectangle is ', a)
print('perimeter of rectangle is ', p)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r=int(input('radius:'))
import math as m
a = m.pi * (r**2)
c = 2*m.pi*r
print('area of circle is ', a)
print("circumference of circle is", c)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x=int(input('enter the slope:'))
y=(2*x) - 2
print('slope value is' , y)


#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1=2
x2=6
y1=2
y2=10
m= (y2-y1)/(x2-x1)
print("the slope is: ", m)

#Compare the slopes in tasks 8 and 9.
if (y==m):
    print('Task 8 and Task 9 slopes are equal')
else: 
    print('Task 8 and Task 9 slopes are not equal')

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-5,5): 
   y = (x**2) + (6*x)+9
   print('for x =', x, 'y = x^2 + 6x + 9 is ', y)
   if y==0:
       print('Found 0! stopping')
       break

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
x=len('python')
y=len('dragon')
if x==y:
    print('Len of Python and Len of dragon are equal')
else: 
    print('Len of Python and Len of dragon are not equal')

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print('on is present in both dragon and python')
else: 
    print('on is not present in both dragon and python')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if 'jargon' in 'I hope this course is not full of jargon.':
    print('"Jargon" is present in "I hope this course is not full of jargon."')
else:
    print('"Jargon" is not present in "I hope this course is not full of jargon."')

#There is no 'on' in both dragon and python
if 'on' not in 'python' and 'on' not in 'dragon':
    print('There is no "on" in both dragon and python')
else:
    print('There is "on" in both dragon and python')

r= 'on' not in 'python' and 'on' not in 'dragon'
print(r)

#Find the length of the text python and convert the value to float and convert it to string
r='python'
s=len(r)
type(s)
t=float(s)
type(t)
u=str(t)
type(u)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x=int(input('check the number is even or odd; enter the number:'))
if x%2==0:
    print('Number is even')
else:
    print('Number is odd')
    
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if 7//3 == int(2.7):
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7")
else:
    print('The floor division of 7 by 3 is not equal to the int converted value of 2.7')
    
#check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("Type of '10' is equal to type of 10")
else:
    print("type of '10' is not equal to type of 10")
        
#Check if int('9.8') is equal to 10
if int(float('9.8')) == 10:
    print("int('9.8') is equal to 10")
else:
    print("int('9.8') is not equal to 10")

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
h= int(input("enter hours: "))
r=int(input("enter rate per hour: "))
print("your weekly earning is ", h*r)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
y=int(input("enter number of years you have lived: "))
print("you have lived for ", y*365*24*60*60,'seconds')

#Write a Python script that displays the following table
for n in range(1,6):
    print(n,1,n,n**2,n**3)