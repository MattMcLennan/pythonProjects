import json
from difflib import get_close_matches


def load_data():
    return json.load(open("data.json"))


def formatDefinition(definitions):
    return '\n'.join(definitions)


def getWordDefinition(word):
    word = word.lower()
    if word in data:
        return formatDefinition(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        suggested_word = get_close_matches(word, data.keys())[0]
        retry_suggested_word = input(
            "Did you mean %s instead? Enyer Y if Yes, or N if no" % suggested_word)
        if retry_suggested_word == "Y":
            return formatDefinition(data[word])
        elif retry_suggested_word == "N":
            return "We didn't understand your entry"
        else:
            return "The word doesn't exist. Please double check it."
    else:
        return "The word doesn't exist. Please double check it."


data = load_data()
word = input("Enter a word: ")

print(getWordDefinition(word))
