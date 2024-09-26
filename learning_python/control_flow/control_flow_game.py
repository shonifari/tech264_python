
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

# Define fighters
fighters_names = ["🧝 ELf", "🥷 Ninja", "🧛 Vampire", "🧙 Wizard"]
attacks_names = ["🗡️","🪄","🪓","🏹"]
life = 75

def yes_no_question(question):
    output = None
    while output is None:
        answer = input(f"{question} y/n: ")
        if answer.lower() not in ["y", "n"]:
            print("⚠️ Respond only with y (Yes) or n (No)")
            sleep(0.8)
            continue

        output = True if answer.lower() == "y" else False
    return  output

# NEW GAME
def new_game():

    fighters = []

    for i, name in enumerate(fighters_names):
        fighters.append(
            {
                "id": i,
                "name": name,
                "life": life,
                "attacks": [{
                        "id":ii,
                        "name": att_name,
                        "power": randint(10, 16),
                        "used":False
                    } for ii, att_name in enumerate(attacks_names)
                ]
            }
            )



    # If Player 2, let them pick the character/fighter they want. If CPU, assign a character/fighter randomly.
    def print_fighters():
        print("SELECT A FIGHTER:")
        for fighter in fighters:
            avg_attack = sum([att.get("power") for att in fighter.get("attacks")]) / len(fighter.get("attacks"))

            spaces = sorted([len(f.get('name')) for f in fighters])[-1]
            spaces -= len(fighter.get('name'))

            fighter_string = f"{fighter.get('id')}. {fighter.get('name').upper()} "
            fighter_string += " "*spaces
            fighter_string +=   f"|  🗡️ Avg att: {avg_attack:.2f} - 🛡️ Life: {fighter.get('life')}"

            print(fighter_string)

    def select_character():
        choice = None
        valid = False
        while not valid:

            print_fighters()

            choice = input("\n🎮 Select a fighter by typing its id: ")
            if not choice.isdigit():
                print("\n⚠️ ERROR: To select a fighter type it's id.\n")
                sleep(0.8)
                continue

            choice = int(choice)

            if choice not in [f.get('id') for f in fighters]:
                print(
                    f"\n⚠️ ERROR: The id you selected ({choice}) is not part of the ids ({','.join([str(f.get('id')) for f in fighters])})\n")
                sleep(0.8)
                continue

            valid = True

        fighter = [f for f in fighters if f.get('id') == choice][0]
        print(f"💠 You have selected {fighter.get('name')}")
        return fighter





    players = []


    # CHARACHTER SELECTION
    p1_character = select_character()
    players.append(p1_character)
    fighters.remove(p1_character)


    # Check for player 2
    is_player_2 = yes_no_question("\n🎮 Add player to the game?")


    if is_player_2:
        players.append(select_character())
    else:
        players.append(choice(fighters))



    print(f"\n\nThe fight will be between:\n\t{players[0].get('name')} VS {players[1].get('name')}")

    if yes_no_question("\n🔔 Ready to start the fight?") == False:
        return

    for n in ["🕔5️⃣","🕓4️⃣","🕒3️⃣","🕑2️⃣","🕐1️⃣"]:
        print(n)
        sleep(1)
    print("🤜 FIGHT 🤛")



    # The two Pokemon/fighters/characters need to fight.


    def print_life():
        string = f"{players[0].get('name')} - {players[0].get('life')}/{life} 🛡️\t"
        string += f" 🛡️ {players[1].get('life')}/{life} - {players[1].get('name')}\n"
        print(string)

    def throw_dice():
        return randint(1,12)

    def print_attacks(fighter):
        for i, att in enumerate(fighter.get("attacks")):
            print(f"{i}. {att.get('name')} - {att.get('power')}{' | (NOT AVAILABLE)' if att.get('used') else ''}")

    def choose_attack(fighter):
        chosen_attack = None
        valid = False
        while not valid:
            print_attacks(fighter)
            chosen_id = input("💠 Choose attack (type the id): ")
            if chosen_id.isdigit() and int(chosen_id) < len(fighter.get('attacks')):
                chosen_attack = fighter.get('attacks')[int(chosen_id)]

                if chosen_attack.get('used'):
                    print(f"⚠️ This attack was already used. Choose another one.")
                    sleep(0.8)
                else:
                    valid = True

        return  chosen_attack

    def reset_attacks():
        if round%5 == 0:
            for pl in players:
                for att in pl.get("attacks"):
                    att['used'] = False
                    pl['attacks'][att.get('id')] = att

            print(f"\n♻️ All attacks are now available again\n")
            sleep(2)

    is_gameover = False
    round = 0
    winner = None
    # ROUND

    while not is_gameover:
        round += 1
        print('_'*25)
        print(f"ROUND {round}")
        sleep(0.5)

        reset_attacks()

        for i in range(0,len(players)):
            # Show current status
            print_life()
            sleep(0.8)

            current_player = i
            defending_player = 1 if i == 0 else 0
            print(f"Its {players[current_player].get('name')} (P{current_player + 1}) turn to attack.")
            sleep(0.3)

            if not is_player_2 and current_player == 1:

                available_attacks = [ atts for atts in players[current_player].get("attacks") if not atts.get('used')]

                choosen_attack = choice(available_attacks)
                print(f"{players[current_player].get('name')} wants to use {choosen_attack.get('name')}:{choosen_attack.get('power')}")
            else:
                # Choose attack
                choosen_attack = choose_attack(players[current_player])
                print(f"{players[current_player].get('name')} wants to use {choosen_attack.get('name')}:{choosen_attack.get('power')}")

                # Roll dice
                input("🎲 Press enter to roll dice")

            # SET ATTACK TO USED
            choosen_attack['used'] = True
            players[current_player]['attacks'][choosen_attack.get('id')] = choosen_attack



            dice_result = throw_dice()
            print(f"{players[current_player].get('name')} rolled 🎲 {dice_result}.")
            sleep(0.2)
            att_power = choosen_attack.get('power') * dice_result // 12
            is_power_higher = False
            print(f"{players[current_player].get('name')} attack power {'increased' if is_power_higher else 'decreased'} and its now: {att_power} {'📈' if is_power_higher else '📉'}")

            print('\n')
            sleep(0.7)


            print("💥")
            sleep(0.8)
            print(f"{players[defending_player].get('name')} was hit with a powerful attack")
            sleep(0.8)




            if players[defending_player]["life"] - att_power <= 0:

                print(f"☠️ KILLER BLOW ☠️")
                sleep(1)
                print(f"{players[defending_player].get('name').upper()} IS DEAD ‼️ ")
                sleep(1)

                # WINNER CONGRATULATIONS
                print("\n")
                congrats_string = f"🎈🎉🎊 Congratulations player {current_player + 1}!! 🎊🎉🎈\n"
                print("🎈🎉🎊✨"*(len(congrats_string)//5))
                if round == 1:
                    congrats_string += f"You won after just {round} round!"
                else:
                    congrats_string += f"You won after {round} rounds!"
                print(congrats_string)
                is_gameover = True
                break



            print(f"{players[defending_player].get('life')} --> {players[defending_player].get('life') - att_power}")
            players[defending_player]["life"] -= att_power
            print("\n")
            sleep(0.8)




play_again = True

while play_again:
    new_game()
    print('-'*25)
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