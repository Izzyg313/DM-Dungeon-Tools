import requests

def get_spell(spell):
    url = f"https://www.dnd5eapi.co/api/spells/{spell}"
    response = requests.get(url)
    return response.json()