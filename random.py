import random
print("                                                    Number Guessing Game")
number = random.randint(1, 20)
chances = 0
print("Guess A Number Between 1 and 20")

while chances < 5:
    guess = int(input("Enter Your Guess: "))

    if guess == number:
        print("Congratulations You Won! ")
        break
    elif guess-number==1:
        print("Your guess is close")
        
    elif guess-number == -1:
        print("your guess is close")

    elif guess < number:
        print("Your Guess Was Too Low: Guess A Number Higher Than", guess)

    else:
        print("Your Guess Was Too High: Guess A Number Lower Than", guess)

    chances += 1

    if not chances < 5:
        print("You Loose! The Number Is", number)