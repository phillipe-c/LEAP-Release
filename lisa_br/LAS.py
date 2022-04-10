
# ██       ████████████ ██████ ████████████  
# ██       ██          ██    ██ ██        ██ 
# ██       ██████      ████████ ███████████  
# ██       ██          ██    ██ ██      
# ████████ ███████████ ██    ██ ██   

#########################################################
#  LISA Source Code  
#
#  Lisa API Service 2 (LAS)
#  Total number of functions: 25+ (not counted)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
#########################################################

# We import all the modules
import aiml
import os
import time
import argparse
import random
from hotword_detection import hotword_engine
import sys
from sounds import play
import sys
import os
import threading
import platform
import lisa_interface_match

# As it is comon to see some errors when importing these modules,
# we add a try/except scope to the code.
try:
    import pyttsx3
    from threading import Thread
    import pyowm
    import wikipedia
    import bs4
    import requests
    from bs4 import BeautifulSoup
    import speech_recognition as sr
    from gtts import gTTS
    import playsound
    from leds import GradLed
except Exception as e:
    pass


# These functions execute tasks related to the operating system (3 functions)
class lisa_system:

    # This function exits the program, shuts the system down and restarts it when asked
    def system_control_terminate(command, end = 'PROGRAM_TERMINATE', shutdown = 'OS_SHUTDOWN', restart = 'OS_RESTART', password = 'raspberry'):
        """Executes the termination commands"""
        if command == end:
            sys.exit()
        elif command == shutdown:
            os.system('echo %s|sudo -S %s' % (password, 'shutdown -h now'))
        elif command == restart:
            os.system('echo %s|sudo -S %s' % (password, 'reboot'))
    
    # Linux or macOS? Here is the answer
    def retrieve_os():
        """
        - Returns "macOS" for macOS
        - Returns "Linux" for Linux
        """
        if platform.system() == 'Darwin':
            return "macOS"
        elif platform.system() == 'Linux':
            return 'Linux'

    # Sets the Wi-Fi:
    def set_wifi(SSID, password, path = "/etc/wpa_supplicant/wpa_supplicant.conf"):
        try:
            with open(str(path), 'a') as file_object:
                file_object.write('\nnetwork={\n')
                file_object.write('        ssid="' + str(SSID).strip() + '"\n')
                file_object.write('        psk="' + str(password).strip() + '"\n')
                file_object.write("}\n")
            print('SUCCESS')
        except Exception as e:
            print('Failed\nError: ' + str(e))

    # Function to read the different steps the setup is in, 
    def first_time(path = "first_time.txt"):
        """
        Reads the state of the setup:
        - If the setup is running for the first time, it returns (bool) True
        - If the setup is in the middle, it returns 'middle'
        - If the setup is in the end, it returns 'end'
        - If everything is finished and running as configurated, it returns (bool) False
        """
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


