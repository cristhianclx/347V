from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy.sql import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

ma = Marshmallow(app)

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
    

class UserBasicSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = User


user_basic_schema = UserBasicSchema()
users_basic_schema = UserBasicSchema(many = True)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "age", "content")
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many = True)


class WorkingResource(Resource):
    def get(self):
        return {"working": True}


class PublicUserResource(Resource):
    def get(self):
        users_data = User.query.all()
        return users_basic_schema.dump(users_data)
    

class UserResource(Resource):
    def get(self):
        users_data = User.query.all()
        return users_schema.dump(users_data)
    
    def post(self):
        # request.form["data"] # send is in format application/form-data
        data_user = request.get_json() # send is in format json
        # {'name': 'Jesus', 'age': '33', 'id': '3'}
        user = User(**data_user)
        # user = User(id = data_user["id"], name=data_user["name"], age=data_user["age"])
        db.session.add(user)
        db.session.commit()
        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "created": user.created_at.strftime("%Y-%m-%d-%H:%M")
        }, 201


class UserByIDResource(Resource):

    def get(self, user_id):
        user = User.query.filter_by(id = user_id).first()
        # TODO: fix this
        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "created": user.created_at.strftime("%Y-%m-%d-%H:%M")
        }

    def patch(self, user_id):
        data_user = request.get_json()
        user = User.query.filter_by(id = user_id).first()
        user.name = data_user["name"]
        db.session.commit()
        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "created": user.created_at.strftime("%Y-%m-%d-%H:%M")
        }

    def delete(self, user_id):
        user = User.query.filter_by(id = user_id).first()
        db.session.delete(user)
        db.session.commit()
        return {}, 204


api.add_resource(WorkingResource, '/')
api.add_resource(PublicUserResource, '/public/users')
api.add_resource(UserResource, '/users')
api.add_resource(UserByIDResource, '/users/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=True)
