import math
import random
numb = random.randint(-100, 100)
print(numb)
guess = int(input("Guess a number!"))
print((((guess - numb)/numb) * 100))