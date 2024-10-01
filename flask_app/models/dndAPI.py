import requests
from flask_app import app

def get_spell(spell):
    url = f"https://www.dnd5eapi.co/api/spells/{spell}"
    response = requests.get(url)
    return response.json()

def all_spells():
    url = "https://www.dnd5eapi.co/api/spells"
    response = requests.get(url)
    return response.json()