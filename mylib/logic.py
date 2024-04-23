import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    "This is a wikipedia fetcher"

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    "This functions searches the name"
    result = wikipedia.search(name)
    return result


def phrase(name):
    "Returns phrases from Wikipedia"
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
