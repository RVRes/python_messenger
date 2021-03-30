import random
import requests
from datetime import datetime

server_address = 'http://127.0.0.1:5000/'

def bot_getcommand(message):
    command = message.split('/')[1].split(' ')[0]
    return command


def bot_say_error():
    return 'Команда написана с ошибкой. Введите /help для списка команд'

#Видимость команд ограничена только данным модулем
#поэтому в проверке команды в списке необходимости нет
def bot_answer(message):
    command = bot_getcommand(message)
    try:
        f = globals()[command]
        answer = f()
    except:
        answer = bot_say_error()
    return answer


def help():
    bot_commands = [
        {
            'name': 'about',
            'description': 'Показать версию и производителя ПО.'
        },
        {
            'name': 'date',
            'description': 'Показать текущую дату.'
        },
        {
            'name': 'hello',
            'description': 'Здороваемся на разных языках.'
        },
        {
            'name': 'help',
            'description': 'Вывести список доступных команд в чат.'
         },
        {
            'name': 'messages',
            'description': 'Показать количество сообщений в чате.'
        },
        {
            'name': 'time',
            'description': 'Показать текущее время.'
        },
        {
            'name': 'users',
            'description': 'Показать количество уникальных пользователей.'
        }
    ]
    answer = 'Вас приветсвутет Бот мессенджера SkillBox!\n' \
             + 'Это самый перспективный прокект по чатостроению в Мире!\n\n' \
             + 'Список доступных команд:\n'
    for cmd in bot_commands:
        cmd_str = '/'+cmd['name']+'  -  '+cmd['description']+'\n'
        answer += cmd_str
    return answer


def hello():
    greetings = [
        'Привет!',
        'Добрый день!',
        'Hi',
        'Hello',
        'Hola',
        'Ни-хао',
        'Здоровэньки булы!'
    ]
    answer = random.choice(greetings)
    return answer


def time():
    dt = datetime.now()
    answer = dt.strftime('%H:%M:%S')
    return answer


def date():
    dt = datetime.now()
    answer = dt.strftime('%d %b %y')
    return answer


def users():
    response = requests.get(server_address+'status')
    answer = response.json()['users']
    return answer


def messages():
    response = requests.get(server_address+'status')
    answer = response.json()['messages']
    return answer


def about():
    response = requests.get(server_address+'status')
    answer = response.json()['name']
    return answer
