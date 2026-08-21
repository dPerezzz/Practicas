from PIL import Image
import requests
from io import BytesIO
import ascii_magic

while True:
    pokemon = input('Ingresa el nombre del pokemon: ').strip().lower()
     
    if not pokemon:
        print('Error: No puedes ingresar un valor vacio')
        continue

    URL= f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(URL)

    if response.status_code == 200:
        print('Conexion exitosa')
        data = response.json()
        spriteURL = data['sprites']['front_default']
        response_image = requests.get(spriteURL)
        image = Image.open(BytesIO(response_image.content)).convert('RGBA')
        fondo = Image.new("RGB", image.size, (0, 0, 0))
        fondo.paste(image, (0,0), image)
        ascii_magic.from_pillow_image(fondo).to_terminal()
        print(data['name'])
        for type in data['types']:
            nombre_type = type['type']['name']
            print(f"  - Tipo: {nombre_type}")
        for stat in data['stats']:
            nombre_stat = stat['stat']['name']
            valor_stat = stat['base_stat']
            print(f"  - {nombre_stat}: {valor_stat}")
        respuesta = input('¿Deseas buscar otro pokemon? (s/n): ').strip().lower()
        if respuesta != 's':
            break

    elif response.status_code == 404:
        print('No existe el pokemon')
    else:
        print('Codigo:', response.status_code)