# This class contains the not only the core functions of Lisa available for importing, but also many important variables. (2 functions)
class lisa_core:

    # These are the variables we use in the program.
    mode = "text" # The default mode is the one with no voice recognition.

    mode_list = ['text', 'voice', 'gTTS'] # The program mode options

    voice = "pyttsx3" # The default voice service is pytts

    terminate = ['tchau', 'sair', 'saia', 'adeus', 'vá', 'fechar'] # The shutdown words

    stop_words = ['parar', 'para', 'pare', 'pausa', 'pause', 'chega', 'parô', 'parou', 'lisa', 'elisa', 'linda']

    hotwords_list = ['Lisa', 'Liza', 'Lisam', 'Elisa', 'Eliza', 'Isa', 'Unisa', 'Lise', 'Iza', 'linda', 'Isa'] # The activation words (yes sometimes the sst understands Unisa)
    hotwords_space = ['Lisa ', 'Liza ', 'Lisam ', 'Elisa ', 'Eliza ', 'Isa ', 'Unisa ', 'Lise ', 'Iza ', 'linda ', 'Isa ']
    hotwords_list = hotwords_space + hotwords_list

    forget = ['não esquece lisa', 'não não esquece', 'esquece esquece lisa', 'esquece o que eu falei', 'esqueca o que eu falei', 'esquece o que eu acabei de falar']

    activation = ['Sim?', 'Estou aqui', 'Oi', 'Vá em frente'] # The answer words

    os_ter = ['desligar'] # The device shutdown word. This word can do a shutdown on CiclOS LISA devices
    
    os_rest = ['reiniciar'] # The device restart word. This word can restart CiclOS LISA devices
    
    en_Voice_id = 'com.apple.speech.synthesis.voice.samantha' # For OSX
    
    pt_Voice_id = 'com.apple.speech.synthesis.voice.luciana' # For OSX
    
    history = [] # Volatile History variable
    
    history_lisa = [] # Volatile History variable
    
    history_dict = {} # Volatile History variable
    
    error_file = 'error_log.txt' # Directory for the error file

    answer_sound = "answer_sound.mp3"

    language = "pt"


    # This function is used to save any text to a file. Most important use of it is for the Error Log
    def save(sentence, filedef, title = '', w_t = False, file_extension = ''):
        """ Saves a text 'sentence' in a file 'filedef' with a title 'title'. 
        It can also save the time and date ('w_t = True') before each sentence 'sentence'. 
        The file extension is set as .txt by default, but it can be changed by setting 
        file_extension to the desired extension
        """
        filechoose = str(filedef)
        if ('.txt' not in filechoose) and (file_extension == ''):
            filechoose = filechoose + '.txt'
        elif ('.' not in file_extension) and (file_extension != ''):
            filechoose = filechoose + '.' + file_extension
        else:
            filechoose = filechoose + file_extension
        if os.path.isfile(filedef):
            try:
                with open(filechoose, 'a') as file_object:
                    if w_t == True:
                        t = time.localtime()
                        the_local_time = str(time.strftime("%D, %H:%M:%S", t))
                        file_object.write(the_local_time + ' -- ' + str(sentence))
                    else:
                        file_object.write(str(sentence))
                    file_object.write("\n")
            except FileNotFoundError:
                print("404 - not found, could not write to file")
        else:
            try:
                with open(filechoose, 'w') as file_object:
                    file_object.write(title + "\n\n")
                    if w_t == True:
                        t = time.localtime()
                        the_local_time = str(time.strftime("%D, %H:%M:%S", t))
                        file_object.write(the_local_time + ' -- ' + str(sentence))
                    else:
                        file_object.write(str(sentence))
                    file_object.write("\n")
            except FileNotFoundError:
                print("404 - not found, could not write to file")


    # Gets the arguments the program to operate
    def argumentos():
        """Just the arguments"""
        argpars = argparse.ArgumentParser()
        options = argpars.add_argument_group('parameters')
        options.add_argument('-v', '--voice', action='store_true', required=False,
                            help='Enables voice recognition')
        options.add_argument('-g', '--gtts', action='store_true', required=False,
                            help='Uses the google voice')
        argumentos = argpars.parse_args()
        return argumentos


# This is the class that contains the functions that are used more in the surface of the program itself, for it to actually do something. (3 functions)
class lisa_service:

    # This function gets the necessary arguments for the program to work
    def mode(set_argument = ''):
        """You can set the desired mode by changing set_argument to 'text', 'gTTS' or 'voice'.
           It can take the mode specified on the program calling this function"""
        if set_argument == '':
            args = lisa_core.argumentos()
            if (args.gtts):
                lisa_core.voice = "gTTS"
                return "gTTS"
            if (args.voice):
                lisa_core.mode = "voice"
                return "voice"
            if (lisa_system.retrieve_os() == 'Linux') and ((args.voice) or (args.gtts)):
                lisa_core.mode = "voice"
                lisa_core.voice = "gTTS"
                return "gTTS"
            else:
                return "text"
        elif set_argument == 'text':
            lisa_core.mode = "text"
            return set_argument
        elif set_argument == 'voice':
            lisa_core.mode = "voice"
            return set_argument
        elif set_argument == 'gTTS':
            lisa_core.voice = 'gTTS'
            return set_argument

    # Loads the kernel
    def load_kernel(xml_file = "std-startup.xml"):
        """Function to load the kernel"""
        # Gets the kernel up and running
        kernel = aiml.Kernel()

        # Gets the XML file for the conversation, and checks if there is a .brn file
        if os.path.isfile("lisa_brain.brn"):
            kernel.bootstrap(brainFile="lisa_brain.brn")
        else:
            kernel.bootstrap(learnFiles=xml_file, commands="load aiml b")
        return kernel
        
    # Function that access lisa for anything needed. Think of it as an API
    def lisa_answer(user_question, _kernel_):
        """Just answers the question in clean text"""
        _answer_ = _kernel_.respond(user_question)
        return _answer_


    # LIM FUNCTION INTEGRATION
    # Function that access lisa for anything needed. Think of it as an API 
    # (LIM Language Version)
    def lisa_answer_lim(user_question, startup_file="lim_startup.liminit"):
        answer = lisa_interface_match.lim_main.answer(str(user_question), startup_file=startup_file)
        return answer
    
    # Double LIM-AIML matching access
    def lisa_answer_both(user_question, aiml_kernel_ = None, lim_startup_file="lim_startup.liminit", priority = 'LIM', block_lim_else = True):
        """If priority is set to 'LIM', the algorithm will search for answers contained in LIM files first\n
           If priority is set to 'AIML', the algorithm will search for answers contained in AIML files first\n
           If priority is set to 'RANDOM', the algorithm will search for answers contained in LIM or AIML files randomly"""

        if priority == 'LIM':
            answer = lisa_service.lisa_answer_lim(user_question, lim_startup_file)
            if answer == None:
                if aiml_kernel_ != None:
                    answer = lisa_service.lisa_answer(user_question, aiml_kernel_)
            return answer
        elif priority == 'AIML':
            answer = None
            if aiml_kernel_ != None:
                answer = lisa_service.lisa_answer(user_question, aiml_kernel_)
            if answer == None:
                answer = lisa_service.lisa_answer_lim(user_question, lim_startup_file)
            return answer
        elif priority == 'RANDOM':
            from random import choice
            answer = []
            if aiml_kernel_ != None:
                answer.append(lisa_service.lisa_answer(user_question, aiml_kernel_))
            answer.append(lisa_service.lisa_answer_lim(user_question, lim_startup_file))
            return choice(answer)


