import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dfa8e94137401109777b5224e0e46c58'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5270'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
