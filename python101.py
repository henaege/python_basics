import random


def guess_game():
    secret_num = random.randint(1, 10)
    print ("I am thinking of a number between 1 and 10.")
    print ("What's the number?")
    guess_num = int(input("> "))
    tried_times = 1
    not_guessed = True
    while not_guessed:
        if tried_times > 5:
            print ("You ran out of guesses!")
            not_guessed = False
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
            not_guessed = False
    print ("Do you want to play again (Y or N)?")
    users_answer = input("> ")
    if users_answer == "Y":
        guess_game()
    else:
        return "Bye!"


print (guess_game())
