from weather import icestorm_results
import sys
usr_choice = str(' '.join(sys.argv[1:]))
status = 0

if "-forecast_weather" in usr_choice:
    usr_choice = usr_choice.replace('-forecast_weather', '')
    status = 'forecast'
elif '-no_text' in usr_choice:
    usr_choice = ''
    status = 'notext'
else:
    usr_choice = usr_choice

try:
    weather = icestorm_results(usr_choice)
except Exception as e:
    print('Não foi possível exibir o tempo por algum motivo. O erro será salvo no log: ' + str(e))
    status = 'notext'

if status == 'forecast':
    # Weather forecast from Google weather (weather.com):
    result = str("A temperatura " + str(weather['day']) + " em " + str(weather['location']) + " estará por volta dos " + str(weather['temperature']) + " graus celcius com " + 
                  str(weather['description']) + ". A precipitação será de " + str(weather['precipitation']) + ", a humidade de " + 
                  str(weather['humidity']) + " e ventos podem chegar até " + str(weather['wind']))
elif status == 'notext':
    result=''
else:
    # Google weather (pwd by weather.com) using local browser adress (usually more precise):
    result = str("A temperatura em " + str(weather['location']) + " está por volta dos " + str(weather['temperature']) + 
                  " graus com " + str(weather['description']) + ". A precipitação é de " + str(weather['precipitation']) + 
                  ", a humidade é de " + str(weather['humidity']) + ", e está ventando a uma velocidade aproximada de " + str(weather['wind']))

try:
    print(result)
except Exception as e:
    print('Não foi possível exibir o tempo por algum motivo. O erro será salvo no log: ' + str(e))
    #save('resweather.py error > ' + e, 'error_log.txt', title = 'Errors In The Lisa Code:', w_t = True)