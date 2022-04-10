# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██       

############################################################
#  LISA Voice Install Service
#
#  Warning: This software will work, but it is not complete
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
############################################################

from LAS import lisa_core, lisa_interaction, lisa_processing, lisa_service, lisa_system
from sounds import play
import os
from time import sleep

words_to_replace = {'espaço':' ', 'traço':'-', 'tracinho':'-', 'hífen':'-', 'underline':'_', 'arroba':'@'}
keywords = ['ultimaletramaiúscula', 'tudomaiúsculo', 'tudominúsculo', 'primeiraletramaiúscula']
ssid_and_psk = []
ap_wifi = []

path = "/home/first_time.txt"
path = "first_time.txt"
wifi_path = "/etc/wpa_supplicant/wpa_supplicant.conf"
#wifi_path = "wifi.txt"

lisa_service.mode()

def explanation():

    # Intro
    lisa_interaction.speak("Olá, eu sou a Lisa, a sua assistente pessoal") # 1.mp3
    lisa_interaction.speak("Eu sou capaz de fazer muitas coisas para você, como realizar buscas na internet, dizer a previsão do tempo, falar notícias, e muito mais.") # 2.mp3
    lisa_interaction.speak("Porém, antes de tudo isso, eu preciso da sua ajuda para me configurar.") # 3.mp3

def word_explanation():
    # Explaining dictation
    lisa_interaction.speak("Agora vomos começar a configuração.") # 3,1.mp3
    lisa_interaction.speak("Vai funcionar assim:, Eu vou perguntar por informações, e você soletrará elas 2 segundos após ouvir esse som") # 4.mp3
    play(lisa_core.answer_sound)

    # Conditions
    lisa_interaction.speak("Se a palavra que você soletrou é escrita completamente em letras maiúsculas, basta dizer, tudo maiúsculo, logo após soletrar a palavra") # 5.mp3
    lisa_interaction.speak("Se a primeira letra da palavra que você soletrou é escrita em maiúsculo, basta dizer, primeira letra maiúscula, logo após soletrar a palavra") # 6.mp3
    lisa_interaction.speak("Para dizer que uma letra é escrita em maiúsculo, basta dizer, última letra maiúscula, logo após dizer a letra") # 7.mp3
    lisa_interaction.speak("Para soletrar um sinal de espaço, basta dizer a palavra, espaço,") # 8.mp3
    lisa_interaction.speak("Para soletrar um hífen, basta dizer a palavra, hífen, tracinho, ou, traço,") # --> 9.mp3
    lisa_interaction.speak("Para soletrar o símbolo de underline, basta dizer a palavra, underline,") # 10.mp3
    lisa_interaction.speak("Para soletrar o símbolo de arroba, basta dizer a palavra, arroba,") # 10,1.mp3
    lisa_interaction.speak("Quando você terminar de soletrar a informação, basta parar de falar e eu entenderei que terminou") # 11.mp3

def ap_connect():
    # Internet SSID
    lisa_interaction.speak("Vamos começar pela conexão com a internet via um ponto de acesso no seu celular.") # 26.mp3
    lisa_interaction.speak("Escute esses passos com atenção:") # 27.mp3
    lisa_interaction.speak("Você criará um Ponto de Acesso usando a sua rede móvel no seu celular.") # 28.mp3
    lisa_interaction.speak("Clique em Configurações ou Ajustes") # 29.mp3
    sleep(3)
    lisa_interaction.speak("Depois, clique em 'Conexões' e escolha a opção 'Roteador Wi-Fi e Ancoragem'") # 30.mp3
    sleep(3)
    lisa_interaction.speak("Ative a função 'Roteador Wi-Fi'") # 31.mp3
    sleep(3)
    lisa_interaction.speak("Clique nessa mesma opção para definir o nome, e senha, da rede") # 32.mp3
    lisa_interaction.speak("O nome deve ser:, lisa, tudo junto e escrito em minúsculo") # 33.mp3
    lisa_interaction.speak("A senha deve ser:, protótipo, tudo junto, minúsculo, e sem acento") # 34.mp3
    lisa_interaction.speak("Agora, eu vou esperar 2 minutos para você configurar a rede, e, em seguida, vou me reiniciar para continuarmos.") # 35.mp3

