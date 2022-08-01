import secrets
import string
import sys


def get_password():
    try:
        length = int(sys.argv[1])
    except IndexError:
        return 'Please enter int arg'
    except ValueError:
        return 'Please enter int'
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


print(get_password())
