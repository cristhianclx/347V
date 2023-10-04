from flask import Flask, request
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)


class WorkingResource(Resource):
    def get(self):
        return {"working": True}


class PokemonResource(Resource):
    
    def get(self, name):
        raw = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(name))
        if raw.ok:
            data = raw.json()
            abilities = []
            for a in data["abilities"]:
                abilities.append(a["ability"]["name"]) 
            return {
                "name": data["name"],
                "height": data["height"],
                "abilities": abilities,
            }
        return {
            "error": "An error happened",
        }, 400


api.add_resource(WorkingResource, '/')
api.add_resource(PokemonResource, '/pokemon-by-name/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)

