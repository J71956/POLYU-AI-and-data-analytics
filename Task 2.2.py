x= int(input("Enter a no"))
y= int(input("Enter a no"))
z = int(input("Enter a no"))

list = [x, y, z]
list.sort

if list[0] == list[1]:
    print(list[0], list[1])
elif list[0] == [-1]:
    print("All equal")
elif list[0] != list[1]:
    print(list[0])

if x > y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
elif x == y and x > z:
    print(x, y)

elif z > y > x:
    print(z)