import re

email = input("Enter new email")
email = email.replace("@",".")
x = email.split(".")
val = True
if x[0].count(" ") >= 0:
    print("invalid password")
    val = False
if x[0].count("&") or 
