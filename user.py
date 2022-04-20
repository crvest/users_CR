# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our databate
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # use class mehotd to query database
    @classmethod
    def get_all(cls):
        # store query variable
        query = "SELECT * FROM users;" 
        # connect to mysql with query from above
        results = connectToMySQL('users_schema').query_db(query)
        # initialize user list to store query data
        users = []
        # loop through the queried results and store them in the users list
        for user in results:
            users.append( cls(user) )
        # return the users list
        return users

    # save new user
    @classmethod
    def save_user(cls, data):
        # store query
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        # data is a dictionary that will be passed into create_user method from server.py
        return connectToMySQL('users_schema').query_db(query,data)