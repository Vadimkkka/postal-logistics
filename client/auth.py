from PyInquirer import prompt
from questions.auth import questions

from configparser import ConfigParser
import requests

#Get the configparser object
config = ConfigParser()
config.read("config.ini")

def auth():
    answers = prompt(questions)
    result = None

    if answers['have_account']:
        result = sign_in(answers['username'], answers['password'])
    else:
        result = sign_up(answers['username'], answers['password'], answers['full_name'])

    if not result:
       return False

    config["USERINFO"] = result
    with open('config.ini', 'w') as conf:
        config.write(conf)
    return result

def check_auth():
    try:
        userinfo = config["USERINFO"]
        result = get_me(userinfo['access_token'])
        if not result:
            raise Exception('Not valid token')
        result['access_token'] = userinfo['access_token']
        config["USERINFO"] = result
        with open('config.ini', 'w') as conf:
            config.write(conf)
        return result
    except Exception as ex:
        return auth()



def logout():
    del config["USERINFO"]
    with open('config.ini', 'w') as conf:
        config.write(conf)

def get_me(token):
    headers = { 'Authorization': 'Bearer {0}'.format(token) }
    resp = requests.get('http://127.0.0.1:8000/users/me', headers=headers)
    if resp.status_code == 200:
        result = resp.json()
        return result
    else:
        return False

def sign_in(username, password):
    data = { 'username': username, 'password': password }
    resp = requests.post('http://127.0.0.1:8000/users/sign-in', data=data)
    if resp.status_code == 200:
        result = resp.json()
        token = result['access_token']
        # FIXME  Вынести отдельно
        result = get_me(token)
        result['access_token'] = token
        return result
    else:
        return False

def sign_up(username, password, full_name):
    data = { 'username': username, 'password': password, 'full_name': full_name }
    resp = requests.post('http://127.0.0.1:8000/users/sign-up', json=data)
    if resp.status_code == 201:
        result = sign_in(data['username'], data['password'])
        return result
    else:
        return False
