# The options
#
# Battle Game
# Dice roll game
# Interactive quiz game
# All the games should use the CLI (not anything like the pygame library).


# Battle game

# Make a 2 player battle game using Python.


# Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.

# If Player 2, let them pick the character/fighter they want. If CPU, assign a character/fighter randomly.

from random import  randint, choice
from time import  sleep

# Define fighters
FIGHTERS_NAMES = ["🧝 ELf", "🥷 Ninja", "🧛 Vampire", "🧙 Wizard"]
ATTACKS_NAMES = ["🗡️", "🪄", "🪓", "🏹"]
LIFE = 75


# METHODS
def yes_no_question(question : str):
    '''Prompt player with the provided question'''
    while True:
        sequence_printing(f"{question} y/n: ", break_line=False)
        answer = input(f"\r{question} y/n: ")

        if answer.lower() not in ["y", "n"]:
            print_warning("⚠️ Respond only with y (Yes) or n (No)")
            sleep(0.8)
            continue

        return True if answer.lower() == "y" else False

def sequence_printing(string:str, break_line = True):
    printed = ""
    for ch in string:
        printed += ch
        print(f"\r{printed}", end="")
        sleep(.02)

    if break_line:
        print()

def print_warning(warn_string, repetitions = 5, speed = 0.25):
    for i in range(0, repetitions*2):
        print(f"\r{'' if i % 2 == 0 else warn_string}", end='')
        sleep(speed)
    print()




