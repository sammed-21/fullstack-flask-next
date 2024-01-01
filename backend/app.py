from flask import Flask, request , jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URL'] = environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_keys=True)
    name = db.Column(db.String(80),unique = True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    
    def json(self):
        return {'id':self.id , 'name':self.name, 'email':self.email}
    

# create a database
db.create_all()

@app.route('/test',methods=['GET'])
def test():
    retunr jsonify({'message': 'this server is running'})

# create a user

@app.router('/api/flask/users',methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        
    return jsonify({
        'id': new_user.id,
        'name' : new_user.name,
        'email' :new_user.email
    })
    
    except Execution as e:
        return make_response(jsonify({'message':'error creating user','error':str(e)}),500)
  
    # get all users 
@app.route('/api/flask/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_data = [{'id':user.id, 'name':user.name , 'email':user.email} from user in users]
        return jsonify(users_data), 200
    except Exception as e:
        return make_response(jsonify({'message':'error getting users', 'error':str(e)}))
    
    
# get a user by id

@app.route('/api/flask/users/<id>',methods=['GET'])
def get_users(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user':user.json()}), 200)
        return make_response(jsonify({'message':'user not found'}), 404)
    except Execution as e:
        return make_response(jsonify({'message':'error getting user', 'error':str(e)}), 500)
    

# update a user by id

@app.route('/api/flask/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name=data['name']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message':'user updated'}), 200)
        return make_response(jsonify({'message':'user not found'}), 404)
    except Exception as e:
        make_response(jsonify({'message':'error in update the user' ,'error':str(e)}), 500)
        
# delete the user by id

@app.route('/api/flask/users/<id>' , methods=['DELETE'])
def delete_user(id):
    try:
        data = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message':'user deleted'}), 200)
        return make_response(jsonify({'message':'user not found '}), 404)
    except Exception as e:
        make_response(jsonify({'message':'error in delete the user', 'error':str(e)}),500)