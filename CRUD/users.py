from flask_restful import Resource, reqparse
from flask import jsonify
from model import UserModel

def make_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, required=True)
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    return parser

parser = make_parser()

class User(Resource):
    def get(self, id: int=None):
        if id: # if id is not None then it is /users/id
            user = UserModel.find_by_id(id)
            if user:
                return jsonify(user)
            return {"messge":"User dose not found"}
        
        else: # if id is None then it is /users
            users = UserModel.get_all_users()
            return jsonify({"Users":users})
        
    def delete(self, id: int):
        user = UserModel.find_by_id(id)
        if user:
            UserModel.delete_by_id(id)
            return {"message": "User deleted successfully"}
        return {"messge":"User dose not found"}
        
    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_id(data['id']):
            return {"message": "User already exist"}
        user = UserModel(**data)
        try:
            user.save_to_db()
            return {"message": "User added to database successfully"}
        except:
            return {'message' : 'internal database error'}
        
    def put(self, id: int):
        data = parser.parse_args()
        if id != data['id']:
            return {"message": "You can not change value of id"}
        user = UserModel(**data)
        if UserModel.find_by_id(id):
            user.update_information()
            return {"message": "User updated successfully"}
        try:
            user.save_to_db()
            return {"message": "User updated successfully"}
        except:
            return {'message' : 'internal database error'}
        

            