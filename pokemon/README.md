# pokemon
Integrantes: 
Efraín Mendoza Alemán 5465
Anna Sofia Plazas Oyervides 6993
Stephany Alejandra Guerrero Peña 6966

Concepto que se aplicó:

Obtiene los detalles de un Pokémon individual.

API usada: PokéAPI (https://pokeapi.co/api/v2/pokemon/{id_o_nombre})

Retorna: nombre, altura, peso, imagen, tipos e ID.

2. pokemon_by_type(type_name) - La que preguntas
Obtiene 10 Pokémon de un tipo específico (Fuego, Agua, Eléctrico, etc.)
API usada: PokéAPI endpoint de tipos (https://pokeapi.co/api/v2/type/{tipo})

Funciona así:
Consulta el tipo (ej: "fire", "water")
Obtiene la lista de Pokémon de ese tipo
Toma los primeros 10
Obtiene detalles de cada uno llamando a get_pokemon_details()

3. random_pokemon()
Genera un número aleatorio entre 1 y 1025
Obtiene ese Pokémon con get_pokemon_details()

Todas utilizan PokéAPI v2