#day 1 coding 

#know how to print
print("hello world")
print(1+2) #printing addition
print(1-2) #printing subtraction
print(1*2) #print multiplication
print(1/2) #print devision
print(1**2) #printing exponentional which translates to 1^2
print(1%2) #printing modulus 
print (1//2) #floor devision, when 1 devided by 2 it is 0.5 which is rounded to the lower number, in this case it is 0

#checking data types
print(type(10)) #integer 
print(type(1.2)) #float
print(type(1+2j)) #complex
print(type("amrutha")) #String
print(type([1,2,3,4])) #list
print(type({'name':"amrutha"})) #dictionary 
print(type({1,2,3,4})) #set/tuple

#used in getting help
help()
help(str)

###
#Exercises: Level 1

#Declare a first name variable and assign a value to it
first_name = 'amrutha'
print(first_name)

#Declare a last name variable and assign a value to it
last_name = 'bhandarkar'
print(last_name)

#Declare a full name variable and assign a value to it
Full_name = first_name + ' ' + last_name
print(Full_name)

#Declare a country variable and assign a value to it
country = 'India'

#Declare a city variable and assign a value to it
city='Bangalore'

#Declare an age variable and assign a value to it
age = 25

#Declare a year variable and assign a value to it
year = 2001

#Declare a variable is_married and assign a value to it
is_married = True

#Declare a variable is_light_on and assign a value to it
is_light_on = True

#Declare multiple variable on one line
rl_no , name , rank = 3 , 'amrutha' , 4
print(rl_no)
print(name)
print(rank)

#Check the data type of all your variables using type() built-in function
type(rl_no)
type(name)

#Using the len() built-in function, find the length of your first name
len(first_name)

#Compare the length of your first name and your last name
if len(first_name) == len(last_name):
    print('both are equal')
else: 
    print( 'both are not equal')

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
num_add = num_one + num_two

#Subtract num_two from num_one and assign the value to a variable diff
num_dif = num_one - num_two

#Multiply num_two and num_one and assign the value to a variable product
num_mul = num_one * num_two

#Divide num_one by num_two and assign the value to a variable division
num_div = num_one / num_two

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
num_mod = num_one % num_two

#Calculate num_one to the power of num_two and assign the value to a variable exp
num_exp = num_one ** num_two

#Find floor division of num_one by num_two and assign the value to a variable floor_division
num_fd = num_one // num_two

#The radius of a circle is 30 meters.
rad = 30

#Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math as m
pi = m.pi
area_of_circle = pi * (rad**2)

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*pi*rad

#Take radius as user input and calculate the area.
r = int(input('radius of circle:'))
type(r)
k = pi*(r**2)
print(pi*(r**2))

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
fn , ln, con, age = input('what is your 1st name: what is your last name:  which country are you from: what is your age:').split()
print(fn)
print(ln)
print(age)
print(con)

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
##