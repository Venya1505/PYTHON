#1) capitalize
#capitalizes the text

txt= "hello world"
x=txt.capitalize()
print(x)

txt= "i am venya. i am 13 years old"
x=txt.capitalize()
print(x)


#2) casefold
#it is uesd to convert lower case to upper case and vice versa

txt= "HELLO INDIA"
x=txt.casefold()
print(x)

txt1= "hi WORLD"
x=txt1.casefold()
print(x)

txt2= "HI GOOD MORNING"
x=txt2.casefold()
print(x)

txt3= "HAPPY BIRTHDAY"
x=txt3.casefold()
print(x)

#3) center()
#it will create a center string
txt= "Hi Venya"
x= txt.center(75)
print(x)

txt1= "Hi Venya"
x= txt1.center(1000)
print(x)

txt2= "Happy Birthday!!"
x=txt2.center(30)
print(x)

#4) count()
#will count how many times a word has been repeated
txt= "Im in India, India has rich traditional values, India is one of the biggest exportes of spices in the world. India is the best."
x=txt.count("India")
print(x)
txt= "Hi, I am Venya. I am 13 years old. I am in eighth grade. I like to play badminton."
x=txt.count("I")
print(x)

#5) encode()
#it returns the encoded version of the string
txt= "My name is Venya and I stay in Singapore"
x= txt.encode()
print (x)  #b'My name is Venya and I stay in Singapore'

#6) endswith()
txt= "My name is Venya and I stay in Singapore"
x= txt.endswith ("Singapore")
print (x) #True

x= txt.endswith ("Hydrabad")
print (x) #False

#7) expandtabs()
txt= "H\te\tl\tl\to"
x =txt.expandtabs(7)
print(x)  #H      e      l      l      o

#8) find()
txt= "Hello, welcome to SG"
x= txt.find("w")
print (x) #7

txt= "Hello, welcome to SG"
x= txt.find("n")#-1
print (x)


#9) format()
txt= "My name is {name}, working in {company}".format(name="Venya", company="Facebook")
print(txt) #My name is Venya working in Facebook
txt= "My name is {0}, working in {1}".format("Venya","Facebook")
print(txt) #My name is Venya working in Facebook
txt= "My name is {}, working in {}".format("Venya","Facebook")
print(txt) #My name is Venya working in Facebook

#11) index()
#The index method() finds the first occurence of the specified value
#The index method() method raises exception if value is not found
#The index() is almost similar to find() method
#Tindex if value is not found it returns exception
#find() if value is not found it returs -1
#syntax   string.index(value,start,end)
#value -required
#start,end- optional

txt= "Hello World"
x= txt.index("e")
print(x)

#12) isalnum() #al-alphabetical abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
               #num-numrical 0123456789
               #is- for checking the condition

txt= "google555"
x= txt.isalnum()
print(x) #true

txt= "google"
x= txt.isalnum()
print(x) #true

txt= "839"
x= txt.isalnum()
print(x) #true

txt= "@#$%"
x= txt.isalnum()
print(x) #false

#13) isalpha() #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

txt= "qwert"
x= txt.isalpha()
print(x) #true

txt= "qwert123"
x= txt.isalpha()
print(x) #false

#15) isdecimal()
     #if all the characters in the strings are decimals (0-9)

txt= "123"
x= txt.isdecimal()
print(x) #true

txt= "qwerty123"
x= txt.isdecimal()
print(x) #false

txt= "!@#$%^&*"
x= txt.isdecimal()
print(x)#false

#16) isdigit()
#The is isdigit() method returns True if all the characters are digits

txt= "123"
x= txt.isdigit()
print(x) #true

txt= "!@#$%^&*"
x= txt.isdigit()
print(x)#false

txt= "qwerty123"
x= txt.isdigit()
print(x) #false

#17) isidentifier()
#methods return true if the strings are valid indentifier otherwise false
#A string is considered a valid indetifier if it only contains alphanumeric letter (a-z) and (0-9) and underscores
#A valid indentifier cannot start with underscores and and any spaces

txt= "singapore"
x= txt.isidentifier()
print(x)#true

#18) islower() The islower() method returns true if all the characters are in lowercase otherwise false
#It is applicable for only alphabetical characters, not numbers, symbols and spaces.
#syntax string.islower()

txt= "HELLO WORLD"
print(txt.islower())
#false

txt= "Hello world"
print(txt.islower())
#false

txt= "hello world"
print(txt.islower())
#true

txt= "Hello world 1234"
print(txt.islower())

#19) isnumeric() this method returns true if all the characters are numeric
#for example exponents like square, 3/4, -1, 1.5 are not considered as numerical values as the characters in the string
#syntax string.isnumeric()

txt= "123456"
print(txt.isnumeric())
#true

txt= "3/4"
print(txt.isnumeric())
#false

txt= "1a2b3c4d5e6f"
print(txt.isnumeric())
#false

txt= "qwerty"
print(txt.isnumeric())
#false

#20) isprintable() The isprintable() method returns true if all the characters are printable otherwise it returns false
#syntax string.isprintable()

txt= "hello world"
x= txt.isprintable()
print(x) #true

#21) isspace() This method returns rtue if all the characters in string are whitespaces otherwise false
#syntax string.isspace()

txt= " "
x= txt.isspace()
print(x) #true

txt= "helloworld"
x= txt.isspace()
print(x)#false

txt= "V E N Y A"
x= txt.isspace()
print(x)#false

#22) istitle() The istitle() method returns true is all words in a text start with a upper case letter and then all lower case
#syntax string.istitle()

txt="HELLO WORLD"
x= txt.istitle()
print(x) #false

txt="Hello World"
x= txt.istitle()
print(x) #true

txt="Hello world"
x= txt.istitle()
print(x) #false

txt="Hello WoRld"
x= txt.istitle()
print(x) #false

#23) isupper() The isupper() method returns true if all the characters in the string are in upper case otherwise it will return false
#Numbers symbols and spaces are not ochecked only alphabetical characters are checked
#syntax string.isupper()

txt= "Hello World"
print(txt.isupper())
#false

txt= "HELLO WORLD"
print(txt.isupper())
#true

txt= "hello world"
print(txt.isupper())
#false

#24) join() The join method takes all the items in an iterable and joins them into one string
#A string must be specified as the sperator
#syntax string.join(literable)

txt= "HI VENYA"
x= "--*--".join(txt)
print(x)

txt= "HI VENYA"
x= "__*".join(txt)
print(x)

#25) lower() The lower method returns a string where all characters are lowercase
#symbols and numbers are ignored
#syntax string.lower()

txt= "HELLO WORLD"
x= txt.lower()
print(x)
#hello world

txt= "HeLlO woRlD"
x= txt.lower()
print(x)
#hello world

#26) lsstrip()
#strip will remove the white spaces from the right and left side
#lstrip will remove the white spaces from the left side
#rstrip will remove the white spaces from the right side
#syntax string.lstrip(characters)

txt= "    singapore    "
x= txt.strip()
print(x) #singapore

txt= "    singapore    "
x= txt.lstrip()
print(x) #singapore   

txt= "    singapore    "
x= txt.rstrip()
print(x)#     singapore

#27)parition()


#The partition() method searches for a specified string and splits into a tuple containing three elements


#syntaxstring.partition(value)



txt = "I could eat apples all day"



x = txt.partition("apples")


print(x)



txt = "Hi! my name is Venya working in a facebook since two years"



x = txt.partition("Venya")


print(x)

#28) rfind()
#The rfind() method rfind the last occurence of the specified value
#The rfind() methods returns -1 if value is not found
#The rfind methods is alnost the same as the rindex()








