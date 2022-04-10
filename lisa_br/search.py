
import os
import sys
from search_at_google import get_google_result
try:
    import pyttsx3
    import wikipedia
    import argparse
except ModuleNotFoundError:
    print("The Necessary Modules for this program were not found. Please install them")

wikipedia.set_lang("pt")
search = []
usr_choice = str(' '.join(sys.argv[1:]))

def answer(question):
    resp = get_google_result(question)
    if resp == None:
        try:
            resp = wikipedia.summary(question, sentences=2)
        except:
            try:
                if question != '':
                    from rss_feed_search import get_feed
                    resp = get_feed(query=question)
                else:
                    try:
                        from leds import GradLed
                        GradLed.error_msg_led()
                    except:
                        x=0
                    return 'Não foi possivel achar nenhum resultado da internet. Verifique se há uma conexão estável com a rede local (código de erro: no_mach_found_rss_search)'
            except:
                try:
                    from leds import GradLed
                    GradLed.error_msg_led()
                except:
                    x=0
                return 'Não foi possivel achar nenhum resultado da internet. Verifique se há uma conexão estável com a rede local (código de erro: no_mach_found_wiki_google_search)'
    return resp

print(answer(usr_choice))
