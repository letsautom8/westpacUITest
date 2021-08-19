import random
import string


class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.firstname = ''
        self.lastname = ''

    def valid(self):
        text = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        text = text + ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
        text = text + ''.join(random.choice(string.punctuation) for _ in range(2))
        text = text + ''.join(random.choice(string.digits) for _ in range(2))
        self.username = ''.join(random.choice(string.ascii_uppercase ) for _ in range(6))
        self.password = text
        self.firstname = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        self.lastname = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

    def invalid_nolower(self):
        text = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        text = text + ''.join(random.choice(string.punctuation) for _ in range(3))
        text = text +''.join(random.choice(string.digits) for _ in range(1))
        self.username = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        self.password = text
        self.firstname = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        self.lastname = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

    def change_password(self):
        text = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        text = text + ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
        text = text + ''.join(random.choice(string.punctuation) for _ in range(2))
        text = text + ''.join(random.choice(string.digits) for _ in range(2))
        self.password = text
        return text