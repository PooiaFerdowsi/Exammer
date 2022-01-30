import sys, os

HELP_TEXT = open('README.md').read() # change it later
RIGHTS_TEXT = open('LICENSE').read()

FLASK_RUNAPP = 'flask runapp'

if len(sys.argv) <= 1:
    print("Actions:")
    print("[1]Run")
    print("[2]Help")
    print("[3]Rights")
    action = input("[?]1/2/3 enter 1 or 2 or 3")
    try:
        action = int(action) # raises ValueError if can't transdata to int
        if action < 1 or action > 3:
            raise ValueError
    except ValueError:
        print("Please enter 1 or 2 or 3 only!")
    else:
        if action == 1:
            os.system(FLASK_RUNAPP)
        else:
            print({2: HELP_TEXT, 3: RIGHTS_TEXT}.get(action))
elif sys.argv[1].lower() == 'runapp':
    os.system(FLASK_RUNAPP)
elif sys.argv[1].lower() == 'help':
    print(HELP_TEXT)
elif sys.argv[1].lower() == 'rights':
    print(RIGHTS_TEXT)
else:
    print(
        """something unexpectedly happened
        Use only:
            -[1]runapp
            -[2]help
            -[3]rights
        like: `py build.py runapp`
        or don't pass any argument""")
