import requests
import random
import datetime
from registar import User

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()


def generate_user(domain):
    first = str(WORDS[random.randint(0, 10000)].decode("utf-8"))[:8]
    second = str(WORDS[random.randint(0, 10000)].decode("utf-8"))[:8]
    third = str(WORDS[random.randint(0, 10000)].decode("utf-8"))
    day = random.randint(1, 27)
    month = random.randint(1, 12)
    year = random.randint(1960, 2002)
    birthDate = datetime.date(year, month, day)
    email = ("" + first + "." + second + "." + third)[:20] + str(year) + "@" + domain
    return User(first, second, second + "." + first, email, birthDate)
