import requests as rq
import pokebase as pb
import re

def fixFlavor(string):
  editado = re.sub(r"\x0c", ' ', string)
  editado = editado.replace("\n"," ")
  return editado

def description(string):
  url = "https://pokeapi.co/api/v2/pokemon-species/" + string
  entry = rq.get(url)
  entry = entry.json()
  entrada = 0
  for i in range(len(entry['flavor_text_entries'])-1):
    if entry['flavor_text_entries'][i]['language']['name'] == 'en':
      entrada =  i
      break  
  text = entry['flavor_text_entries'][entrada]['flavor_text']
  text = fixFlavor(text)
  return text

def getPokemon(string):
  url = "https://pokeapi.co/api/v2/pokemon/" + string
  entry = rq.get(url)
  entry = entry.json()
  return entry

if __name__ == "__main__":
  a = input('Nome do pokemon:  ')
  getPokemon(a)
