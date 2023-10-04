from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
app.debug = True

migrate = Migrate(app, db)

api = Api(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<User {self.id}>"
    

class WorkingResource(Resource):
    def get(self):
        return {"working": True}


class UserResource(Resource):
    def get(self):
        users_data = User.query.all()
        users_results = []
        for user_data in users_data:
            users_results.append({
                "id": user_data.id,
                "name": user_data.name,
                "age": user_data.age,
                "created": user_data.created_at.strftime("%Y-%m-%d-%H:%M"), # datetime()
            })
        return users_results
    
    def post(self):
        print(request.get_json()) # send is in format json
        # request.form["data"] # send is in format application/form-data
        return {}, 201


api.add_resource(WorkingResource, '/')
api.add_resource(UserResource, '/users')


if __name__ == '__main__':
    app.run(debug=True)