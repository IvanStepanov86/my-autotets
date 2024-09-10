import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dfa8e94137401109777b5224e0e46c58'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

BODY_CREATE = {
    "name": "generate",
    "photo_id": -1
}
BODY_CONFIRM = {
    "trainer_token": TOKEN
}
BODY_CHANGE = {
    "pokemon_id": "69250",
    "name": "generate",
    "photo_id": -1
}
BODY_CATCH = {
    "pokemon_id": "69250"
}

RESPONSE_CREATE = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(RESPONSE_CREATE.text)
MESSAGE = RESPONSE_CREATE.json()['id']
print(MESSAGE)

'''RESPONSE_CHANGE = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(RESPONSE_CHANGE.text)'''

'''RESPONSE_CATCH = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CATCH)
print(RESPONSE_CATCH.text)'''

