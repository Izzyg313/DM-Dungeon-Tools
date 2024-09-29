from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.character import Character
from flask_app.models.user import User

@app.route('/home')
def display_home():
    if 'id' in session:
        user = User.get_one(session['id'])
        return render_template('home.html', user=user, characters = Character.get_all())
    return redirect('/')

@app.route('/character/new')
def new_character():
    user = User.get_one(session['id'])
    return render_template('new.html', user=user)

@app.route('/character/create', methods=['POST'])
def create_character():
    Character.new_character(request.form)
    return redirect('/home')

@app.route('/character/show/<int:id>')
def show_character(id):
    character = Character.get_one(id)
    print(character['skills'])
    return render_template('show.html', character = character)

@app.route('/character/combat')
def generate_combat():
    return render_template('combat.html')

@app.route('/character/party/<int:id>')
def add_party(id):
    session['party'].append(Character.get_one(id))