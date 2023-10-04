from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class WorkingResource(Resource):
    def get(self):
        return {"working": True}


class PokemonResource(Resource):
    # https://pokeapi.co/
    # requests
    def get(self, name):
        return {
            "name": "pikachu",
            "height": "5",
            "abilities": ["electric"]
        }


api.add_resource(WorkingResource, '/')
api.add_resource(PokemonResource, '/pokemon-by-name/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)

