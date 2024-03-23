import random

list_of_names = ["hesham", "gannah", "samar", "islam", "ahmed", "esam"]

computer_shuffle = random.choice(list_of_names)

print("The name contains * letters :")

guesses = ''
attempts = 12

while attempts > 0:
    failed = 0

    for letter in computer_shuffle:
        if letter in guesses:
            print(letter)
        else:
            print("*")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The name is :", computer_shuffle)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in computer_shuffle:
        attempts -= 1
        print("Wrong guess")
        print(f"You have {attempts} more guesses")

        if attempts == 0:
            print("Game over")