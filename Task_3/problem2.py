import random
import string

def generate_passsword (length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = "".join(random.choice(chars) for x in range(length) )
    return password

password = print(generate_passsword(8) )