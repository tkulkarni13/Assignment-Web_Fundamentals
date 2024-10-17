# Task 1: Setting up a Python Virtual Environmnent and Installing Packages
import requests
import json

# Task 2: Fetching Data from the Pokemon API
url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url)
json_data = response.text

pikachu_data = json.loads(json_data)

print(f"Name: {pikachu_data["name"]}")

# Original solution
"""
ability1 = pikachu_data["abilities"][0]
ability2 = pikachu_data["abilities"][1]

print(f"Ability 1: {ability1["ability"]["name"]}")
print(f"Ability 2: {ability2["ability"]["name"]}")
"""

# Cleaner solution
for i, ability in enumerate(pikachu_data["abilities"]):
    print(f"Ability {i+1}: {ability["ability"]["name"]}")

# Task 3: Analyzing and Displaying Data
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(url)
        json_data = response.text
        poke_data = json.loads(json_data)
        return poke_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def calculate_average_weight(pokemon_list):
    sum = 0
    length = len(pokemon_list)
    for pokemon in pokemon_list:
        data = fetch_pokemon_data(pokemon)
        weight = data["weight"]
        sum += weight
    return sum / length

pokemon_list = ["pikachu", "bulbasaur", "charmander"]
print(calculate_average_weight(pokemon_list))