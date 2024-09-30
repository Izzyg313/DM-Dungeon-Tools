from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Character:
    DB = 'DnD'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.race = data['race']
        self.characterClass = data['characterClass']
        self.level = data['level']
        self.hp = data['hp']
        self.tempHp = 0
        self.AC = data['AC']
        self.ability = {'str':data['str'],'dex':data['dex'],'con':data['con'],'wis':data['wis'],'int':data['int'],'cha':data['cha']}
        self.proficiency = {'athletics': data['athletics'], 'acrobatics':data['acrobatics'], 'sleight_of_hand':data['sleight_of_hand'], 'stealth':data['stealth'], 'arcana':data['arcana'], 'history':data['history'], 'investigation':data['investigation'], 'nature':data['nature'], 'religion':data['religion'], 'animal_handling':data['animal_handling'], 'insight':data['insight'], 'medicine':data['medicine'], 'perception':data['perception'], 'survival':data['survival'], 'deception':data['deception'], 'intimidation':data['intimidation'], 'performance':data['performance'], 'persuasion':data['persuasion']}
        self.bonus = self.get_proficiency(self.level)
        self.skills = self.get_skills(self.proficiency, self.bonus)
        self.other = data['other']
        self.user = []

    @classmethod
    def new_character(cls, data):
        query = """ INSERT INTO characters(user_id, name, race, characterClass, str, dex, con, wis, `int`, cha, hp, AC, athletics, acrobatics, sleight_of_hand, stealth, arcana, history, investigation, nature, religion, animal_handling, insight, medicine, perception, survival, deception, intimidation, performance, persuasion, level)
                    VALUES(%(user_id)s, %(name)s, %(race)s, %(characterClass)s, %(str)s, %(dex)s, %(con)s, %(wis)s, %(int)s, %(cha)s, %(hp)s, %(AC)s, %(athletics)s, %(acrobatics)s, %(sleight_of_hand)s, %(stealth)s, %(arcana)s, %(history)s, %(investigation)s, %(nature)s, %(religion)s, %(animal_handling)s, %(insight)s, %(medicine)s, %(perception)s, %(survival)s, %(deception)s, %(intimidation)s, %(performance)s, %(persuasion)s, %(level)s)
                """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, id):
        query = """ SELECT * FROM characters
                    WHERE id = %(id)s
                """
        data = {'id':id}
        result = connectToMySQL(cls.DB).query_db(query, data)[0]
        return result
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM characters"""
        results = connectToMySQL(cls.DB).query_db(query)
        characters = []
        for result in results:
            character = Character(result)
            characters.append(character)
        return characters

    @classmethod
    def update_characters(cls, data):
        query = """ UPDATE characters
                    SET name = %(name)s, race = %(race)s, characterClass = %(characterClass)s, str = %(str)s, dex = %(dex)s, con = %(con)s, wis = %(wis)s, int = %(int)s, cha = %(cha)s, hp = %(hp)s, temphp = %(temphp)s, AC = %(AC)s
                    WHERE id = %(id)s
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def delete_character(cls, id):
        query = """ DELETE FROM characters
                    WHERE id = %(id)s
                """
        data = {'id': id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    def get_proficiency(self, level):
        if level > 16:
            return 6
        elif level > 12:
            return 5
        elif level > 8:
            return 4
        elif level > 4:
            return 3
        else:
            return 2
    
    def get_skills(self, profs, bonus):
        skill_abilities = {
            'athletics': 'str', 'acrobatics': 'dex', 'sleight_of_hand': 'dex', 
            'stealth': 'dex', 'arcana': 'int', 'history': 'int', 
            'investigation': 'int', 'nature': 'int', 'religion': 'int', 
            'animal_handling': 'wis', 'insight': 'wis', 'medicine': 'wis', 
            'perception': 'wis', 'survival': 'wis', 'deception': 'cha', 
            'intimidation': 'cha', 'performance': 'cha', 'persuasion':'cha'
        }
        skills = []
        for skill, ability in skill_abilities.items():
            ability_score = self.ability[ability]
            modifier = (ability_score - 10) // 2
            base_skill = modifier 
            skills.append(base_skill + bonus if profs[skill] == 1 else base_skill)
        return skills