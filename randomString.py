from string import *
from random import *
characters = ascii_letters + punctuation  + digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print(password)