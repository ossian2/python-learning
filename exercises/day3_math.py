answer = 4

guess = int(input("2 + 3 + x = 9, what is x? "))

if guess == answer:
    print("You are correct!")
elif guess > answer:
    print(f"Too high! The answer is {answer}.")
else:
    print(f"Too low! The answer is {answer}.")