from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import dndAPI

@app.route('/monster/<str:spell>')
def get_monster(spell):
    spell = dndAPI.get_spell(spell)
    return render_template('spell.html', spell = spell)