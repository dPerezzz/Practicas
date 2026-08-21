import requests

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
    print(data['name',data['stats']])
    break
elif response.status_code == 404:
    print('No existe el pokemon')
else:
    print('Codigo:', response.status_code)

