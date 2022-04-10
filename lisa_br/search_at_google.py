
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  In Search Code
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

# We first import the modules.
import requests
from bs4 import BeautifulSoup
from requests.api import get

# Here is our main function
def get_google_result(query):
    
    # We get our input and make it undestandable for Google
    query = query.replace('+', '%2B') # In case there's any "+" in the query
    query = query.replace(' ', '+') # Replaces the spaces with '+'

    # We initialize the browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

    # Here is the link that we can enter anything to search
    r = requests.get('https://www.google.com/search?q=' + query, headers=headers)

    # We specify how the results should be saved
    soup = BeautifulSoup(r.text, 'lxml')

    # Information containing the standard location on google's website to where the snippets are
    outras_classes = ['wwUB2c PZPZlf', '2ahUKEwjo9o270cbsAhVOIbkGHdOBCfYQ2kooAjAmegQIMRAM', 
                      '2ahUKEwi-luuzysbsAhVzHbkGHQhMCqcQ2kooAjAeegQIMRAM', 'zloOqf PZPZlf', 
                      'LrzXr', 'aCOpRe', 'HwtpBd gsrt PZPZlf', 'yxAsKe', 'vXQmIe gsrt','rpnBye'] 
    
    # Classes 'zloOqf PZPZlf', 'LrzXr' for location

    # These are the main classes of where we search everything. 
    # The order of where they are is the most important thing: 
    # we want the top results to be shown first, right?
    classes = ['Z0LcW', 'IZ6rdc', 'ILfuVd NA6bn', 'ILfuVd', 'hgKElc', 'Okagcf', 'ILfuVd', 'dbg0pd OSrXXb'
               'CAIQAQ', 'vk_gy vk_sh',
               'Z0LcW XcVN5d AZCkJd', 'Z0LcW XcVN5d', 'gsrt vk_bk dDoNo FzvWSb XcVN5d DjWnwf',
               'vXQmIe gsrt', 'gsrt vk_bk dDoNo XcVN5d', 'vk_bk dDoNo FzvWSb XcVN5d', 'hgKElc',  # gsrt vk_bk dDoNo FzvWSb XcVN5d DjWnwf is new, remove if necessary 
               'yxAsKe', 'hgKElc', 'wob_t TVtOme', 'hgKElc', 'VssY5c', 'qv3Wpe', 'z7BZJb XSNERd', # 'ILfuVd', 'LGOjhe', 'wDYxhc', 'junCMe'
                # Remove class 'junCMe' if results aren't accurate 
               'ztXv9', 'Crs1tb', 'LGOjhe', 
                # Remove 'wDYxhc' if results aren't accurate 
               'ILfuVd', 'hgKElc', 'tw-data-text tw-text-large XcVN5d tw-ta', # Remove 'wDYxhc' if results aren't accurate 
               'tw-ta-container hide-focus-ring tw-nfl', 'hrcAhc', 'SvKTZc', 'dbg0pd', 'cXedhc', 
               'NC4yhe', 'm6vS6b PZPZlf', 'g9WsWb', 'Z0LcW XcVN5d AZCkJd', 'Uo8X3b', 'MUxGbd t51gnb lyLwlc lEBKkf', 
               'gsrt vk_bk dDoNo FzvWSb XcVN5d', 'KKHQ8c'] # For List use 'di3YZe', For wikipedia results in the google page use 'Uo8X3b'
               # Remove 'vXQmIe gsrt' if results arent accurate

    ## REMOVED CLASSES:
    removed_classes = {'junCMe' : 'Mais imagens',
                       'wDYxhc' : 'Something strange and "Mais imagens"'}
    
    classes_expl = {'Z0LcW': {'Type': 'div', 'Sample Question' : 'quem é o presidente dos estados unidos', 'Source' : 'Trustable'},
                    'IZ6rdc' : {'Type': 'div', 'Sample Question' : 'qual é a cor do mar', 'Source' : 'Post, Trustable', 'Additional Information' : {'Type of Answer' : 'Post', 'Classe de resposta adicional à direta' : ['span', 'ILfuVd NA6bn']}},
                    'ILfuVd NA6bn' : {'Type': 'span', 'Sample Question' : 'qual é a cor do mar', 'Source' : 'Post, Trustable', 'Additional Information' : {'Type of Answer' : 'Post', 'Classe de resposta direta' : ['div', 'IZ6rdc']}},
                    'hgKElc' : {'Type': 'span', 'Sample Question' : 'o que são animais filtradores', 'Source' : 'Post, Trustable', 'Informações adivionais' : {'data da postagem' : 'kX21rb ZYHQ7e'}},
                    'Okagcf' : {'Type': 'div', 'Sample Question' : 'Como surfar', 'Source' : 'Post, Trustable', 'Additional Information' : {'Type of Answer' : 'em pontos'}},
                    'wDYxhc' : {'Type': 'div', 'Sample Question' : 'o que fazer quando a pressão está baixa', 'Source' : 'Post, Trustable', 'Additional Information' : {'Type of Answer' : 'Post', 'Specific Class' : ['span', 'ILfuVd']}},
                    'ILfuVd' : {'Type': 'span', 'Sample Question' : 'o que é a mudança climática', 'Source' : 'Post, Trustable', 'Additional Information' : {'Type of Answer' : 'Post', 'Specific Class' : ['span', 'hgKElc'], 'Location of answer': 'Top of page, underneath images'}},
                    'dbg0pd OSrXXb' : {'Type': 'div', 'Sample Question' : 'qual é o hospital mais perto', 'Source' : 'Google, Trustable', 'Additional Information' : {'Type of Answer' : 'Google', 'Specific Class' : None, 'Location of answer': 'Top result of google maps search'}},
                    'cXedhc' : {'Type': 'div', 'Sample Question' : 'qual é a padaria mais perto', 'Source' : 'Google, Trustable', 'Additional Information' : {'Type of Answer' : 'Whole Result of dbg0pd OSrXXb', 'Specific Class' : None, 'Location of answer': 'Top result of google maps search'}},
                    'KKHQ8c' : {'Type': 'div', 'Sample Question' : 'quem fundou a apple', 'Source' : 'Google, Trustable', 'Additional Information' : {'Type of Answer' : 'All of the apple founders on top of page', 'Specific Class' : None, 'Location of answer': 'Top result of google search'}}
                    }

    # Here is the IDs for the webpages HTML
    ID = ['cwos', 'tw-target-text', 'tw-target-text-container', 'kAz1tf', 'WEB_ANSWERS_RESULT_6_QnOaYaSMFKPe1sQPg5mH0Ac__3', ''] # 1st Answer (little boxes down the search page) ID is 'NotFQb'

    # And the different types of 'boxes', I guess...
    typ = ['div', 'span', 'td']

    # A flag, just to be sure
    flag = True

    # This is the main loop
    for cl in classes:
        if flag == True:
            result = soup.find('div', class_=cl)
            #print(result)
            if result != None:
                flag = False
                #print('https://www.google.com/search?q=' + query + ' --> div -- ' + cl)
                break
            elif result == None:
                for sub in ID:
                    result = soup.find('div', class_=cl, id=sub)
                    #print(result)
                    if result == None:
                        result = soup.find('span', class_=cl, id=sub)
                        #print(result)
                    elif result != None:
                        #print('https://www.google.com/search?q=' + query + ' --> ' +cl+' -- span -- '+sub)
                        flag=False
                        break
                result = soup.find('span', class_=cl)
                #print(result)
                if result != None:
                    flag = False
                    break
                elif result == None:
                    result = soup.find(typ, class_=cl, id=ID)
                    #print(result)
        else:
            break
        if result != None:
            #print('https://www.google.com/search?q=' + query + ' --> ' + cl)
            break
    # Returns the answer found in google's snippet
    try:
        result = result.text
        return result
    except:
        return None