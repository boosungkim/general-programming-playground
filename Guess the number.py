import random

secret = random.randint(1,20)
print("I am thinking of a number between 1 and 20")
print("I'll give you 3 tries! Try your best :)")
#Ask the player to guess 6 times
for i in range(1,4):
    print("Take a guess")
    guess = int(input())
    if guess < secret:
        print("Your answer is too low")
        print("You have " + str(3-i) + " tries remaining!")
    elif guess > secret:
        print("Your guess is too high")
        print("You have " + str(3-i) + " tries remaining!")
    else:
        break

if guess == secret:
    print("Good job! You guessed my number in " + str(i) + " guesses!")
else:
    print("Wrong dipshit, The number is " + str(secret) + ".")
