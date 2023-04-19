from uzwords import words
from difflib import get_close_matches
#word1 = "тариҳ"
def CheckWord(word, words=words):
    matches = set(get_close_matches(word, words))
    available = False

    if word in words:
        matches = word
        available = True
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))
    return {'Available' : available, 'matches' : matches}
#print(CheckWord(word1))