import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name):

    url = f"{base_url}/pokemon/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to get Data :( ")
        print(f"Error Code: {response.status_code}")
        return None



def render_pokemon():
    pass



get_pokemon_data("pikachu")






