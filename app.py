from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL de la API de ejemplo
API_URL = 'https://jsonplaceholder.typicode.com/posts'

@app.route('/')
def index():
    # Hacer una solicitud a la API y obtener los datos
    response = requests.get(API_URL)
    data = response.json()

    # Renderizar una plantilla HTML y pasar los datos a la plantilla
    return render_template('index.html', posts=data)

if __name__ == '__main__':
    app.run(debug=True)
