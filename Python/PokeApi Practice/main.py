from PIL import Image
import requests
from io import BytesIO


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
        # spriteURL = data['sprites']['front_default']
        # image_response = requests.get(spriteURL)
        # image = Image.open(BytesIO(image_response.content))
        # image = image.convert("RGBA")
        # image.show()
        # print(data['name'])
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

