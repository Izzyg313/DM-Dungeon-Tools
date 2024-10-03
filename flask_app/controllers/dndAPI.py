from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import dndAPI

@app.route('/spell/<string:spell>')
def get_spell(spell):
    spell = dndAPI.get_spell(spell)
    return render_template('spell.html', spell = spell)

@app.route('/spell/search')
def find_spell():
    spells = dndAPI.all_spells()
    return render_template('spell_search.html', spells = spells)