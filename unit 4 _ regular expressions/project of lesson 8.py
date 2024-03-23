import re

def is_email(email):

    the_email = re.search(r'^[A-Za-z0-9]+[\.-]?[a-zA-Z0-9]+@\w+\.\w{2,3}$', email)

    if the_email:
        print("Email is valid !")
    else:
        print("Email is not valid !")

is_email('heshamAbokamar015@gmail.com')