
# The options
#
# Battle Game
# Dice roll game
# Interactive quiz game
# All the games should use the CLI (not anything like the pygame library).
#
#
#
#
#
# Battle game
#
# Make a 2 player battle game using Python.


# Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.

from random import  randint, choice
from time import  sleep

fighters_name = ["A", "B","C","D"]
attacks_names = ["1","2","3","4"]


def yes_no_question(question):
    output = None
    while output is None:
        answer = input(f"{question} y/n: ")
        if answer.lower() not in ["y", "n"]:
            print("Respond only with y (Yes) or n (No)")
            sleep(0.8)
            continue

        output = True if answer.lower() == "y" else False
    return  output




def new_game():

    FIGHTERS = []

    for i, name in enumerate(fighters_name):
        FIGHTERS.append(
            {
                "id": i,
                "name": name,
                "life": 10,
                "attacks": [{
                        "name": att_name,
                        "power": randint(10, 16)
                    } for att_name in attacks_names
                ]
            }
            )

    # If Player 2, let them pick the character/fighter they want. If CPU, assign a character/fighter randomly.
    def print_fighters():
        print("SELECT A FIGHTER:")
        for fighter in FIGHTERS:
            avg_attack = sum([att.get("power") for att in fighter.get("attacks")]) / len(fighter.get("attacks"))

            print(
                f"{fighter.get('id')}. {fighter.get('name').upper()}\n  - Avg att: {avg_attack:.2f}\n  - Life: {fighter.get('life')}")

    def select_character():
        choice = None
        valid = False
        while not valid:

            print_fighters()

            choice = input("Select a fighter by typing its id: ")
            if not choice.isdigit():
                print("\nERROR: To select a fighter type it's id.\n")
                sleep(0.8)
                continue

            choice = int(choice)

            if choice < 0 or choice not in [f.get('id') for f in FIGHTERS]:
                print(
                    f"\nERROR: The id you selected ({choice}) is not part of the ids ({','.join([str(f.get('id')) for f in FIGHTERS])})\n")
                sleep(0.8)
                continue

            valid = True
        fighter = [f for f in FIGHTERS if f.get('id') == choice][0]
        print(f"You have selected {fighter.get('name')}")
        return fighter

    players = []


    # CHARACHTER SELECTION
    p1_character = select_character()
    players.append(
        p1_character
    )
    FIGHTERS.remove(p1_character)





    is_player_2 = yes_no_question("Add player to the game?")
    p2_character = None
    if is_player_2:
        players.append(
            select_character()
        )
    else:
        players.append(
            choice(FIGHTERS)
        )



    print(f"\n\nThe fight will be between:\n\t{players[0].get('name')} VS {players[1].get('name')}")

    if yes_no_question("Start fight?") == False:
        print("Start the program over.")
        return

    for i in range(0,5):
        print(f"{5-i}...")
        sleep(1)
    print("FIGHT!!!")



    # The two Pokemon/fighters/characters need to fight.


    def print_life():
        string = f"{players[0].get('name')} - {players[0].get('life')}/100\t"
        string += f"{players[1].get('name')} - {players[1].get('life')}/100\n"
        print(string)

    def throw_dice():
        return randint(1,10)

    def print_attacks(fighter):
        for i, att in enumerate(fighter.get("attacks")):
            print(f"{i}. {att.get('name')} - {att.get('power')}")

    def choose_attack(fighter):
        chosen_attack = None
        valid = False
        while not valid:
            print_attacks(fighter)
            choice = input("Choose attack (type the id): ")
            if choice.isdigit() and int(choice) < len(fighter.get('attacks')):
                chosen_attack = fighter.get('attacks')[int(choice)]
                valid = True

        return  chosen_attack



    is_gameover = False
    round = 0
    winner = None
    # ROUND

    while not is_gameover:
        round += 1
        print(f"ROUND {round}")
        sleep(0.5)

        for i in range(0,len(players)):
            # Show current status
            print_life()

            current_player = i
            defending_player = 1 if i == 0 else 0

            current_fighter = FIGHTERS[current_player]
            defending_fighter = FIGHTERS[defending_player]

            print(f"Its player {current_player + 1} turn to attack.")
            sleep(0.3)

            # Choose attack

            choosen_attack = choose_attack(current_fighter)
            print(f"{current_fighter.get('name')} wants to use {choosen_attack.get('name')}:{choosen_attack.get('power')}")

            input("Press enter to roll dice")
            dice_result = throw_dice()
            print(f"{current_fighter.get('name')} rolled {dice_result}.")
            sleep(0.2)
            att_power = choosen_attack.get('power') * dice_result // 12
            print(f"{current_fighter.get('name')} attack power is now: {att_power}")
            print('\n')
            sleep(0.5)


            print(f"{defending_fighter.get('name')} was hit with a powerful attack")
            print(f"{defending_fighter.get('life')} --> {defending_fighter.get('life') - att_power}")
            players[defending_player]["life"] -= att_power
            print("\n")
            sleep(0.8)

            if players[defending_player]["life"] <= 0:
                is_gameover = True
                winner = current_player

    print(f"Congratulations player {winner}!!\nYou won ater {round} rounds!")

new_game()
play_again = yes_no_question("Do you want to play again?")

while play_again:
    new_game()
    play_again = yes_no_question("Do you want to play again?")



# A winner must be declared via some sort of calculation.
#
#
#
# Bonus: Want to play again?
#
# Note: No Pygame or Turtle allowed. CLI only.
#
#
#
#
#
# Interactive quiz
#
# Create and interactive quiz game using Python.
#
#
#
# The subject can be what you want. Why not try to give the user an outcome at the end, like their personality type, what avenger they would be, what position on a football team would best suit them, etc?
#
#
#
# Start by asking if they are ready to play the quiz, if they are start the game.
#
#
#
# Ask question one, work out if the answer given is correct and if so add to a score variable.
#
#
#
# Keep asking questions. As many as you like.
#
#
#
# When the quiz ends, give them their score back, if you can give them back something more interesting than a score, that would be awesome!
#
#
#
# Bonus: Want to play again?
#
#
#
#
#
#
#
# Dice game
#
# Make a dice game:
#
#
#
# Let's make a game that rolls a dice and picks a winner.
#
#
#
# Start the game with a welcome message and ask if the user is ready to play.
#
#
#
# Get the user's name and start a loop (While loop recommended)
#
#
#
# Use the random library and a method from that library to roll, a number 1-6
#
#
#
# Store the number in a variable
#
#
#
# Do the same for the computer
#
#
#
# Compare the two numbers, whose was bigger? Tell the user! and end the game
#
#
#
# Now add functionality to the game. Let the User and the CPU roll until one gets to 30. The one that gets there first is the winner!
#
#
#
# Bonus: Want to play again?