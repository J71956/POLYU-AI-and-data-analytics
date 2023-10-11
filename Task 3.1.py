import math
import random
numb = random.randint(-100, 100)
while guess != numb:
    guess = int(input("Guess a number!"))
    if (((guess - numb)/numb) * 100) <= 10:
        print("too low") 
    elif (((guess - numb)/numb) * 100) >= 10:
        print("too high") 
    elif (((guess - numb)/numb) * 100) <= 5:
        print("little low") 
    elif (((guess - numb)/numb) * 100) >= 5:
        print("little high") 
    elif abs((((guess - numb)/numb) * 100)) >= 2:
        print("very close")
    else:
        print("Bingo")
        break