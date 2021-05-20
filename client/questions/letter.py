from helpers import is_not_empty

q_create = [
    {
        'type': 'confirm',
        'name': 'track',
        'message': 'Отслеживать?',
        'default': False,
    },
    {
        'type': 'confirm',
        'name': 'express',
        'message': 'Экспресс?',
        'default': False,
    },
]


q_recipient = [
    {
        'type': 'input',
        'name': 'first',
        'message': 'Имя',
        'validate': is_not_empty
    },
    {
        'type': 'input',
        'name': 'last',
        'message': 'Фамилия',
        'validate': is_not_empty
    },
    {
        'type': 'input',
        'name': 'middle',
        'message': 'Отчество',
        'validate': is_not_empty
    },
]

q_address = [
    {
        'type': 'list',
        'name': 'country',
        'message': 'Страна',
        'choices': ['Беларусь', 'Россия', 'США', 'Италия']
    },
    {
        'type': 'input',
        'name': 'city',
        'message': 'Город',
        'validate': is_not_empty
    },
    {
        'type': 'input',
        'name': 'district',
        'message': 'Район',
    },
    {
        'type': 'input',
        'name': 'street',
        'message': 'Улица',
        'validate': is_not_empty
    },
    {
        'type': 'input',
        'name': 'house_number',
        'message': 'Номер дома',
        'validate': is_not_empty
    },
    {
        'type': 'input',
        'name': 'postcode',
        'message': 'Почтовый индекс',
        'validate': is_not_empty
    },
]
