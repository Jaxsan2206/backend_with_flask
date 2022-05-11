from flask import Flask
from Models import usersModel

def index(req):
    fetchAll = usersModel.Users.getAll()
    return fetchAll, 200

def show(req, username):
    fetchUser = usersModel.Users.show(username)
    return fetchUser, 200


def create(req):
    new_user = req.get_json()
    createUser = usersModel.Users.create(new_user)
    return createUser, 201

def update(req, username):
    fetchUser = usersModel.Users.show(username)
    newData = req.get_json()
    updatedUser = usersModel.Users.update(fetchUser[0], newData)
    # print(updatedUser)
    return updatedUser, 203

def destroy(req, username):
    fetchUser = usersModel.Users.show(username)
    deletedUser = usersModel.Users.delete(fetchUser[0]['id'])
    print(type(fetchUser))
    return [{"message": "Deleted"}], 204

