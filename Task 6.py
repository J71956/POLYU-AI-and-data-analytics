import random
diff = eval(input("1 for easy, 2 for medium, 3 for hard, 4 for insane"))
if diff == 1:
    ub = 10
else:
    ub = 100
G= random.randint(0,ub)
print(G)
if diff != 3:
    lives = 3
else:
    lives = 2
guess = int(input("Guess a random number!"))
while guess != G and lives > 0:
    guess = int(input("Guess a random number!"))
    if diff != 4:
        if guess > G:
            print("too high" + "you have " %lives + " chances remaining")
            lives -= 1
        elif guess < G:
            print(" Too low" + "you have " %lives + " chances remaining")
            lives -= 1
        elif guess == G:
            print("You win!")
        if not(lives > 0):
            print("You lose!")
    else:
        if guess > G:
            lives -= 1
            print("you have " %lives + " chances remaining")
        elif guess < G:
            lives -= 1
            print("you have " %lives + " chances remaining")
        elif guess == G:
            print("You win!")
        if not(lives > 0):
            print("You lose!")