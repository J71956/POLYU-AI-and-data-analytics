message = str(input("Give a str with only a to z "))
shiftno = int(input("Give shift number"))
list = []
str = ""
for i in range(len(message)):
    if ord(message[i]) + shiftno >= 122:
        x = ord(message[i]) + shiftno -25
        list.append(chr(x))
    elif ord(message[i]) + shiftno < 122 and ord(message[i]) + shiftno >= 97:
        x = ord(message[i]) + shiftno
        list.append(chr(x))
print(list)
str = str.join(list)
print(str)

list2 = []
revstr = ""
for i in range(len(str)):
    if ord(str[i]) - shiftno < 97:
        x = ord(str[i]) - shiftno +25
        list2.append(chr(x))
    elif ord(str[i]) - shiftno >=97 :
        x = ord(str[i]) - shiftno
        list2.append(chr(x))
print(list2)
revstr = revstr.join(list2)
print(revstr)