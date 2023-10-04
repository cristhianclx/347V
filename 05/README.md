python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt --upgrade

flask --app main db init
flask --app main db migrate
flask --app main db upgrade

flask --app main shell

flask --app main run --reload


# definir rutas y posibles respuesta

/ => {"working": True}

/pokemon-by-name/<pikachu>/ => {
    "name": "pikachu",
    "height": 5kg,
    "abilities": ["electric"]
}