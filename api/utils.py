import random
import re
from typing import List

import requests


def get_word():
    # Words that can be selected in the game
    words = get_words()
    # Choose a random word
    return random.choice(words)


def get_words() -> List[str]:
    url = 'https://www.getrandomthings.com/data/random-russian-words.php'
    data = {"num": 6, "add": "address", "unique": True}
    resp = requests.post(url, data=data)
    html = resp.content.decode()

    pattern = r"<div class='col-md-6 pt'>(.*?)<span class='sdes'> \* (.*?)</span>"
    matches = re.findall(pattern, html, re.DOTALL)
    search = [re.sub("<.*?>", "", match[0]) for match in matches if "noun" in match[1]]
    if not search:
        return get_words()
    return search
