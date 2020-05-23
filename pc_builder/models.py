from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
from flask import jsonify
import os
import uuid

graph = Graph("bolt://localhost:7687", auth=("neo4j", "test"))


class User:
    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.run(
            "MATCH (n:User { username: '%s'} ) RETURN n" % self.username
        ).data()
        return user

    def register(self, password, first_name, last_name, email):
        if not self.find():
            user = Node(
                "User",
                username=self.username,
                password=bcrypt.encrypt(password),
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            graph.create(user)
            return True
        else:
            return False

    def verify_password(self, password):
        user = self.find()
        if user:
            return bcrypt.verify(password, user[0]["n"]["password"])
        else:
            return False
