#List

#1) List is represented with []
#2) Python Lists just like dynamicalled sized arrays
#3) It can store different kinds of elements ['a', 22,True, 23.4]
#4) We can also store different duplicate items [1,2,2,2,2,2,3,3,4,4,5,5,6,6]
#5) Python Lists are ordered

#creation of empty lists
li= []
print(li)

#Note by using type keyword we can check the datatype.
#creation of lists with elements

li= ['hi','welcome','good']
print(li) #['hi','welcome','good']
print (type (li)) #<class 'list'>


#creation of lists with numbers

li = [10,20,30]
print ("List of numbers", li)

#Creating a list of elements and accessing using Index

li= ['Venya' , 'Karthik' , 'Singapore' , 'Canada' , 'Malasiya']

print (li)

print(li[1])
print(li[2])

#We can access two elements at a time bu using slicing

#   [start:end:step]

print (li[2:5:])

li= ['1','2','3','4','5','6','7','8','9','10']
print (li[0:10:2]) #['1', '3', '5', '7', '9']

li= ['1','2','3','4','5','6','7','8','9','10']
print (li[1:10:2]) #['2', '4', '6', '8', '10']

li= ['1','2','3','4','5','6','7','8','9','10']
print (li[0:10:4])#['1', '5', '9']

li= ['1','2','3','4','5','6','7','8','9','10']
print (li[5:10:3]) #['6', '9']

li= ['1','2','3','4','5','6','7','8','9','10']
print (li[4:10:2]) #['5', '7', '9']

li= [['Singapore' , 'Canada'],['Venya' , 'Radika'], ['Karthik', 'Malasiya']]
print (li[1][0])
print (li[2][1])


#List Methods:

#1) append
#Adds an element at the end of the list

x= ['kumar','ravi','raju']

y= x.append ('yuvaraj')

print (x)


x= [1,2,3,4,5,6,7]

x.append ('raju123')
print (x) 


#2) clear
#Helps remove all the elements present in the list at a time


#3) copy
#It will copy all the elements into another variable

x= [1,2,3,4,5]

y= x.copy()

print("Elements present inside x are :",x)
print("Elements present inside y are :",y)


#4) count

x= ['a','b','c','d','e','a','a','a','f','a']

y= x.count ('a')

print('total number of a inside the list:' ,y)


x= ['a','b','c','d','e','a','a','a','c','a']

y= x.count ('c')

print('total number of c inside the list:' ,y)


x= ['a','b','c','d','e','a','a','a','f','a']

y= x.count ('b')

print('total number of b inside the list:' ,y)


#5) extend
#extended function will add the two lists into a single list

india- ['Hyderabad', 'Andhra Pradesh' , 'Tamil Nadu', 'Banglore']
Country - ['India', 'America','Singapore','Canada']

india.extend(country)

print (india)


#6) index
#By using index we know the index position of that  item
india- ['Hyderabad', 'Andhra Pradesh' , 'Tamil Nadu', 'Banglore']

y = india.index('Andhra Pradesh')

print("The index value for this:" ,y)

#7) insert
#By using the insert method we can add the element in the required position

india- ['Hyderabad', 'Andhra Pradesh' , 'Tamil Nadu', 'Banglore']
india.insert (0, 'Chennai')
print (india)

#8) pop
#9) remove
#10) reverse
#11) sort
