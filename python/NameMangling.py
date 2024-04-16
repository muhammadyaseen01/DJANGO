# NAME-MANGLING:
# you can access hidden variable from inside the class but cannot directly from outside the class
# HOW TO MAKE HIDDEN VARIABLES:
    #write:
        # __varibleName  EG: __var1,__a,__y

# HOW TO ACCESS THESE VARIABLES:
    # to access hidden variables from outside the class 
    # write:
        # _className  before hidden variable name

# CODE:
class Test:
    x = 15
    __hiddenVar = 13
    def __init__(self):
        self.__a = 18
    
print(Test._Test__hiddenVar)
obj=Test()
print(obj._Test__a)