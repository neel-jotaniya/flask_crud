import pymongo
import os

client = pymongo.MongoClient(os.environ.get('CONNECTION_STRING'))
db = client["flask_crud"]
collection = db["project1"]

class UserModel:
    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id 
        self.name = name
        self.email = email
        self.password = password
        
    def json(self) -> dict:
        return {'id': self.id, 'name': self.name, 'email': self.email, 'password': self.password}
    
    @classmethod
    def find_by_id(cls, id: int):
        myquery = {'id': id}
        user = collection.find_one(myquery)
        if user:
            del user['_id']
        return user

    @classmethod
    def delete_by_id(cls, id: int):
        myquery = {'id': id}
        collection.delete_one(myquery)
        
    def save_to_db(self):
        collection.insert_one(self.json())
        
    def update_information(self):
        new_values = {'$set': self.json()}
        collection.update_one({'id': self.id}, new_values)

    @classmethod
    def get_all_users(cls):
        users = collection.find({}, {'_id': False})
        return list(users)
        
        
      