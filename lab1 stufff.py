import math
print("Shiloh Siu")
print("Shiloh Siu \n")
print("Shiloh \n Siu\n")
myvar = input("enter ur name")

option = int(input("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division"))
if option == 1:
    var1 = int(input("1st no"))
    var2 = int(input("2nd no"))
    var3 = var1 + var2
    print(var3)
elif option == 2:
    var1 = int(input("1st no"))
    var2 = int(input("2nd no"))
    var3 = var1 - var2
    print(var3)
elif option == 3:
    var1 = int(input("1st no"))
    var2 = int(input("2nd no"))
    var3 = var1 * var2
    print(var3)
elif option == 4:
    var1 = int(input("1st no"))
    var2 = int(input("2nd no"))
    var3 = var1 / var2
    print(var3)
else:
    print("not a valid input")