# NEW GAME
def new_game():
    '''Start a new game. Only breaks after winning or character selection'''

    fighters = []

    # Initialise the fighters
    for i, name in enumerate(FIGHTERS_NAMES):
        fighters.append(
            {
                "id": i,
                "name": name,
                "life": LIFE,
                "attacks": [{
                        "id":ii,
                        "name": att_name,
                        "power": randint(10, 16),
                        "used":False
                    } for ii, att_name in enumerate(ATTACKS_NAMES)
                ]
            }
            )





    def print_fighters():
        '''Prints a list of available fighters'''
        sequence_printing("SELECT A FIGHTER:")

        # Get the length of longest name
        longest_name_length = sorted([len(f.get('name')) for f in fighters])[-1]

        for fighter in fighters:
            avg_attack = sum([att.get("power") for att in fighter.get("attacks")]) / len(fighter.get("attacks"))

            # Calculate spaces to print neatly
            spaces = longest_name_length - len(fighter.get('name'))

            #
            fighter_string = f"{fighter.get('id')}. {fighter.get('name').upper()} "
            fighter_string += " "*spaces
            fighter_string +=   f"|  🗡️ Avg att: {avg_attack:.2f} - 🛡️ Life: {fighter.get('life')}"

            sequence_printing(fighter_string)

    def select_character():
        '''Prompt the user to select a fighter and returns it'''
        fighter = None
        while True:

            print_fighters()

            sequence_printing("🎮 Select a fighter by typing its id: ", False)
            fighter_id = input("\r🎮 Select a fighter by typing its id: ")

            if not fighter_id.isdigit():
                print_warning("⚠️ ERROR: To select a fighter type it's id.")
                sleep(0.8)
                continue

            fighter_id = int(fighter_id)

            if fighter_id not in [f.get('id') for f in fighters]:
                print_warning(
                    f"⚠️ ERROR: The id you selected ({fighter_id}) is not part of the ids ({','.join([str(f.get('id')) for f in fighters])})")
                sleep(0.8)
                continue

            fighter = [f for f in fighters if f.get('id') == fighter_id][0]
            break


        sequence_printing(f"💠 You have selected {fighter.get('name')}\n")
        return fighter




    # Initialise players
    players = []

    # P1 character selection
    p1_character = select_character()
    players.append(p1_character)
    fighters.remove(p1_character)

    # Check for player 2 or set as CPU

    is_player_2 = yes_no_question("🎮 Add player to the game?")
    if is_player_2:
        players.append(select_character())
    else:
        players.append(choice(fighters))

    print('\n')
    sequence_printing(f"The fight will be between:")
    sequence_printing(f"\t{players[0].get('name')} VS {players[1].get('name')}")
    sleep(.8)


    # Confirm start of fight
    print('\n')
    if yes_no_question("🔔 Ready to start the fight?") == False:
        return

    # Countodown
    for n in ["🕔5️⃣","🕓4️⃣","🕒3️⃣","🕑2️⃣","🕐1️⃣"]:
        print(f"\r{n}", end='')
        sleep(1)
    print()

    print_warning("🤜 FIGHT 🤛")


    # GAMEPLAY METHODS

    def print_life():
        '''Prints the current life of each player'''
        string = f"{players[0].get('name')} - {players[0].get('life')}/{LIFE} 🛡️\t"
        string += f" 🛡️ {players[1].get('life')}/{LIFE} - {players[1].get('name')}\n"
        print(string)

    def throw_dice():
        return randint(1,12)

    def print_attacks(fighter):
        '''Prints a list of attacks of the provided fighter'''
        for i, att in enumerate(fighter.get("attacks")):
            sequence_printing(f"{i}. {att.get('name')} - {att.get('power')}{' | (NOT AVAILABLE)' if att.get('used') else ''}")

    def choose_attack(fighter):
        '''Prompt the player with the list of attacks of their fighter. Player selects one available '''

        while True:
            print_attacks(fighter)

            chosen_id = input("💠 Choose attack (type the id): ")
            if chosen_id.isdigit() and int(chosen_id) < len(fighter.get('attacks')):
                attack = fighter.get('attacks')[int(chosen_id)]

                if not attack.get('used'):
                    break

                print_warning(f"⚠️ This attack was already used. Choose another one.")
                continue

            print_warning(f"⚠️ Input the attack id.")

        return  attack

    def reset_attacks():
        '''Reset availability of every attack'''
        for pl in players:
            for att in pl.get("attacks"):
                att['used'] = False
                pl['attacks'][att.get('id')] = att

        print('\n')

        sequence_printing("♻️ All attacks are now available again")
        print('\n')
        sleep(2)

    def print_player_damages(player, damage):
        '''A'''
        player_life = player.get('life')
        icons = ["🟢", "🟡", "🟠", "🔴"]

        for hit in range(0, damage + 1):

            current_life = player_life - hit
            current_life_percentage = current_life * 100 / LIFE
            icon = ""

            if current_life_percentage >= 75:
                icon = "🟢"
            elif current_life_percentage >= 50:
                icon = "🟡"
            elif current_life_percentage >= 25:
                icon = "🟠"
            elif current_life_percentage >= 0:
                icon = "🔴"
            else:
                icon = "⚫"


            print(f"\r{players[defending_player].get('life')} --> {current_life} {icon} ({current_life_percentage:.2f}%)", end='')
            sleep(0.2)

    # GAMEPLAY
    is_gameover = False
    round = 0

    while not is_gameover:
        round += 1

        print('_'*25)
        print(f"ROUND {round}")
        sleep(0.5)

        # Check if last round is multiple of number of attacks, then there are no more available attacks
        if (round - 1) % len(ATTACKS_NAMES) == 0:
            reset_attacks()

        # PLAYERS TURN
        for i in range(0,len(players)):

            # Show current status
            print_life()
            sleep(0.8)

            # Set which player is attacking/defending
            current_player = i
            defending_player = 1 if i == 0 else 0
            sequence_printing(f"Its {players[current_player].get('name')} (P{current_player + 1}) turn to attack.")
            sleep(0.3)

            # If playing against CPU
            if not is_player_2 and current_player == 1:
                sleep(0.5)
                available_attacks = [ atts for atts in players[current_player].get("attacks") if not atts.get('used')]
                chosen_attack = choice(available_attacks)
                sequence_printing(f"{players[current_player].get('name')} wants to use {chosen_attack.get('name')}:{chosen_attack.get('power')}")
                sleep(0.8)


            else:
                # Choose attack
                chosen_attack = choose_attack(players[current_player])
                sequence_printing(f"{players[current_player].get('name')} wants to use {chosen_attack.get('name')}:{chosen_attack.get('power')}")

                # Roll dice
                input("🎲 Press enter to roll dice")


            # Set the attack to used
            chosen_attack['used'] = True
            players[current_player]['attacks'][chosen_attack.get('id')] = chosen_attack


            # Roll the dice
            dice_result = throw_dice()
            sequence_printing(f"{players[current_player].get('name')} rolled 🎲 {dice_result}.")
            sleep(0.2)

            # Calculate attack power
            att_power = chosen_attack.get('power') * dice_result // 12
            is_power_higher = False
            sequence_printing(f"{players[current_player].get('name')} attack power {'increased' if is_power_higher else 'decreased'} and its now: {att_power} {'📈' if is_power_higher else '📉'}")

            # Show battle
            print('\n')
            sleep(0.7)
            for boom in "💥💥💥":
                print(boom, end='')
                sleep(0.7)
            print()
            sleep(0.8)
            sequence_printing(f"{players[defending_player].get('name')} was hit with a powerful attack")
            sleep(0.8)



            # Check if defending player died
            if players[defending_player]["life"] - att_power <= 0:

                sequence_printing(f"☠️ KILLER BLOW ☠️")
                sleep(1)
                sequence_printing(f"{players[defending_player].get('name').upper()} IS DEAD ‼️ ")
                sleep(1)

                # WINNER CONGRATULATIONS
                print("\n")
                congrats_string = f"🎈🎉🎊 Congratulations player {current_player + 1}!! 🎊🎉🎈"
                print("🎈🎉🎊✨"*(len(congrats_string)//7))
                sequence_printing(congrats_string)

                if round == 1:
                    congrats_string += f"You won after just {round} round!"
                else:
                    congrats_string += f"You won after {round} rounds!"
                sequence_printing(congrats_string)

                # Terminate
                is_gameover = True
                break


            # Change defending player's life
            print_player_damages(players[defending_player], att_power)
            #print(f"{players[defending_player].get('life')} --> {players[defending_player].get('life') - att_power}")
            players[defending_player]["life"] -= att_power
            print("\n")
            sleep(0.8)

if __name__ == '__main__':

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