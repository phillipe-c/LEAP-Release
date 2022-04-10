import os
import sys
try:
    import pyttsx3
    import wikipedia
    import argparse
except ModuleNotFoundError:
    pass

wikipedia.set_lang("pt")
search = []

def say(sentence):
    engine = pyttsx3.init()
    engine.say(str(sentence))
    engine.runAndWait()

wiki = wikipedia.summary(str(' '.join(sys.argv[1:])), sentences=6)
print(wiki)
