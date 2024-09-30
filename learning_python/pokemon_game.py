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
from time import sleep
import requests
import json
from random import choice, randint

LIFE = 100


# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    pokemon_id = pokemon['url'].split('/')[-2]
    print(f"{pokemon_id}. {pokemon['name']}")



# Ask the user to choose a pokemon
user_choice = input('Enter your pokemon: ').lower()

# Get the pokemon's data from the API



def init_pokemon(pokemon_id:str)-> dict:
    pokemon = {'life':LIFE}

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon_data = json.loads(response.text)

    # ID
    pokemon['id'] = pokemon_data['id']
    # Name
    pokemon['name'] = pokemon_data['name']
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
            attacks.append({
                'name':chosen_att['move']['name'],
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

players = [
    # Pokemon user 1
    init_pokemon(user_choice),

    # Pokemon CPU
    init_pokemon(str(randint(1,200)))

    ]

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

        att_power = chosen_attack['power']
        # Check if defending player died

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
                congrats_string += f"You won after just {round} round!"
            else:
                congrats_string += f"You won after {round} rounds!"
            print(congrats_string)

            # Terminate
            is_gameover = True
            break

        players[defending_player]["life"] -= att_power
        print("\n")
        sleep(0.8)