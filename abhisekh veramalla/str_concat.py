""" str1= " G anesh  "
str2= "moka" 

print (str1+" "+str2)
print(len(str1))
print( " lower case",str1.lower())
print( " upper case",str1.upper())
print( " replace",str1.replace("G", "S"))
print( " split",str1.split())
print( " strip", str1.strip()) """

""" num=int(input("enter the number: "))
if((num%2)==0):
    print("the number is even")
else:
    print("the number is odd") """

""" number=[6,3,5,8,4,2,5,4,11]
sum=0
for i in number:
    sum=sum+i
print("Sum is", sum) """

""" num=int(input("enter the number: "))
if num > 0:
    if num%2==0:
        print("the number is positive and even")
    else:
        print("the number is positive and odd")
elif num < 0:
    if num%2==0:
        print("the number is negative and even")
    else:
        print("the number is negative and odd")
else: 
    print("the number is zero")"""

  

""" rows=5
K=6
for i in range(rows,0,-1):
    K-=1
    for j in range(1,i+1):
        print(K, end='')
    print() """

""" sub=['english','hindi','science','math','kannada']
sub_drop =sub.pop(1)
print('deleted subject:', sub_drop)
print('updated subject:', sub)
 """
""" totalTemp=0
for day in range(1,8):
    temp=float(input("enter tempture for day {}: ".format(day)))
    totalTemp+= temp
avg_temp=totalTemp / 7
print("average tempture of the week:", avg_temp)
 """

# a=11
# b=10

# if (a!=b):
#     print( a,"a is lesser than b",b)
# else:
#     print (b,"is lesser than",a)

# logical operator
""" x= False
y= True

result= not y
print(result) """

# AND 
# X   Y   result 
# T   T    T
# T   F    T
# F   T    F
# F   F    F

# OR
# X   Y   result 
# T   T    T
# T   F    F
# F   T    F
# F   F    F

# identity operators
my_list=["hi","ganesh"]
your_list= my_list

compare = my_list is your_list
not_same= my_list is not your_list
element = "ganesh" in my_list
print(element)
print(compare)
print(not_same)