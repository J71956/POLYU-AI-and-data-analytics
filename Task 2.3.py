import math
x,y = int(input("Give a number")), int(input("Give another number"))

calc = str(input("What  operation do you want to do?"))
if calc == "+":
    print(x+y)
elif calc == "-":
    print(x-y)
elif calc == "*":
    print(x*y)
elif calc == "/":
    print(x/y)
elif calc == "^":
    print(x**y)
elif calc == "%":
    print(x%y)