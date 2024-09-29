from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Monster:
    DB = 'DnD'
    def __init__(self, data):
        self.id = data['id']
        self.xp = data['xp']
        self.hp = data['hp']
        self.ac = data['ac']
        self.name = data['name']
        self.actions = data['actions']
        self.stats = {'str':data['str'], 'dex':data['dex'], 'con':data['con'], 'wis':data['wis'], 'int':data['int'], 'cha':data['cha']}