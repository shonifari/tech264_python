# Work in your groups of 2-3 to make a single game
# API documentation: PokéAPI (pokeapi.co)
# Recommended: Understand the Pokemon lookup program first (code below) to fully understand accessing data from the API.
# The Pokémon data MUST come from the PokeApi
# Get random Pokémon for at least the CPU (Player can be chosen or random)


# Pokémon should fight and a winner should be declared in some way
# No Pygame. Focus on interacting with the API.
# Be as creative as you like after this. Can you incorporate different abilities/stats etc.?
# Try and work collaboratively on the one repo using Git
# To deliver: Give it your best shot! Share your code (message your Ramon + Luke directly, NOT a message in the main chat) by COB (17:00)
import requests
import json
from time import sleep
from random import choice, randint

LIFE = 100


# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
url = f'https://pokeapi.co/api/v2/pokemon/?offset={randint(20,200)}&limit=20'
response = requests.get(url)
print(response.content)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    pokemon_id = pokemon['url'].split('/')[-2]
    print(f"{pokemon_id}. {pokemon['name'].capitalize()}")


# Ask the user to choose a pokemon
user_choice = input('Enter your pokemon: ').lower()

# Get the pokemon's data from the API



def init_pokemon(pokemon_id:str)-> dict:
    pokemon = {'life':LIFE}

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon_data = json.loads(response.text)

    # for key in pokemon_data['stats']:
    #     print(key)
    #


    # ID
    pokemon['id'] = pokemon_data['id']
    # Name
    pokemon['name'] = pokemon_data['name'].capitalize()
    # to format height and weight properly
    height = int(pokemon_data['height'])
    weight = int(pokemon_data['weight'])

    height_formatted = height / 10
    weight_formatted = weight / 10

    pokemon['height'] = height_formatted
    pokemon['weight'] = weight_formatted

    attacks = []
    while len(attacks) < 4:
        chosen_att = choice(pokemon_data['moves'])
        if not chosen_att['move']['url'] in [att['url'] for att in attacks]:

            name = chosen_att['move']['name']
            name = ' '.join([name_part.capitalize() for name_part in name.split('-')])

            attacks.append({
                'name':name,
                'url': chosen_att['move']['url'],
                "power": randint(15, 20),
                "used": False
            })

    pokemon['attacks'] = attacks

    return pokemon

def print_life():
    '''Prints the current life of each player'''
    string = f"{players[0].get('name')} - {players[0].get('life')}/{LIFE} 🛡️\t"
    string += f" 🛡️ {players[1].get('life')}/{LIFE} - {players[1].get('name')}\n"
    print(string)

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




players = [
    # Pokemon user 1
    init_pokemon(user_choice),

    # Pokemon CPU
    init_pokemon(str(randint(1,200)))

    ]

print(f"CPU chose {players[1].get('name')}")
sleep(0.8)

print(f"The fight will be between:\n{players[0].get('name')}   vs   {players[1].get('name')}")
print(1)


# GAMEPLAY
is_gameover = False
round = 0

while not is_gameover:
    round += 1

    print('_' * 25)
    print(f"ROUND {round}")
    sleep(0.5)
    print_life()
    for i in range(0, len(players)):

        # Set which player is attacking/defending
        current_player = i
        defending_player = 1 if i == 0 else 0

        print(f"Its {players[current_player].get('name')} (P{current_player + 1}) turn to attack.")

        if current_player == 1:
            chosen_attack = choice(players[current_player]['attacks'])
        else:
            for i, attack in enumerate(players[current_player]['attacks']):
                print(f"{i}. {attack['name']} \t {attack['power']}")

            user_choice = int(input("Choose an attack: "))
            chosen_attack = players[current_player]['attacks'][user_choice]


        print(f"{players[current_player].get('name')} wants to use {chosen_attack.get('name')}:{chosen_attack.get('power')}")
        att_power = chosen_attack['power']


        # Check if defending player died
        # BATTLE
        # Show battle
        print('\n')
        sleep(0.7)
        for boom in "💥💥💥":
            print(boom, end='')
            sleep(0.7)
        print()
        sleep(0.8)
        print(f"{players[defending_player].get('name')} was hit with a powerful attack")
        sleep(0.8)




        # PLAYER IS DEAD
        # Calculate if the player died
        if players[defending_player]["life"] - att_power <= 0:

            print(f"☠️ KILLER BLOW ☠️")
            sleep(1)
            print(f"{players[defending_player].get('name').upper()} IS DEAD ‼️ ")
            sleep(1)

            # WINNER CONGRATULATIONS
            print("\n")
            congrats_string = f"🎈🎉🎊 Congratulations player {current_player + 1}!! 🎊🎉🎈"
            print("🎈🎉🎊✨" * (len(congrats_string) // 7))
            print(congrats_string)


            if round == 1:
                print(f"You won after just {round} round!")
            else:
                print(f"You won after {round} rounds!")

            # Terminate
            is_gameover = True
            break


        # Change defending player's life
        print_player_damages(players[defending_player], att_power)
        players[defending_player]["life"] -= att_power
        print("\n")
        sleep(0.8)