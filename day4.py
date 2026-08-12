#day 4

#Declare an empty list
empty_list = []

#Declare a list with more than 5 items
alpha=['a','b','c','d','e']

#Find the length of your list
len(alpha)

#Get the first item, the middle item and the last item of the list
first= alpha[0]
last=alpha[-1]
middle_index=len(alpha)//2
middle=alpha[middle_index]
print(first)
print(middle)
print(last)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
my_data=['amrutha',25 ,'5ft 4in', 'single', 'banglore']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
len(it_companies)

#Print the first, middle and last company
first_it=it_companies[0]
last_it=it_companies[-1]
middle_index=len(it_companies)//2
midde_it=it_companies[middle_index]
print(first_it)
print(midde_it)
print(last_it)

#Print the list after modifying one of the companies
it_companies[3]='Adobe'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Cloudflare')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(middle_index, 'Exxon')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2]=it_companies[2].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
it_companies.extend('#;  ')
print(it_companies)

#Check if a certain company exists in the it_companies list.
'Exxon' in it_companies

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
it_companies[0:3]

#Slice out the last 3 companies from the list
it_companies[-3:]

#Slice out the middle IT company or companies from the list
it_companies[middle_index]

#Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.remove(it_companies[middle_index])
print(it_companies)

#Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end + back_end
print(full_stack)

#Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
r_index=full_stack.index('Redux')
full_stack[r_index+1:r_index+1]=['Python','SQL']
print(full_stack)

#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(ages)
minvalue=ages[0]
maxvalue=ages[-1]
print(minvalue)
print(maxvalue)

#Add the min age and the max age again to the list
ages.append(minvalue)
ages.append(maxvalue)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
middle=len(ages)//2
ages[middle]

#Find the average age (sum of all items divided by their number )
average=sum(ages)/len(ages)
print(average)

#Find the range of the ages (max minus min)
max(ages)-min(ages)

#Compare the value of (min - average) and (max - average), use abs() method
minv=min(ages)
maxv=max(ages)
minab=abs(minv-average)
maxab=abs(maxv-average)
if minab>maxab:
    print("minimum value is far from average")
else:
    print("Max value is away from average")
    
#Find the middle country(ies) in the countries list
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid=len(country)//2
if len(country)%2!=0:
    middle_country= country[mid]
else:
    middle_country= country[mid-1:mid+1]
    
print(middle_country)

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(country)%2!=0:
    first_half=country[0:mid+1]
    second_half=country[mid+1:]
else:
    first_half=country[0:mid]
    second_half=country[mid:]

print(first_half)
print(second_half)

