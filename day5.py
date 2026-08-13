# day 5

#Create an empty tuple
empty_tuple = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings= ('Mansaa','Mahima','Shreya','Ananth','Guru','Deepak','Divya','Trupti')
sisters=siblings[0:3] + siblings[-2:]
brothers=siblings[3:6]

#Join brothers and sisters tuples and assign it to siblings
sibling= brothers+sisters
print(sibling)

#How many siblings do you have?
len(sibling)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family=list(sibling)
type(family)
family.append('Prakash')
family.append('pushpa')
print(family)
family = tuple(family)
type(family)
print(family)

#Unpack siblings and parents from family_members
del family

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple','mango')
vegetables=('carrot','cabbage')
animal_product=('milk','butter')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle=len(food_stuff_lt)//2
if middle%2 == 0 :
    half_stuff=food_stuff_tp[0:middle+1]
else:
    half_stuff=food_stuff_tp[0:middle]

print(half_stuff)

#Slice out the first three items and the last three items from food_stuff_lt listf
first=food_stuff_tp[0:3]
print(first)

last=food_stuff_tp[-3:]
print(last)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
print(food_stuff_tp)

#Check if 'Estonia' is a nordic country and Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries
'Iceland' in nordic_countries
