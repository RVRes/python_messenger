from datetime import datetime
import requests
from PyQt6 import QtWidgets, QtCore
import clientui


class MessengerUI(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.send_message)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

        self.after = 0  # время последнего сообщения, после которого выводим новые
        self.server_address = 'http://127.0.0.1:5000'

    def print_message(self, message):
        dt = datetime.fromtimestamp(message['time'])
        dt_str = dt.strftime('%d %b %H:%M:%S')
        self.textBrowser.append(dt_str + ' ' + message['name'])
        self.textBrowser.append(message['text'])
        self.textBrowser.append('')

    def get_messages(self):
        try:
            response = requests.get(self.server_address + '/messages',
                                    params={'after': self.after})
            messages = response.json()['messages']
        except:
            return

        for message in messages:
            self.print_message(message)
            self.after = message['time']

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        try:
            response = requests.post(
                self.server_address + '/send',
                json={'name': name, 'text': text}
            )
        except:
            self.textBrowser.append('Error - server post request failed')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append('Error - user data incorrect')
            self.textBrowser.append('')
            return

        self.textEdit.clear()


app = QtWidgets.QApplication([])
w = MessengerUI()
w.show()
app.exec()
