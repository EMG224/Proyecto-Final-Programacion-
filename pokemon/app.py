from flask import Flask, render_template, request, redirect, url_for
import requests
import random

app = Flask(__name__)

def get_pokemon_details(pokemon_id_or_name):
    """Obtiene los detalles de un Pokémon de la API"""
    try:
        api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return {
                'name': data['name'].capitalize(),
                'height': data['height'] / 10,
                'weight': data['weight'] / 10,
                'image': data['sprites']['other']['official-artwork']['front_default'],
                'types': [t['type']['name'].capitalize() for t in data['types']],
                'id': data['id']
            }
    except:
        pass
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon_data = None
    error = None
    search_query = request.form.get('search_query', 'pikachu').lower().strip()

    if request.method == 'POST' and request.form.get('search_query'):
        search_query = request.form.get('search_query').lower().strip()

    pokemon_data = get_pokemon_details(search_query)
    if pokemon_data is None and search_query != 'pikachu':
        error = "Pokémon no encontrado. ¡Intenta con otro nombre o ID!"

    return render_template('index.html', pokemon=pokemon_data, error=error)

@app.route('/random')
def random_pokemon():
    """Obtiene un Pokémon aleatorio"""
    try:
        random_id = random.randint(1, 1025)
        pokemon_data = get_pokemon_details(random_id)
        if pokemon_data:
            return render_template('index.html', pokemon=pokemon_data, error=None)
    except:
        pass
    return render_template('index.html', pokemon=None, error="No se pudo obtener un Pokémon aleatorio")

@app.route('/type/<type_name>')
def pokemon_by_type(type_name):
    """Obtiene Pokémon de un tipo específico"""
    try:
        api_url = f'https://pokeapi.co/api/v2/type/{type_name.lower()}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            pokemons = data['pokemon'][:10]  # Primeros 10
            pokemon_list = []
            for p in pokemons:
                pokemon = get_pokemon_details(p['pokemon']['name'])
                if pokemon:
                    pokemon_list.append(pokemon)
            return render_template('type.html', type_name=type_name.capitalize(), pokemons=pokemon_list, error=None)
    except:
        pass
    return render_template('type.html', type_name=type_name, pokemons=[], error=f"Tipo '{type_name}' no encontrado")

if __name__ == '__main__':
    app.run(debug=True, port=5000)