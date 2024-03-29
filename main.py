# importing
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialing Flask
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:arun12@localhost/Details'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initial db

db = SQLAlchemy(app)


# creating model/class
class Com(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    address = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    def _init_(self, email, username, address):
        self.email = email
        self.username = username
        self.address = address


# Routes
@app.route('/')
def home():
    return "Welcome to our API"


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if isinstance(data, list):
        # If data is a list, iterate through each item
        for user_data in data:
            new_user = Com(username=user_data['username'], email=user_data['email'], address=user_data['address'])
            db.session.add(new_user)

        db.session.commit()
        return jsonify({'MESSAGE': 'USERS CREATED SUCCESSFULLY'})
    else:
        # Handle the case when a single user is sent
        new_user = Com(username=data['username'], email=data['email'], address=data['address'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'MESSAGE': 'USER CREATED SUCCESSFULLY'})


@app.route('/users', methods=['GET'])
def get_all_users():
    users = Com.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'address': user.address} for user in users]
    return jsonify({'users': user_list})


# GET method to retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = Com.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email, 'address': user.address})
    return jsonify({'MESSAGE': 'USER NOT FOUND'}), 404


# PUT method to update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Com.query.get(user_id)
    if user:
        data = request.get_json()
        user.email = data['email']
        user.username = data['username']
        db.session.commit()
        return jsonify({'MESSAGE': 'USER UPDATED SUCCESSFULLY'})
    return jsonify({'MESSAGE': 'USER NOT FOUND'}), 404


# DELETE method to delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Com.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return {'MESSAGE': f'User with ID {user_id} DELETED SUCCESSFULLY'}
    else:
        return {'ERROR': 'USER NOT FOUND'}, 404


# Run
if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        app.run(debug=True)# importing
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialing Flask
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:arun12@localhost/Details'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initial db

db = SQLAlchemy(app)


# creating model/class
class Com(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    address = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    def _init_(self, email, username, address):
        self.email = email
        self.username = username
        self.address = address


# Routes
@app.route('/')
def home():
    return "Welcome to our API"


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if isinstance(data, list):
        # If data is a list, iterate through each item
        for user_data in data:
            new_user = Com(username=user_data['username'], email=user_data['email'], address=user_data['address'])
            db.session.add(new_user)

        db.session.commit()
        return jsonify({'MESSAGE': 'USERS CREATED SUCCESSFULLY'})
    else:
        # Handle the case when a single user is sent
        new_user = Com(username=data['username'], email=data['email'], address=data['address'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'MESSAGE': 'USER CREATED SUCCESSFULLY'})


@app.route('/users', methods=['GET'])
def get_all_users():
    users = Com.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'address': user.address} for user in users]
    return jsonify({'users': user_list})


# GET method to retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = Com.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email, 'address': user.address})
    return jsonify({'MESSAGE': 'USER NOT FOUND'}), 404


# PUT method to update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Com.query.get(user_id)
    if user:
        data = request.get_json()
        user.email = data['email']
        user.username = data['username']
        db.session.commit()
        return jsonify({'MESSAGE': 'USER UPDATED SUCCESSFULLY'})
    return jsonify({'MESSAGE': 'USER NOT FOUND'}), 404


# DELETE method to delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Com.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return {'MESSAGE': f'User with ID {user_id} DELETED SUCCESSFULLY'}
    else:
        return {'ERROR': 'USER NOT FOUND'}, 404


# Run
if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        app.run(debug=True)