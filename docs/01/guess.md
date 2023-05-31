```py
import random

number = random.randint(1, 10)
guess = -1

for i in range(3):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("You guessed it!")
        break
    if guess == number:
        break
```
[Back](./#guessing-game)