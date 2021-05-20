from PyInquirer import prompt, print_json, Separator

from cmd import Cmd

from auth import check_auth, auth, logout
from helpers import clearConsole, big_print, parse_flags

from models.user import User
from models.letter import show_letter_plot

from prettytable import PrettyTable

from PyInquirer import prompt
from questions.letter import q_address, q_recipient, q_create 


class MyPrompt(Cmd):
    prompt = '> '
    doc_header = "Доступные команды (введите help <тема>):"
    misc_header = "Разные разделы справки:"
    intro = "Введите help для просмотра списка команд"

    def preloop(self):
        big_print('Postal Logistics')
        user = check_auth()
        if user:
            big_print('Hi, '+user['full_name'])
            self.prompt = '{0}/{1}: '.format(user['role'], user['username'])
            self.user = User(**user)
        else:
            clearConsole()
            print('Неверные логин или пароль')
            self.preloop()

    def do_logout(self,inp):
        logout()
        self.prompt = '> '
        clearConsole()
        self.preloop()
    def help_logout(self):
        print('Выйти из аккаунта')

    def do_my_user_info(self, inp):
        print(self.user)
    def help_my_user_info(self):
        print('Вывод информации о текущем пользователе')

    def do_show_letters(self, inp):
        params = parse_flags(inp)
        # print('params', params)
        letters = self.user.get_letters()
        if not letters:
            print('Таблица писем - пуста')
        else:
            if params['plot']:
               show_letter_plot(letters) 
            else:
                x = PrettyTable()
                x.field_names = ["Идентификатор","Отправитель", "Адрес", "Отслеживание", "Статус", "Экспресс"]
                for i in letters:
                    x.add_row(i.get_data_from_table())
                print(x)
    def help_show_letters(self):
        print('\nОтобразить список писем. Доступные параметры:\n\t--plot {bool} - вывести график\n')

    def do_create_letter(self, inp):
        if self.user.role == 'user':
            print('У вас не достаточно прав')
            return False
        print('Отправитель:')
        recipient = prompt(q_recipient)
        print('Адрес:')
        address = prompt(q_address)
        print('Другое:')
        other = prompt(q_create)
        new_letter = self.user.create_letter(recipient, address, **other)
        print(new_letter)
    def help_create_letter(self):
        print('Создать письмо')

    def do_delete_letter(self, inp):
        params = parse_flags(inp)
        if not params['id']:
            print('Не задан Идентификатор')
        else:
            result = self.user.delete_letter(params['id'])
            if result: 
                print('\n\tПисьмо {0}, удалено\n'.format(params['id']))
            else:
                print('\n\tНе удалось удалить письмо {}\n'.format(params['id']))
    def help_delete_letter(self):
        print('\nУдалить письмо по id. Доступные параметры:\n\t--id {id} - идентификатор письма\n')

    def do_cls(self, inp):
        clearConsole()
    def help_cls(self):
        print('Очистить консоль')

    def do_exit(self, inp):
        return True
    def help_exit(self):
        print('Выход из приложения. Клавиши: Ctrl-D.')

    def default(self, inp):
        print("Default: {}".format(inp))

    def postloop(self):
        print("Пока 👋")

    do_EOF = do_exit
    help_EOF = help_exit

if __name__ == '__main__':
    MyPrompt().cmdloop()