# This class handles all the information processing, such as cleaning out specific words of an answer or input. (7 functions)
class lisa_processing:

    def input_cleanout(question, clean_words: list):
        """Removes clean_words from the the text question and then returns the result"""
        if clean_words in question:
            for cw in clean_words:
                if cw in question:
                    lisa_core.save(cw + ' -- ' + question, 'bad_file.txt', 'Expressões Explicitas Usadas:')
                    question = str(question).replace(cw, '')
        return question

    def answer_cleanout(answer, clean_words: list):
        """Removes clean_words from the the text answer and then returns the result"""
        if clean_words in answer:
            for cw in clean_words:
                if cw in answer:
                    lisa_core.save(cw + ' -- ' + answer, 'bad_answers.txt', 'Expressões Explicitas Respondidas:')
                    str(answer).replace(cw, '')
                    return answer

    def remove_lisa_from_input(question, lisa_activation_list: list = lisa_core.hotwords_list):
        """Removes lisa activation words from the input question and then returns it"""
        for lisa_word in lisa_activation_list:
            if lisa_word in question:
                question = str(question).replace(str(lisa_word),"")
        return question 

    # Not working, don't know why
    def check_none_input(question):
        if (str(question) == "") or (str(question) == 0) or (str(question) == '0'):
            return None
        else:
            return question    

    def check_forget_input(question):
        forget = lisa_core.forget
        for f in forget:
            if f in str(question):
                return None
        return question
    
    def check_termination_on_user_input(question, terminate_words = lisa_core.terminate, shutdown_words = lisa_core.os_ter, restart_words = lisa_core.os_rest):
        """Returns 'PROGRAM_TERMINATE' when the input is terminate_words,
                   'OS_SHUTDOWN' when the input is shutdown_words, and
                   'OS_RESTART' when the input is restart_words"""
        if str(question).lower().replace(" ", "") in terminate_words:
            return 'PROGRAM_TERMINATE'
        elif str(question).lower().replace(" ", "") in shutdown_words:
            return 'OS_SHUTDOWN'
        elif str(question).lower().replace(" ", "") in restart_words:
            return 'OS_RESTART'

    def update_history(history_dict = {}, input_ = '', answer_ = ''):
        """Updates history"""
        if input_ == '' and answer_ == '':
            for key in history_dict:
                lisa_core.save('Question: ' + key, 'history_of_conversation.txt', 'History of conversation:', w_t = True)
                lisa_core.save('Answer: ' + history_dict[key] + '\n', 'history_of_conversation.txt', 'History of conversation:', w_t = True)
        else:
            history_dict = {input_ : answer_}
            for key in history_dict:
                lisa_core.save('Question: ' + key, 'history_of_conversation.txt', 'History of conversation:', w_t = True)
                lisa_core.save('Answer: ' + history_dict[key] + '\n', 'history_of_conversation.txt', 'History of conversation:', w_t = True)

    # The fancyest function of the processing class
    def preocess_input_for_dictation(something, words_to_replace = {'espaço':' ', 'traço':'-', 'tracinho':'-', 'hífen':'-', 'underline':'_', 'arroba':'@'}, keywords = ['últimaletramaiúscula', 'tudomaiúsculo', 'tudominúsculo', 'primeiraletramaiúscula']):
        """Process input coming from a dictation:
        - "hífen" or "tracinho" or "traço" —> "-"
        - "underline" —> "_"
        - „tudo maiúsculo“ —> what came before gets upper() (ed)
        - „tudo minúsculo“ —> what came before gets lower() (ed)
        - „primeira letra grande“ or „primeira letra maiúscula“ —> what came before > .title()
        - "arroba" --> @
        - „espaço“ —> " " \n
        Exemplo: (antes / depois)
        - "o i primeira letra maiúscula espaço tracinho e u tudo maiúsculo espaço q u e underline 
        r o tudo maiúsculo espaço u m ultimaletramaiúscula espaço b o ultimaletramaiúscula m espaço 
        d i a primeiraletramaiúscula"
        - Oi -EU que_RO uM bOm Dia
        """
        some_list = []
        list_of_something = list(something)

        # Removing spaces
        for key_one in list_of_something:
            if key_one != ' ':
                some_list.append(key_one)

        # Replacing symbols
        another_list = ''.join(some_list)
        for key in words_to_replace:
            another_list = another_list.replace(key, words_to_replace[key])
        
        # Upper for a letter
        upper_letter_list = list(another_list)
        more_lists = []
        x=-1
        for fl in upper_letter_list:
            x=x+1
            more_lists.append(fl)
            if len(more_lists) >= 20:
                if ''.join(more_lists[x-19:x+1]) == keywords[0]:
                    more_lists[x-20] = str(more_lists[x-20]).upper()
        upper_letter_list = ''.join(more_lists).replace(keywords[0], '')

        # Upper or lower for a word
        upper_word_list = list(upper_letter_list)
        more_lists = []
        final_l = []
        x=-1
        z=0
        for fl2 in upper_word_list:
            x=x+1
            more_lists.append(fl2)
            if len(more_lists) >= 13:
                if (''.join(more_lists[x-12:x+1]) == keywords[1]) or (''.join(more_lists[x-12:x+1]) == keywords[2]):
                    y=-1
                    rev_list = []
                    ml_rev = more_lists[0:x-12]
                    ml_rev.reverse()
                    for rl in ml_rev:
                        if (rl != ' ') and (rl != '_') and (rl != '-'):
                            y=y+1
                            rev_list.append(rl)
                        else:
                            break
                    rev_list.reverse()
                    if ''.join(more_lists[x-12:x+1]) == keywords[1]:
                        more_lists[(x-13)-y:x-12] = str(''.join(rev_list)).upper()
                    elif ''.join(more_lists[x-12:x+1]) == keywords[2]:
                        more_lists[(x-13)-y:x-12] = str(''.join(rev_list)).lower()
        upper_word_list = ''.join(more_lists).replace(keywords[2], '')
        list(upper_word_list)
        upper_word_list =''.join(upper_word_list).replace(keywords[1], '')

        # Title a word
        title_word_list = list(upper_word_list)
        more_lists = []
        x=-1
        for fl2 in title_word_list:
            x=x+1
            more_lists.append(fl2)
            if len(more_lists) >= 22:
                if (''.join(more_lists[x-21:x+1]) == keywords[3]):
                    y=-1
                    rev_list = []
                    ml_rev = more_lists[0:x-21]
                    ml_rev.reverse()
                    for rl in ml_rev:
                        if (rl != ' ') and (rl != '_') and (rl != '-'):
                            y=y+1
                            rev_list.append(rl)
                        else:
                            break
                    rev_list.reverse()
                    more_lists[(x-22)-y:x-21] = str(''.join(rev_list)).title()
        title_word_list = ''.join(more_lists).replace(keywords[3], '')

        return title_word_list


