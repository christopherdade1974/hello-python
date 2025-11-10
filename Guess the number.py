# Guess the number
secret = 5
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("🎉 You got it!")
elif guess > secret:
    print("Too high!")
elif guess > 10 :
    print("I said between 1-10!")
else:
    print("Too low!")
-2