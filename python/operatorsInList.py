# COMPARISION OPERATOR:
l1 = [1,2,3]
l2 = [3,2,1]
l3 = [1,2,3,4,5]
l4 = [1,2,3]

l1 == l2 # FALSE ---> element or unka sequence same hona zaroori
        # l1 ka first elem l2 k first se compare agr same to 2nd phr 3rd and so on
l1 == l3 # FALSE
        # no.of elements + same elements + same sequence
l1 == l4 # TRUE

l1>l3 # ---> false

l3> l1 # ---> true


# CONCATINATION     
l = l1+l2
print(l)

#repitition operator
new_list = [1,5,9]
new_list1 = 3*new_list
print(new_list1)

#SLICING OPERATOR:
list1 = [10,20,30,40,50,60]
#listObj = [beg:end:step]
print(list1[0:6:2])
print(list1)
print("---------------------")
main_list = [11,60,97,77,68,81,83,35,103,134,682]
print(main_list[1:9:1])
print(main_list[1:9:])
print(main_list[1:9])#this and above are same
print(main_list[:9])# first : k bas end value hoti (first = 0 or step =1 ko default lega)
print(main_list[:]) # complete defualt
print(main_list[::]) # same as above
    #beg ko extreme beg(left) or end ko extreme right (end) 
print(main_list[::-1]) # reverse print
    #ab beg ko extreme right end and end ko extreme beg lega

