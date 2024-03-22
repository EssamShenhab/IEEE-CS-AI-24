import random
import string

chars = list(string.digits + string.ascii_letters)
random.shuffle(chars)
Password = "".join(chars[0:7])
print(Password)
