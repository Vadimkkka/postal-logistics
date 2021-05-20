from helpers import is_not_empty

questions = [
    {
        'type': 'confirm',
        'name': 'have_account',
        'message': ' У вас уже есть аккаунт?',
        'default': True,
    },
    {
        'type': 'input',
        'name': 'username',
        'message': 'Имя пользователя',
        'validate': is_not_empty
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'Пароль'
    },
    {
        'type': 'input',
        'name': 'full_name',
        'message': 'Полное имя',
        'when': lambda answers: answers['have_account'] == False
    },

]
