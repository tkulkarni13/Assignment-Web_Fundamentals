# Task 1: Set up a Python Virtual Environment and Install Required Packages
import requests

# Task 2: Fetch Space Data from a Space API
def fetch_planet_data():
    url = 'https://api.le-systeme-solaire.net/rest/bodies'
    response = requests.get(url)
    bodies = response.json()['bodies']
    planets = []

    for body in bodies:
        if body['isPlanet']:
            name = body['englishName']
            massValue = body['mass']['massValue']
            massExponent = body['mass']['massExponent']
            mass = 10**massExponent * massValue
            orbit_period = body['sideralOrbit']

            planet = (name, mass, orbit_period)
            planets.append(planet)
            
            """
            print(f"Planet: {name}, Mass: {mass['massValue']} * 10^{mass['massExponent']}, "\
                  f"Orbit Period: {orbit_period} days")
            """
    return planets

print(fetch_planet_data())

# Task 3: Data Representation and Analysis
def find_heaviest_planet(planets):
    heaviest_planet = ("", 0)
    for planet in planets:
        mass = planet[1]

        if mass > heaviest_planet[1]:
            heaviest_planet = (planet[0],planet[1])
    return heaviest_planet

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg")
