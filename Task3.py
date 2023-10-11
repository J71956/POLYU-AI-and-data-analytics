import random
list = ["computer", 'python', 'human', 'keyboard', 'mouse']
selcwrd = list[random.randint(0,len(list))]
start_range = 0 # inclusive 
end_range = len(selcwrd) # exclusive (Length of word)

word = []
chances = 4
num_samples = 3 # Number of random numbers to generate 
diff = int(input("press 1 for easy, 2 for medium, 3 for hard"))
if diff == 1:
    chances = 4
    num_samples = round(selcwrd/2)
elif diff == 2:
    chances = 3
    num_samples = round(selcwrd*0.4)
elif diff == 3:
    chances = 2
    num_samples = round(selcwrd*0.3)



random_numbers = random.sample(range(start_range, end_range), num_samples) 

for i in range(0, len(selcwrd)):
    if i not in random_numbers:
        word.append("_")
    elif i in random_numbers:
        word.append(selcwrd[i])
print(''.join(word))

while chances > 0 and word.count("_") >0:
    guess = str(input("guess a letter! "))
    if selcwrd.count(guess) > 0:
        for c in range (0, len(selcwrd)):
            if guess == selcwrd[c]:
                word[c] = selcwrd[c]
                print(''.join(word))
    else:
        chances -= 1
        print("Not in word! You have " + str(chances) +" left")
else:
    print("You win!")
if not(chances > 0):
    print("You lose!")
elif word.count("_") >0:
    print("you win!")