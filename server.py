from flask_app.controllers import characters, users, dndAPI
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True, port=8080)