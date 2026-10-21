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




#DOUBTS...
def draw_image_on_terminal(image_pil, max_width=60):
    """
    Desenha o Pokémon eliminando automaticamente os espaços vazios 
    (linhas transparentes) acima, abaixo e nas laterais da imagem.
    """
    image_pil = image_pil.convert("RGBA")

    # --- O SEGREDO DO CORTE (CROP) ---
    # getbbox() encontra as coordenadas exatas onde o desenho do Pokémon começa e termina
    caixa_do_desenho = image_pil.getbbox()
    if caixa_do_desenho:
        # Recorta a imagem eliminando todo o espaço transparente ao redor
        image_pil = image_pil.crop(caixa_do_desenho)

    # Redimensiona mantendo a proporção a partir da imagem já recortada
    width, height = image_pil.size
    aspect_ratio = height / width
    new_width = max_width
    new_height = int(max_width * aspect_ratio)

    if new_height % 2 != 0:
        new_height += 1

    image_pil = image_pil.resize((new_width, new_height), Image.Resampling.NEAREST)

    print("\nSPRITE:")
    for y in range(0, new_height, 2):
        line = ""
        for x in range(new_width):
            r1, g1, b1, a1 = image_pil.getpixel((x, y))
            r2, g2, b2, a2 = image_pil.getpixel((x, y + 1))

            if a1 < 50 and a2 < 50:
                line += "\033[0m "
                continue

            if a1 < 50:
                ansi_top = "\033[38;2;0;0;0;0m"
                char = " "
            else:
                ansi_top = f"\033[38;2;{r1};{g1};{b1}m"
                char = "▀"

            if a2 < 50:
                ansi_bottom = "\033[49m"
            else:
                ansi_bottom = f"\033[48;2;{r2};{g2};{b2}m"

            line += f"{ansi_bottom}{ansi_top}{char}"

        print(line + "\033[0m")











# ID / NAME / height / weight / abilities(data['abilities'][0]['ability']['name']) / type(data['types'][0]['type']['name']) /sprite(imagem) 
def render_pokemon(name):
    data = get_pokemon_data(name)

    if data:
        image_url = data['sprites']['front_default']

        if image_url:
            image_response = requests.get(image_url)
            image_data = io.BytesIO(image_response.content)
            pokemon_image = Image.open(image_data)

            
            draw_image_on_terminal(pokemon_image)
        else:
            print("Image not found :(")


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





render_pokemon("raichu")






