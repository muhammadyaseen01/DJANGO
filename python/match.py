# it is same as switch case
"""
MATCH:
    1).cases different types k bhi hosakte hain depend krta h
    2). match and case is called soft keyword (not in the list of keyword)
        match or case ko as a variable name bhi use kr sakte is liye soft keyword bolte hain isse (not reserved keyword)
    3). duplicate cases are also allowed in python but it runs only first appearence
    4). case me conditional statement bhi use kr sakte hain
"""


"""
x = int(input("enter the number: "))
y = eval(input("enter the number: "))
match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")

match y :
    case 1.1:
        print("One")
    case True:
        print("Two")
    case 3+4j:
        print("Three")
    case [1,2,3]:
        print("Four")
    case _: # for default this _ is used
        print("invalid")

z = int(input("enter your value for z: "))
match z:
    case 97:
        print ("One")
    case 97:
        print ("Two")

print ("outside")
"""



#for type checking
cond = eval(input("enter the value for cond: "))
match cond:
    case cond if type(cond) == int:
        print("Integer")
    case cond if type(cond) == float:
        print("float")
    case cond if type(cond) == complex:
        print("Complex")
    case cond if type(cond) == bool:
        print("Boolean")
    case _:
        print("Other Type")