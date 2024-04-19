"""
OPERATOR ARE FUNCTION IN PYTHON
Arithemetic Operators:
1).+ ---> add two values and (also used to concatinate the string)
2).- ---> subtract two values
3).* ---> multiply two values and (also usr to multiply the string)
    4*"abc" --> abcabcabcabc output ayega --> us string ko int times return krega
4).** ---> first number is base and second is power 2**3 (2kiPower3)
5)./ ---> TRUE DIVISION --> actual division --> return float value
6).// ---> floor division --> return float and int depend on oprends
    agr 10 ya multiple of 10 se divide to jitne zero hnge right se utne number delete krdenge or remaining number ans
    EG: 243//100 --> two 0 h to right se two digit delete ---> remaining 2 h to ans
7).% ---> modulo operator --> returns reminder
    agr kabhi kisi no ka modulo 10 se ya multiple of 10 (100 1000 10000) se lia jaye to jitne zero (0) hnge utne right se digit return
    EG: 243%10 --> one zero h to ans=3
    EG: 243 %100 --> two 0 h to 43 return
"""
# practice on shell

2+5
7
2.4+6
8.4
"asd"+"ASD"
'asdASD'
4-5
-1
4-2
2
# "asd"-"ASD" ---> not possible
2**3
8
-2**2
-4
(-2)**2
4
2**-2
0.25
-2**-2
-0.25
2**0.5
1.4142135623730951
# 2**100000 ---> to big value based on 164 lines


2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376


2**-100
7.888609052210118e-31
7/3
2.3333333333333335
5/2
2.5
5.0/2.0
2.5
15/4
3.75
15//4
3
4//15
0
243//10
24
243/10
24.3
7%3
1
10%4
2
243%10 
3

"""
RELATIONAL OPERATORS: always return true or false (true value is 1 in int and false is 0)
1).>,<,>=,<= ----> inequality operators
    it gives error (complex me or etc)
2).==,!= -----> equality operators 
    they never gives error
    complex number  me bhi error nh denge true ya false me bata denge
"""

"""
LOGICAL OPERATORS:
not ---> unary operator --> ek operand chahiye
and ---> binary operator
or ---> binary operator
POINT: agr operand bool hain to ans bhi bool
        agr operand non-bool hain to ans bhi non-bool
        1).EG: "abc" or "def" ---> isme pehle non-empty str h to true (Or k case me ek true ho tab bhi ans true hota) pehla true to dosre ko check nh krnge islie ans --->abc
        2).EG: "abc" and "def" ---> isme dono true hona zarori h --> pehle true h lakin ans abhi bhi second par depend kr rha h wo true hona chahiye is liye ans second wala ANS ---> def
"""
