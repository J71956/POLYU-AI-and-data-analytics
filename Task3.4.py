miltime = str(input("Give military time "))
list = []

for x in miltime:
    list.append(int(x))
print(str(list[0]) + str(list[1]) + ":" + str(list[2]) + str(list[-1]))