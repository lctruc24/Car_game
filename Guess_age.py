max_age = 100
min_age = 0

guess_age = (max_age + min_age)/2
print(f"Your age: {guess_age}")

while True:
    guess_age = (max_age + min_age)/2
    
    print("Your age is higher than the guessed age")

    answer = input("")

    if answer.lower() == "yes":

        min_age = guess_age

        guessed_age = int((max_age + min_age)/2)

        print(f"Your age: {guessed_age}")

    elif answer.lower() == "no":

        max_age = guess_age

        guessed_age = int((max_age + min_age)/2)

        print(f"Your age: {guessed_age}")

    
    elif answer.lower() == "perfect":
        print("---Congratulation!!!!!---")
        print(f"You are {guessed_age} years old")
        break