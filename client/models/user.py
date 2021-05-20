import requests
from models.letter import Letter

class User:
    def __init__(self, _id, username, full_name, role, disabled, access_token, hashed_password):
        self._id = _id
        self.username = username
        self.full_name = full_name
        self.role = role
        self.disabled = disabled
        self.access_token = access_token

    def __str__(self):
        return "\n\tИмя пользователя: {0}\n\tПолное имя: {1}\n\tРоль: {2}\n".format(self.username, self.full_name, self.role)

    def get_letters(self):
        headers = { 'Authorization': 'Bearer {0}'.format(self.access_token) }
        resp = requests.get('http://127.0.0.1:8000/letters', headers=headers)
        if resp.status_code == 200:
            result = resp.json()
            letters = []
            for i in result:
                letters.append(Letter(**i))
            return letters
        else:
            return False

    def create_letter(self, recipient, address, track=None, express=None):
        headers = { 'Authorization': 'Bearer {0}'.format(self.access_token) }
        data = { 'recipient': recipient, 'address': address, 'track':track, 'express': express }
        resp = requests.post('http://127.0.0.1:8000/letters', headers=headers, json=data)
        if resp.status_code == 201:
            return Letter(**resp.json())
        else:
            return False
        
    def delete_letter(self, letter_id ):
        headers = { 'Authorization': 'Bearer {0}'.format(self.access_token) }
        resp = requests.delete('http://127.0.0.1:8000/letters/{}'.format(letter_id), headers=headers)
        if resp.status_code == 204:
            return True
        else:
            return False
