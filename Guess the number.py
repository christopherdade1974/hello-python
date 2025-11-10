# Guess the number
secret = 5
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("🎉 You got it!")
elif guess > secret:
    print("Too high!")
else:
    print("Too low!")
