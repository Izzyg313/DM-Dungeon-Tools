from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from PIL import Image
import io

# This route will display the home page, which lists all saved users and provides a link to create new ones.
@app.route('/')
def show_home():
    users = User.get_all()
    return render_template('login.html', users=users)

# This route renders the HTML page to create a new user.
@app.route('/user/new')
def new_user():
    return render_template('user.html')

# This route handles the form submission to create a new user and save it to the database.
@app.route('/user/create', methods=['POST'])
def create_user():
    username = request.form['username']
    profile_picture = request.files['profile_picture']

    # Resize and compress the image
    image = Image.open(profile_picture)
    image = image.convert("RGB")

    # Resize the image to a maximum of 800x800 pixels
    max_size = (800, 800)
    image.thumbnail(max_size)

    # Save the image to a BytesIO object
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG', quality=85)
    img_byte_arr = img_byte_arr.getvalue()

    data = {
        'username': username,
        'profile_picture': img_byte_arr
    }
    User.new_user(data)
    return redirect('/')

@app.route('/user/login/<int:id>')
def login_user(id):
    session['id'] = id
    return redirect('/home')

@app.route('/user/logout')
def logout_user():
    if 'id' in session:
        session['id'] = None
    return redirect('/')