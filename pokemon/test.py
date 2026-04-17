import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

payload = {}
headers = {}

respuesta = requests.get(url)




# response = requests.request("GET", url, headers=headers, data=payload)

print(respuesta.text)
