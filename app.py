from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route racine
@app.route('/')
def hello_world():
    return 'Hello, World! This is my Flask application.'

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
