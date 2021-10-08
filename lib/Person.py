class Person:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password
