import getpass
import users.user as userModel
# logic from class Note needed to be able to use note's methods in nextAction method
import notes.actions as noteAction

class Actions:

    def signIn(self):
        print('Please, write your data in fields below\n')
        name = str(input("What's your name? "))
        surname = str(input("What's your surname? "))
        email = str(input("Type an email "))
        password = getpass.getpass(prompt="Type a password: ")

        user = userModel.User(name, surname, email, password)
        signIn = user.register()  # returns 1 if user have been registered or 0 if not

        if signIn[0] >= 1:
            print(f'\n{signIn[1].name} have been registered')
        else:
            print('\nSomething went wrong. You have not been registered')

    def logIn(self):
        print('Please, identify yourself\n')
        try:
            email = str(input("Type your email "))
            password = getpass.getpass(prompt="Type your password: ")

            user = userModel.User('', '', email, password)
            logIn = user.identify()

            if email == logIn[3]:
                print(f'\nWelcome {logIn[1]}!')
                self.nextActions(logIn)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f'Failed to log in!')

    def nextActions(self, user):
        print("""
            Available actions:
                - New note (new)
                - Show notes (show)
                - Delete note (delete)
                - Exit (exit)
        """)

        action = input('What to do? ')
        do = noteAction.Actions()

        if action == 'new':
            do.create(user)
            self.nextActions(user)
        elif action == 'show':
            do.show(user)
            self.nextActions(user)
        elif action == 'delete':
            do.delete(user)
            self.nextActions(user)
        elif action == 'exit':
            exit()
        else:
            print('Type an existing option')

