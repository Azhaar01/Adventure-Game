import time
import random
import pycodestyle

enemy = ["pirate", "troll", "wicked fairie", "dragon", "gorgon"]
user_choice = random.choice(enemy)
weapon = 0


def print_pause(massage, seconds):
    print(massage)
    time.sleep(seconds)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.", 2)
    print_pause(f"Rumor has it that a {user_choice} is somewhere around here,"
                "and has been terrifying the nearby village.", 2)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.", 2)


intro()


def ask():
    print_pause("\nEnter 1 to knock on the door of the house.", 2)
    print_pause("Enter 2 to peer into the cave.", 2)
    print_pause("What would you like to do?", 2)


def run():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.", 2)


ask()
while True:
    choose = input("Please enter 1 or 2.)\n")

    if '1' in choose:
        print_pause("You approach the door of the house.", 2)
        print_pause("You are about to knock when the door opens "
                    f"and out steps a {user_choice}.", 2)
        print_pause(f"Eep! This is the {user_choice}'s house!", 2)
        print_pause(f"The {user_choice} attacks you!", 2)
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.", 2)

        decide = input("Would you like to (1) fight or (2) run away?")

        while decide != '1' and decide != '2':
            decide = input("Would you like to (1) fight or (2) run away?")

        if '1' in decide:
            if weapon == 0:
                print_pause("You do your best...", 2)
                print_pause("but your dagger is no match "
                            f"for the {user_choice}.", 2)
                print_pause("You have been defeated!", 2)

            if weapon == 1:
                print_pause(f"As the {user_choice} moves to attack, "
                            "you unsheath your new sword.", 2)
                print_pause("The Sword of Ogoroth shines brightly in your "
                            "hand as you brace yourself for the attack.", 2)
                print_pause(f"But the {user_choice} takes one look at "
                            "your shiny new toy and runs away!", 2)
                print_pause(f"You have rid the town of the {user_choice}. "
                            "You are victorious!", 2)

            again = input("Would you like to play again? (y/n)").lower()

            while again != 'y' and again != 'n':
                again = input("Would you like to play again? (y/n)").lower()

            if again == 'y':
                print_pause("Excellent! Restarting the game ...", 2)
                weapon = 0
                global user_choice
                user_choice = random.choice(enemy)
                intro()
                ask()

            elif again == 'n':
                print_pause("Thanks for playing! See you next time.", 2)
                break
        if '2' in decide:
            run()
            ask()
    if '2' in choose:
        if weapon == 0:
            print_pause("You peer cautiously into the cave.", 2)
            print_pause("It turns out to be only a very small cave.", 2)
            print_pause("Your eye catches a glint of metal behind a rock.", 2)
            print_pause("You have found the magical Sword of Ogoroth!", 2)
            print_pause("You discard your silly old dagger "
                        "and take the sword with you.", 2)
            print_pause("You walk back out to the field.", 2)
            weapon = 1
            ask()

        elif weapon == 1:
            print_pause("You peer cautiously into the cave.", 2)
            print_pause("you've been here before, and gotten all the good "
                        "stuff. It's just an empty cave now.", 2)
            print_pause("You walk back out to the field.", 2)
            ask()

