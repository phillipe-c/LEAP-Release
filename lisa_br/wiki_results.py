import os
import sys
try:
    import pyttsx3
    import wikipedia
    import argparse
except ModuleNotFoundError:
    print("The Necessary Modules for this program were not found. Please install them")

search = []
def say(sentence):
    engine = pyttsx3.init()
    engine.say(str(sentence))
    engine.runAndWait()

wiki = wikipedia.search(str(' '.join(sys.argv[1:])))
print(wiki)