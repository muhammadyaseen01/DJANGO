""" 
SYNTAX:
while <condition>
    block 
    of
    code
else:
    code

"""
# Normal Method using while
i = 1
while i<=3:
    a = int(input("enter the number"))
    if a%2 == 0:
        break
    i+=1
if i == 4:
    print("You lost the game")
else: 
    print("You won the game")

j = 1
while j<=3:
    a = int(input("enter the number"))
    if a%2 ==0:
        print ("you won the game!")
        break
    j+=1
else:
    print ("You lost the game!")