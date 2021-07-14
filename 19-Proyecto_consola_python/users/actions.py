import getpass

class Actions:

    def signIn(self):
        print('Please, write your data in fields below\n')
        name = str(input("What's your name? "))
        surname = str(input("What's your surname? "))
        email = str(input("Type an email "))
        password = getpass.getpass(prompt="Type a password: ")

    def logIn(self):
        print('Please, identify yourself\n')
        email = str(input("Type your email "))
        password = getpass.getpass(prompt="Type your password: ")    