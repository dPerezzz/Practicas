import requests
import json

pokemon = input('Ingresa el nombre del pokemon: ').lower()


URL= f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
response = requests.get(URL)

if response.status_code == 200:
    print('Conexion exitosa')
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print('Error en la conexion')
    print('Codigo de error:', response.status_code)