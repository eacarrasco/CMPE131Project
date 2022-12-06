from app import myapp_obj, db
from app.models import User, Message

# Use this utility to create a new app.db and put some filler accounts and messages into it
# Note: This will delete all existing data in the database

myapp_obj.app_context().push()
db.drop_all()
db.create_all()

john = User(username='john', password='_')
john.set_password('pass123')

john_message = Message(contents='Hello, this is a test message', user_id=john.id)

john.favorite_messages.append(john_message)

db.session.add(john)
db.session.add(john_message)

# add other users and messages here

db.session.commit()