x = float(input("Give your CGPA (Must be within 0 to 4.3)"))
while x > 4.3 or x < 0:
    x = float(input("Give your CGPA (Must be within 0 to 4.3)"))
if 0 <= x < 1:
    print("F")
elif x == 4.3:
    print("A+")
elif x < 4.3 and x >= 4:
    print("A")
elif x < 4 and x >= 3.7:
    print("A-")
elif x < 3.7 and x >= 3.3:
    print("B+")
elif x < 3.3 and x >= 3:
    print("B")
elif x < 3 and x >= 2.7:
    print("B-")
elif x < 2.7 and x >= 2.3:
    print("C+") 
elif x < 2.3 and x >= 2:
    print("C")   
elif x < 2 and x >= 1.7:
    print("C-")   
elif x < 1.7 and x >= 1.3:
    print("D+")     
elif x < 1.3 and x >= 1:
    print("D")     