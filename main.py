from flask import Flask, render_template, request, url_for, redirect
import requests as rq
import re

def getPokemon(string):
  url = "https://pokeapi.co/api/v2/pokemon/" + string
  entry = rq.get(url)
  pokemon = ''
  if entry.status_code == 200:
  	pokemon = entry.json()
  	entry.close()
  return pokemon

def fixFlavor(string):
  editado = re.sub(r"\x0c", ' ', string)
  editado = editado.replace("\n"," ")
  return editado

def description(string):
  url = f"https://pokeapi.co/api/v2/pokemon-species/{string}"
  entry = rq.get(url)
  entrada = entry.json()
  entry.close()
  entradas = 0
  for i in range(len(entrada['flavor_text_entries'])-1):
    if entrada['flavor_text_entries'][i]['language']['name'] == 'en':
      entradas =  i
      break  
  text = entrada['flavor_text_entries'][entradas]['flavor_text']
  text = fixFlavor(text)
  return text

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])	
@app.route('/search',methods=['GET','POST'])
def find():
	if request.method == 'POST':
		pkmn = request.form['pokemon']
		return redirect(url_for("dex",pokemon=pkmn))
	else:
		return render_template('home.html')

@app.route("/<pokemon>",methods=['GET','POST'])
def dex(pokemon):
	if pokemon.lower() == 'deoxys':
		pokemon = 'deoxys-normal'
	pkm = getPokemon(pokemon.lower())
	if type(pkm) == dict:
		if request.method == 'POST':
			return redirect(url_for('find'))
		else:
			if pkm['name'] == 'deoxys-normal':
				pkm['name'] = 'deoxys'
			nome = pkm['name']
			desc = description(nome)
			return render_template('find.html',content=pkm,description=desc)
	else:
		return redirect(url_for('find'))
	 

if __name__ == "__main__":
	app.run(debug=True)