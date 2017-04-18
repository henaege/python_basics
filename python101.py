import random


def guess_game():
    secret_num = random.randint(1, 10)
    print ("I am thinking of a number between 1 and 10.")
    print ("What's the number?")
    guess_num = int(input("> "))
    tried_times = 1
    while guess_num != secret_num:
        if tried_times > 5:
            print ("You ran out of guesses!")
            break
        if guess_num > secret_num:
            print ("%d is too high." % guess_num)
        else:
            print ("%d is too low." % guess_num)
        print ("Nope, try again.")
        print ("What's the number?")
        guess_num = int(input("> "))
        tried_times += 1
    if guess_num == secret_num:
        print ("Yes! You win!")
    print ("Do you want to play again (Y or N)?")
    users_answer = input("> ")
    if users_answer == "Y":
        guess_game()
    else:
        return print("Bye!")


guess_game()
