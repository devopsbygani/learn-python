# l=[1,2,0,65,8,3]
# l.sort()
# print(l)

# #append
# l.append("hey")
# print (l)

# #extend
# l.extend([1,2,3,4,"hey"])
# print(l)

""" 
#regular expression
# it check wheater the given string is exist in the given varaible

import re
text = " hey how are you"
check = r" hey how are you"
search = re.search(check,text)
if search:
    print( "found",search.group())
else:
    print( "not found")

# exact match of string with space and case sentisitive
match = re.match(check,text)
if match:
    print( "found",match.group())
else:
    print( "not found")

# replacement

name = "hey i am ganesh"
pattern = r"ganesh"
replacement = "biti"
print(name)
edited_text= re.sub(pattern,replacement,name)
print( "i am replaced text : " ,re.sub(pattern,replacement,name))


# split the given text

fruits = "oranges/apple/grapes"
pattern=r"/"

split_fruits=re.split(pattern,fruits)
print(split_fruits)

 """

""" # string concat

text1= "iamone"
text2="   iAm    two0   "

# add two strings: concatinating
add_text=text1+" "+text2
print(add_text)
# printing the length of string
length_of_text1=len(text1)
length_of_text2=len(text2)
print(length_of_text1,length_of_text2)
# upper and lower case
uppercase = text1.upper()
lowercase = text2.lower()
print(uppercase)
print(lowercase)
# replacing the string
replace_text=text2.replace("iAm","we are")
print(replace_text)
# spliting the string to list
print(text2.split(" "))  # check the empty and split
print(text2)
# strip remove the extra spaces
print(text2.strip())
# left strip and right strip 
leftstrip = text2.lstrip()
rightstrip = text2.rstrip()
print(leftstrip)
print(rightstrip)
#note: it cannot remove the spaces inbetween
 """

#keyword
""" 
a=10
b=20
if a==20 or b==20:
    print("i am true")
else:
    print(" opps no!") """

a=int(input("enter a value: "))
b=int(input("enter b value: "))

def add():
	c = a+b
	print(add)
def sub():
	sub = a-b
	print(sub)
def multiplication():
	mul = a*b
	print(mul)
add()
sub()
multiplication()

def division ():
	div=a/b
	print ("dividion:",div)

division()
