import requests
from PIL import Image
import io




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





def draw_image_on_terminal():
    pass


# ID / NAME / height / weight / abilities(data['abilities'][0]['ability']['name']) / type(data['types'][0]['type']['name']) /sprite(imagem) 
def render_pokemon(name):
    data = get_pokemon_data(name)

    if data:
        print(f"ID: {data['id']}")
        print(f"NAME: {data['name']}")
        print(f"HEIGHT: {data['height']}")
        print(f"WEIGHT: {data['weight']}")

        ability_names = [item['ability']['name'] for item in data['abilities']]
        ability_names_join = ", ".join(ability_names)
        print(f"ABILITIES: {ability_names_join}")

        type_names = [item['type']['name'] for item in data['types']]
        type_names_join = ", ".join(type_names)
        print(f"TYPES: {type_names_join}")

        image_url = data['sprites']['front_default']

        if image_url:
            image_response = requests.get(image_url)
            image_data = io.BytesIO(image_response.content)
            pokemon_image = Image.open(image_data)

            draw_image_on_terminal(pokemon_image, new_width=50)
        else:
            print("Image not found :(")





render_pokemon("charizard")






