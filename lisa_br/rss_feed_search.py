
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  LISA RSS Feed Service (RFS)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

try:    
    import feedparser
    import webbrowser
    import xml.etree.cElementTree as ET
    from xml.dom import minidom
    import sys
    import random
except:
    print('the necessary modules were not found, please install them')

feed_bbc = feedparser.parse ('http://www.bbc.co.uk/portuguese/index.xml')
feed_est = feedparser.parse ('https://brasil.estadao.com.br/blogs/vencer-limites/feed/')
feed_est = feedparser.parse ('https://brasil.estadao.com.br/feed/')

random_rss_choose = ['https://feeds.folha.uol.com.br/ambiente/rss091.xml', 'https://brasil.estadao.com.br/blogs/vencer-limites/feed/', 'https://feeds.folha.uol.com.br/mundo/rss091.xml',
                     'https://feeds.folha.uol.com.br/poder/rss091.xml', 'https://feeds.folha.uol.com.br/educacao/rss091.xml', 'https://feeds.folha.uol.com.br/ciencia/rss091.xml',
                     'https://feeds.folha.uol.com.br/comida/rss091.xml', 'https://feeds.folha.uol.com.br/tec/rss091.xml', 'https://feeds.folha.uol.com.br/emcimadahora/rss091.xml',
                     'https://feeds.folha.uol.com.br/mercado/rss091.xml']

rss_bbc_rand = ['http://www.bbc.co.uk/portuguese/index.xml', 'http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml', 'http://www.bbc.co.uk/portuguese/topicos/economia/',
                'http://www.bbc.co.uk/portuguese/topicos/saude/', 'http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/', 'http://www.bbc.co.uk/portuguese/topicos/cultura/']

else_mist_rss_link = ['https://brasil.estadao.com.br/blogs/vencer-limites/feed/']
total_rss = else_mist_rss_link + rss_bbc_rand + random_rss_choose
total_feed = rss_bbc_rand + else_mist_rss_link

def random_rss_feed():
    random_rss = random.choice(total_feed)
    #print(random_rss)
    feed_choosen = feedparser.parse (str(random_rss))
    return feed_choosen

def prettify(elem):

    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

root = ET.Element('root')

def search_rss(link, numbers_of_news, x=0):
    for story in link.entries:
        x+=1
        item = ET.SubElement(root,'item')
        title = ET.SubElement(item,'title')
        title.text = story.title
        # why doesn't pubDate work?
        description = ET.SubElement(item,'description')
        description.text = story.description
        link = ET.SubElement(item,'link')
        link.text = story.link
        #print(story.keys())
        #print(prettify(root))
        stor = story['description']
        #pub = story['published']
        return ("\n" + story['description'] + "\n")

def get_feed(query='', numbers_of_news=3):
    if query != '':
        query = query.replace(' ', '+') # Replaces the spaces with '+' so that it becomes a undestandable link
        #query = query.replace('+', '%2B')
        link= feedparser.parse ('https://www.bing.com/search?q='+ str(query) + '&format=rss&adlt=strict')
        #link= feedparser.parse ('https://news.google.com/rss/search?q='+ str(query))
        #print(link)
        return search_rss(link, numbers_of_news)
    else:
        news = search_rss(random_rss_feed(), numbers_of_news)
        while news == None:
            news = search_rss(random_rss_feed(), numbers_of_news)
            if news != None:
                break
            else:
                news = search_rss(random_rss_feed(), numbers_of_news)
                if news != None:
                    break
        return news

def print_rss(query):
    if query != '':
        return get_feed(query=query)
    else:
        return get_feed()