# This class provides all the necessary functions for the interaction with the world (5 functions)
class lisa_interaction:

    # Function to transform Text to Speech using Google's engine
    def say_using_gtts_with_mixer(speech_file):
        tts = gTTS(text=speech_file, lang='pt')
        tts.save('speech_file.mp3')
        mixer.init()
        mixer.music.load('speech_file.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)
    
    # Even another function to transform Text to Speech, but using pyttsx3
    def say_using_pytts(sentence):
        try:
            engine = pyttsx3.init()
            try:
                if platform.system() == 'Darwin':
                    engine.setProperty('voice', lisa_core.pt_Voice_id)
                else:
                    engine.setProperty('voice')
            except:
                lisa_core.save('func say(), error at configuring property', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)        
                engine.setProperty('voice', lisa_core.pt_Voice_id)
                print("Property couldn't be set")
            engine.say(str(sentence))
            engine.runAndWait()
        except:
            lisa_core.save('func say(), Could not say "' + sentence + '"', lisa_core.error_file, title='Errors In The Lisa Code:', w_t = True)

    # Another function to transform Text to Speech using Google's engine, but this time using native players on both OS X and Linux
    def say_using_gtts(speech_file):
        try:
            myobj = gTTS(text=speech_file, lang='pt', slow=False) 
            myobj.save("speach_file_gtts.mp3")
            try:
                if platform.system() == 'Darwin':
                    os.system("afplay speach_file_gtts.mp3")
                else:
                    os.system("mpg321 speach_file_gtts.mp3")
            except:
                os.system("afplay speach_file_gtts.mp3") # Use mpg321, if you are in Linux
        except:
            lisa_core.save('func gtts_say(), Could not say "' + speech_file + '", using pyttsx3 instead', lisa_core.error_file, title='Errors In The Lisa Code:', w_t = True)
            try:
                lisa_interaction.say_using_pytts(speech_file)
            except Exception as e:
                lisa_core.save('func gtts_say() in say(), Could not say "' + speech_file + '" even using pyttsx3, due to the following error: ' + str(e), lisa_core.error_file, title='Errors In The Lisa Code:', w_t = True)

    def generate_speech_audio_file_gtts(text, filename_with_sufix):
        try:
            myobj = gTTS(text=text, lang='pt', slow=False) 
            myobj.save(filename_with_sufix)
        except:
            lisa_core.save('func gtts_say(), Could not say "' + text + '", using pyttsx3 instead', lisa_core.error_file, title='Errors In The Lisa Code:', w_t = True)
            
    # THE function to transform Text to Speech. It actually chooses which one of those 2 above will be used.
    def speak(speech_file, voice = lisa_service.mode()): # For a better experience in Linux, try using gTTS
        if voice == "gTTS":
            try:
                GradLed.respond_led() # Activates device LED. Check which LISA devices supports LED response
            except:
                lisa_core.save('func speak(), Could not activate respond_led', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)
            lisa_interaction.say_using_gtts(speech_file)
            try:
                GradLed.grad_turn_off() # Deactivates device LED. Check which LISA devices supports LED response
            except:
                lisa_core.save('func speak(), Could not deactivate respond_led', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)
        else:
            try:
                GradLed.respond_led() # Activates device LED. Check which LISA devices supports LED response
            except:
                lisa_core.save('func speak(), Could not activate respond_led', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)
            lisa_interaction.say_using_pytts(speech_file)
            try:
                GradLed.grad_turn_off() # Deactivates device LED. Check which LISA devices supports LED response
            except:
                lisa_core.save('func speak(), Could not deactivate respond_led', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)

    # Function to transform Speech to Text using Google's engine
    def listen_engine():
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source: # use sr.Microphone(device_index=YOUR_INDEX) for the desired microphone index
                                        # LISA devices use sr.Microphone(device_index=1)
            print("Listening...")
            try:
                #audio = r.adjust_for_ambient_noise(source) # delete this if the program won't recognize
                audio = r.listen(source)
            except:
                return 0
        try:
            recognized_audio = r.recognize_google(audio, language='pt_BR')
            return recognized_audio
        except sr.UnknownValueError:
            return(0)
        except sr.RequestError as e:
            print("Could not request results from " +
                  "Google Speech Recognition service; {0}".format(e))
            lisa_core.save('func listen_engine(), Could not get listen results from Google', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)
            try:
                GradLed.error_msg_led() # Activates device error LED. Check which LISA devices supports error LED response
            except:
                lisa_core.save('func listen_engine(), Could not activate error message LED', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)


# These set of functions can be used to build a voice interface faster. (2 functions)
class lisa_prebuilt_voice:

    def load_listener(hotwords = lisa_core.hotwords_list, play_startup_sound = False):
        if play_startup_sound == True:
            play("LEAP\ Welcome.m4a")
        hotword_engine.start_listener(lisa_core.hotwords_list)

    def detect_and_listen(answer_sound = 'answer_sound.mp3', hotwords = lisa_core.hotwords_list, invert_activation = 1):
        """Searches for a hotword ONCE and if it foud, listens to the outside world...\n
        If "invert_activation" == 0, it will run the rest of the function if the hotword is NOT detected."""
        print('Trying to detect...')
        user_input = 0
        while True:
            try:
                if hotword_engine.hotword_detection(lisa_core.hotwords_list) == 1:
                    print('\nDETECTED!\n')
                    try:
                        GradLed.grad_turn_off()
                    except:
                        lisa_core.save('func main(), Could not deactivate respond_led', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)
                    play(answer_sound)
                    user_input = lisa_interaction.listen_engine()
                    break
            except:
                break
        if lisa_processing.check_none_input(user_input) == None:
            print('None')
            return None
        elif lisa_processing.check_forget_input(user_input) == None:
            print('Forgetting')
            lisa_interaction.speak('OK')
            return None
        else:
            if lisa_processing.check_termination_on_user_input(user_input) == "PROGRAM_TERMINATE":
                play('LEAP\ Goodbye.m4a')
                sys.exit()
            return user_input

    def process_and_answer(user_input, kernel = ''):
        """Processes the input and answers the question"""
        if kernel == '':
            kernel = lisa_service.load_kernel()
        answer = lisa_service.lisa_answer(user_input, kernel)
        return answer

    def process_and_answer_lim(user_input, startup_file = "lisa_startup.liminit"):
        """Processes the input and answers the question"""
        answer = lisa_service.lisa_answer_lim(user_input, startup_file)
        return answer
    
    def process_and_answer_both(user_question, aiml_kernel_ = None, lim_startup_file="lim_startup.liminit", priority = 'LIM'):
        """If priority is set to 'LIM', the algorithm will search for answers contained in LIM files first\n
           If priority is set to 'AIML', the algorithm will search for answers contained in AIML files first\n
           If priority is set to 'RANDOM', the algorithm will search for answers contained in LIM or AIML files randomly"""
        return lisa_service.lisa_answer_both(user_question, aiml_kernel_, lim_startup_file, priority)

    def speak_and_listen_for_ending(answer, mode):
        """INCOMPLETEEEEE!!!!!!!!!! DO NOT USE OR IT MIGHT BREAK EVERYTHING"""        
        thread = threading.Thread(target=lisa_interaction.speak, args=(answer, mode,), daemon=True)
        thread.start()
        thread = threading.Thread(target=hotword_engine.hotword_detection, args=(lisa_core.forget,), daemon=True)
        thread.start()
        

# These functions are those from the voice install. (2 functions)
class lisa_install:

    def first_time(path = "first_time.txt"):
        """Reads if it's the first time running"""
        with open(str(path), 'r') as file_object:
            f = file_object.readline()
        if f.strip() == 'true':
            return True
        else:
            return False

    def write_first_time(path = "first_time.txt", first_time = False):
        """Write if it's the first time running"""
        with open(str(path), 'w') as file_object:
            if first_time == True:
                file_object.write('true')
            else:
                file_object.write('false')


# These are old functions, in case of compatibility need:
class lisa_old:

    #Importing
    from hotword_old import Hotword

    def detect_and_listen(answer_sound = 'answer_sound.mp3', hotwords = lisa_core.hotwords_list, invert_activation = 1):
        """Searches for a hotword ONCE and if it foud, listens to the outside world...\n
        If "invert_activation" == 0, it will run the rest of the function if the hotword is NOT detected."""
        print('Trying to detect...')
        if Hotword.detect_hotwords_with_list(hotwords) == invert_activation:
            print('Hotword Detected!')
            try:
                GradLed.grad_turn_off()
            except:
                lisa_core.save('func main(), Could not deactivate respond_led', lisa_core.error_file, title = 'Errors In The Lisa Code:', w_t = True)
            play(answer_sound)
            user_input = lisa_interaction.listen_engine()
            if lisa_processing.check_none_input(user_input) == None:
                print('None')
                return None
            else:
                return user_input
        else:
            return None
