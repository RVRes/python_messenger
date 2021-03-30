from pprint import pprint
import time

print('https://repl.it/@levashov/messenger')
print(time.time())

messages = [
    {
        'name': 'Jack',
        'text': 'Привет всем, я Jack',
        'time': 1614928868.9759247,
    },
    {
        'name': 'Mary',
        'text': 'Привет Jack, я - Mary',
        'time': 1614928869.9759247,
    }
]


def send_message(name, text):
    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    messages.append(message)


def get_messages(after):
    response = []
    for message in messages:
        if message['time'] > after:
            response.append(message)
    return response[:50]


response = get_messages(0)
pprint(response)
print()

after = response[-1]['time']

response = get_messages(after)
pprint(response)
print()

response = get_messages(after)
pprint(response)
print()

send_message('Jack', '1')
send_message('Jack', '2')

response = get_messages(after)
pprint(response)
print()
