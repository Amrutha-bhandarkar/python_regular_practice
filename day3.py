#day 3 coding

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = ['Thirty', 'Days', 'Of', 'Python']
title = ' '.join(a) 
print(title)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a,b,c = 'Coding', 'For' , 'All'
title  = a+' '+b+' '+c
print(title)

#Declare a variable named company and assign it to an initial value "Coding For All".
com = 'abc'
new_title=com + ' '+ title
print(new_title)

#Print the variable company using print().
print(com)

#Print the length of the company string using len() method and print().
print(len(com))

#Change all the characters to uppercase letters using upper() method.
com.upper()

#Change all the characters to lowercase letters using lower() method.
com.lower()

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
title.capitalize()
title.title()
title.swapcase()

#Cut(slice) out the first word of Coding For All string.
title[3:]

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
a,b,c = 'Coding', 'For' , 'All'
title  = a+' '+b+' '+c
title.find('Coding')
title.index('Coding')

#Replace the word coding in the string 'Coding For All' to Python.
nt= title.replace('Coding', 'Python')

#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
nt.replace('All', 'Everyone' )

#Split the string 'Coding For All' using space as the separator (split()) .
title.split(' ')

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
a = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
a.split(',')

#What is the character at index 0 in the string Coding For All.
title[0]

#What is the last index of the string Coding For All.
len(title)-1

#What character is at index 10 in "Coding For All" string.
title[10]

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
ac=''
for i in nt.split():
    ac+=i[0]
print(ac)

#Create an acronym or an abbreviation for the name 'Coding For All'.
ca=''
for i in title.split():
    ca+=i[0]
print(ca)

#Use index to determine the position of the first occurrence of C in Coding For All.
title.index('C')

#Use index to determine the position of the first occurrence of F in Coding For All.
title.index('F')

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
title.rfind('l')

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
test='You cannot end a sentence with because because because is a conjunction'
test.index('because')
test.find('because')

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
test.rindex('because')

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
test.split('because')

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
test.index('because')

#Does 'Coding For All' start with a substring Coding?
title.startswith('Coding')

#Does 'Coding For All' end with a substring coding?
title.endswith('Coding')

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
ntt='   Coding For All      '
ntt.strip()

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
a='30DaysOfPython'
b='thirty_days_of_python'
a.isidentifier()
b.isidentifier()

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
w = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lib=' '.join(w)
print(lib)

#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
a  = 'I am enjoying this challenge. \nI just wonder what is next. '
print(a)

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
a = 'Name\t Age\t Country\t City\nAsabeneh\t 250\t Finland\t Helsinki'
print(a)

#Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
r=10
a=3.14*r**2
stg='The area of a circle with radius %i is %i meters square.'%(r,a)
print(stg)

#Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
a=8
b=6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