def wifi():
    # Internet SSID
    lisa_interaction.speak("Vamos continuar com a conexão com a internet")
    lisa_interaction.speak("Pronto para dizer as informações? Responda, Sim, ou, Não, após o som")
    play(lisa_core.answer_sound)
    yn = lisa_interaction.listen_engine()

    if str(yn).strip().lower() == 'sim':
        lisa_interaction.speak("Qual é o nome da rede que você deseje que eu me conecte?")
        play(lisa_core.answer_sound)

        while True:
            SSID = lisa_interaction.listen_engine()
            SSID = lisa_processing.preocess_input_for_dictation(str(SSID))
            lisa_interaction.speak("O nome da sua rede é " + str(SSID))
            print(SSID)
            play(lisa_core.answer_sound)
            yn = lisa_interaction.listen_engine()

            if 'sim' in str(yn).strip().lower():
                break
            else:
                lisa_interaction.speak("Qual é o nome da rede que você deseje que eu me conecte?")
                play(lisa_core.answer_sound)
    else:
        lisa_interaction.speak("Ok, quando estiver pronto diga, estou pronto")
        while True:
            yn = lisa_interaction.listen_engine()
            if 'pronto' in str(yn).strip().lower():
                lisa_interaction.speak("Qual é o nome da rede que você deseje que eu me conecte?")
                play(lisa_core.answer_sound)
                while True:
                    SSID = lisa_interaction.listen_engine()
                    SSID = lisa_processing.preocess_input_for_dictation(str(SSID))
                    lisa_interaction.speak("O nome da sua rede é " + str(SSID))
                    play(lisa_core.answer_sound)
                    yn = lisa_interaction.listen_engine()

                    if 'sim' in str(yn).strip().lower():
                        break
                    else:
                        lisa_interaction.speak("Qual é o nome da rede que você deseje que eu me conecte?")
                        play(lisa_core.answer_sound)
    
    # Internet Password
    lisa_interaction.speak("Agora vamos para a senha da sua internet")
    lisa_interaction.speak("Pronto para me dizer? Responda, Sim, ou, Não, após o som")
    play(lisa_core.answer_sound)
    yn = lisa_interaction.listen_engine()

    if 'sim' in str(yn).strip().lower():
        lisa_interaction.speak("Qual é a senha da rede " + str(SSID))
        play(lisa_core.answer_sound)

        while True:
            psk = lisa_interaction.listen_engine()
            psk = lisa_processing.preocess_input_for_dictation(str(psk))
            lisa_interaction.speak("A senha da sua rede é " + str(psk))
            play(lisa_core.answer_sound)
            yn = lisa_interaction.listen_engine()

            if 'sim' in str(yn).strip().lower():
                break
            else:
                lisa_interaction.speak("Qual é a senha da rede " + str(SSID))
                play(lisa_core.answer_sound)
    else:
        lisa_interaction.speak("Ok, quando estiver pronto diga, estou pronto")
        while True:
            yn = lisa_interaction.listen_engine()
            if 'pronto' in str(yn).strip().lower():
                lisa_interaction.speak("Qual é a senha da rede " + str(SSID))
                play(lisa_core.answer_sound)
                while True:
                    psk = lisa_interaction.listen_engine()
                    psk = lisa_processing.preocess_input_for_dictation(str(psk))
                    lisa_interaction.speak("A senha da sua rede é " + str(psk))
                    play(lisa_core.answer_sound)
                    yn = lisa_interaction.listen_engine()

                    if 'sim' in str(yn).strip().lower():
                        break
                    else:
                        lisa_interaction.speak("Qual é a senha da rede " + str(SSID))
                        play(lisa_core.answer_sound)

    ssid_and_psk.append(SSID)
    ssid_and_psk.append(psk)

def updates():
    # Warnings
    lisa_interaction.speak("Pronto. Agora eu vou me reiniciar e em seguida vou buscar por atualizações.")
    lisa_interaction.speak("Isso demorará o tempo necessário para tomar uma xícara de café. Quando tudo estiver pronto, avisarei tocando o som")
    play(lisa_core.answer_sound)
    lisa_interaction.speak("E falando, Atualizações instaladas,")
    os.system('sudo python3 install.py -lisa')

def restart():
    lisa_system.system_control_terminate("OS_RESTART")

def after_updates(download_from_gh = True):

    lisa_interaction.speak("Versão atual do sistema LISA: ")
    lisa_interaction.speak("Pronto. Todas as atualizações foram instaladas")
    lisa_interaction.speak("Para conversar comigo, basta dizer a palavra „Lisa“, aguardar pelo som,")
    play(lisa_core.answer_sound)
    lisa_interaction.speak("E começar a falar depois de 2 segundos.")

def first_time(path):
    with open(str(path), 'r') as file_object:
        f = file_object.readline()
    if f.strip() == 'true':
        return True
    elif f.strip() == 'middle':
        return "middle"
    elif f.strip() == 'end':
        return 'end'
    else:
        return False

def write_first_time(path = path, first_time = False):
    with open(str(path), 'w') as file_object:
        if first_time == True:
            file_object.write('true')
        elif first_time == "middle":
            file_object.write("middle")
        elif first_time == 'end':
            file_object.write('end')
        else:
            file_object.write('false')

if os.path.isfile(path):
    path=path
else:
    with open(str(path), 'w') as file_object:
        file_object.write('true')
    

if first_time(path) == True:
    explanation()
    ap_connect()
    write_first_time(path, first_time="middle")
    sleep(120)
    restart()
elif first_time(path=path) == "middle":
    word_explanation()
    wifi()
    lisa_system.set_wifi(ssid_and_psk[0], ssid_and_psk[1], path=wifi_path)
    write_first_time(path, 'end')
    updates()
    restart()
elif first_time(path) == 'end':
    after_updates(download_from_gh = False)
    write_first_time()
    os.system("python3 lisa_LAS.py -v -g")
else:
    os.system("python3 lisa_LAS.py -v -g")