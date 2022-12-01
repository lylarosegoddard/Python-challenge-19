from app.guess import Guess

guess = int(input("What is your guess?"))
print(Guess(guess).comment())