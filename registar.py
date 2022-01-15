import json

import requests
from config import REGISTAR_HOST, USERS_ENDPOINT


class User:

    def __init__(self, firstname, lastname, password, email, birthDate):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.email = email
        self.birthDate = birthDate


def user_add(user: User):
    user.birthDate = str(user.birthDate)
    headers = {'content-type': 'application/json'}
    requests.post(REGISTAR_HOST + USERS_ENDPOINT,
                  data=json.dumps(user.__dict__),
                  headers=headers)
