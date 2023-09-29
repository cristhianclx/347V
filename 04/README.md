flask --app main db init
flask --app main db migrate
flask --app main db upgrade

flask --app main shell

>>> from main import db, User, Message
>>> user_1 = User(id = 1, name="Cristhian", age=33)
>>> user_2 = User(id = 2, name="Genaro", age=34)
>>> db.session.add(user_1)
>>> # 
>>> db.session.add(user_2)
>>> # 
>>> db.session.commit()

flask --app main run --reload

>>> from main import db, User, Message
>>> user_3 = User.query.filter_by(id = 3).first()
>>> db.session.delete(user_3)
>>> db.session.commit()

>>> from main import db, User, Message
>>> user_1 = User.query.filter_by(id = 1).first() # not needed
>>> message = Message(id = 1, content="<b><i>This is a message</i><b>", user_id=1)
>>> db.session.add(message)
>>> db.session.commit()

>>> from main import db, User, Message
>>> user_1 = User.query.filter_by(id = 1).first()
>>> user_1.name = "Cristhian's"
>>> db.session.commit()
