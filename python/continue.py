i =1
while i<=5:
    a = int(input("enter the number: "))
    if a%2==0:
        continue
    if a == 7:
        print("END")
        break
    print (i,"--> a = ",a)
    i+=1