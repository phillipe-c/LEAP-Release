import os
import sys
from rss_feed_search import get_feed
try:
    import pyttsx3
    import wikipedia
    import argparse
except ModuleNotFoundError:
    print("The Necessary Modules for this program were not found. Please install them")

search = []
usr_choice = str(' '.join(sys.argv[1:]))

def answer_rss(question):
    resp = get_feed(query=question)
    if resp == None:
        from leds import GradLed
        GradLed.error_msg_led()
        return 'Não foi possivel achar nenhum resultado da internet. Verifique se há uma conexão estável com a rede local'
    else:
        return resp

print(answer_rss(usr_choice))