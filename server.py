import time
from flask import Flask, request, abort
from chatbot import bot_answer

app = Flask(__name__)
messages = [
    {
        'name': 'Jack',
        'text': 'А в нашем чате есть бот?',
        'time': 1614928868.9759247,
    },
    {
        'name': 'Mary',
        'text': 'Конечно! Попробуй отправить / в сообщении, чтобы поговорить с ним!',
        'time': 1614928869.9759247,
    }
]


def get_users_count():
    unique_users = []
    for message in messages:
        if not message['name'] in unique_users:
            unique_users.append(message['name'])
    return len(unique_users)


@app.route("/")
def hello():
    return "<b>Hello, World!<b>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Skillbox messenger ver.02 by Roman Reshetnikov',
        'time': time.time(),
        'users': get_users_count(),
        'messages': len(messages)
    }


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)

    name = data.get('name')
    text = data.get('text')

    if not isinstance(name, str) or len(name) == 0:
        return abort(400)
    if not isinstance(text, str) or \
            len(text) == 0 or len(text) > 1000:
        return abort(400)

    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    messages.append(message)

    # Вызываем бота по '/' в сообщении
    if message['text'].find('/') != -1:
        messages.append(
            {'name': 'ChatBot',
             'text': bot_answer(message['text']),
             'time': time.time()
             }
        )

    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    response = []
    for message in messages:
        if message['time'] > after:
            response.append(message)
    return {'messages': response[:50]}


app.run()
