from users import actions
# Main menu
print("""
    Available options:
        - Sign in (Press 1)
        - Log in (Press 2)
        - Exit (Type exit())
""")

do = actions.Actions()
action = input('What to do? ')

if action == '1':
    do.signIn()
elif action == '2':
    do.logIn()
elif action == 'exit()':
    print('Bye!')
else:
    print('Please, press 1, 2 or type exit() depending on your needs')
