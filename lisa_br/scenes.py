
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  LISA Scenes API (LSA)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

import os
import sys
from weather import icestorm_results

usr_choice_sc = str(' '.join(sys.argv[1:]))
def weather():
    usr_choice='-no_text'
    result_weather = icestorm_results('')
    precipitation = int(result_weather['precipitation'].replace('%',''))
    temp = "A temperatura agora é de " + result_weather['temperature'] + ' graus celcius. '
    if precipitation > 40:
        rain = 'Hoje pode estar chovendo bastante, é melhor se preparar e levar um guarda chuva. A precipitação é de ' + str(precipitation) + '%.'
    elif precipitation < 10:
        rain = 'E a precipitação hoje é de ' + str(precipitation) + '%. Não há necessidade de levar um guarda chuva. '
    else:
        rain = 'E a precipitação hoje é de ' + str(precipitation) + '%.'
    wind = int(result_weather['wind'].replace(' km/h',''))
    if wind >= 22 and wind <= 27:
        wind_resp = ' Os ventos estão fortes, e podem chegar até uma velocidade de ' + str(wind) + 'km/h. Pode ser difícil manter um guarda chuva aberto e há assobio em fios de postes.'
    elif wind >= 28 and wind <= 40:
        wind_resp = ' Os ventos estão bem fortes, e podem chegar até uma velocidade de ' + str(wind) + 'km/h. Pode haver quebra em galhos de árvores.'
    elif wind >= 41:
        wind_resp = ' Tome cuidado hoje, pois está ventando muito, a uma velocidade de ' + str(wind) + 'km/h. É bem possível haver danos em árvores e em pequenas construções. '
    else:
        wind_resp = ' Os ventos estão a uma velocidade de ' + str(wind) + 'km/h, '
    humidity = int(result_weather['humidity'].replace('%',''))
    if humidity > 30:
        hum = ' E a umidade é de ' + str(humidity) + '%.'
    elif humidity > 12 and humidity <= 30:
        hum = ' Cuidado! A umidade está muito baixa hoje, estando a ' + str(humidity) + '%. Procure não fazer exercicios fisicos ao ar livre, e se lembre de se manter bem hidratado. É aconselhável umidificar o ambiente e usar soro fisiológico nos olhos e narinas.'
    else:
        hum = ' A umidade está abaixo de 12%. Este é um estado de emergência. Interrompa qualquer atividade ao ar livre como exercícios físicos e atividades que exigam aglomeração de pessoas. Mantenha locais com crianças e idosos muito bem umidificados.'

    return temp + rain + wind_resp + hum
    

def today():
    from datetime import date
    today = date.today()
    # dd/mm/YY
    year= today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    l_date = date(int(year), 1,1)
    f_date = date(int(year), int(month), int(day))
    delta = (f_date - l_date)
    a = "Já estamos no dia de número " + str(delta.days) + " do ano. Força aí."
    b = "Já se passaram cerca de " + str(round((int(delta.days) / 365)*100)) + " por cento do ano."
    if int(day) %2 or int(month) == 1:
        return b
    else:
        return a

def dia_de_que():
    import requests
    from bs4 import BeautifulSoup
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.datascomemorativas.me/', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    ID = ['cwos', 'tw-target-text', 'tw-target-text-container', 'kAz1tf', ''] # Answer ID is 'NotFQb'
    typ = ['span', 'div', 'td', 'th', 'li', 'table']
    #classes=['vk_bk TylWce', 'wob_t TVtOme']
    classes = ['calendar-day is-today','day-date']
    for cl in classes:
        for t in typ:
            result = soup.find(t, class_=cl)
            if result == None:
                for i in ID:
                    #result = soup.find(t, class_=cl, id=i)
                    result = soup.find(t, class_=cl, id=i, xpath='/html/body/section/div/div/table/tbody/tr[4]/td[5]/ul/li/span')
                    if result != None:
                        return (result.text).split(':')[1]

            else:
                return (result.text).split(':')[1] 
        
    if result==None:
        return 'Não disponível'

    date =result.split('.')[1]

def good_morning():
    from search_at_google import get_google_result
    dia = str(get_google_result('dia de hoje'))
    rep = ['Hora local', 'Feedback']
    if dia != None:
        try:
            for i in rep:
                dia = str(dia).replace(i, "")
        except:
            pass
    dia_de_que_ = str(dia_de_que())
    hj = today()
    day = ". Hoje é " + str(dia).strip() + ", o dia em que comemoramos o " + str(dia_de_que_).strip() + '. É bom lembrar que ' + str(hj) + ' '
    wea = "Agora aqui vai a previsão do tempo: " + weather()
    return day + wea + resume()

def good_night():
    from search_at_google import get_google_result
    # Hours:
    import requests
    from bs4 import BeautifulSoup
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=que+horas+s%C3%A3o', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    hours = soup.find('div', class_="gsrt vk_bk FzvWSb YwPhnf")
    try:
        hours = hours.text
    except:
        hours = get_google_result('que horas são')
    a = '. Já são ' + str(hours) + ' da noite. O sol vai nascer amanhã as ' + str(get_google_result('que horas é o nascer do sol amanhã')) + ' da manhã. '
    from weather import get_weather_google, get_place_google, get_forecast_google
    usr_choice = ''
    weather = icestorm_results('amanhã')
    b = str("A temperatura amanhã em " + str(weather['location']) + " estará por volta dos " + str(weather['temperature']) + " graus celcius com " + 
        str(weather['description']) + ". A precipitação será de " + str(weather['precipitation']) + ", a humidade de " + 
        str(weather['humidity']) + " e ventos podem chegar até " + str(weather['wind']) + ". ")
    if 'quinta' in str(get_google_result('dia de hoje')):
        c = '. Por fim, tenho algo bom para lhe dizer: amanhã é sexta-feira. '
    else:
        c=''
    return a+b+c

def resume():
    from rss_feed_search import get_feed
    news_a = get_feed(query='')
    return ' Aqui vai a notícia mais recente: ' + str(news_a).strip() + '. '

if 'day' in usr_choice_sc:
    try:
        print(good_morning())
    except Exception as e:
        print(str(e) + '. Infelizmente eu não consigo me conectar à internet, e portanto não posso exibir o seu feed. Então, ')
elif 'night' in usr_choice_sc:
    try:
        print(good_night())
    except:
        print('. Infelizmente eu não consigo me conectar à internet, e portanto não posso exibir o seu feed. Então, ')



