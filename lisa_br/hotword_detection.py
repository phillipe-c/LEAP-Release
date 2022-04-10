
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

##########################################################
#  LISA Hotword Detector
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

import speech_recognition as sr
import threading
from time import sleep
from threading import Event
from datetime import datetime
import multiprocessing

r = sr.Recognizer()
aud = []
detected = []
flag = True

buffer_clean = []

class hotword_engine:
    """The VERY simple and rudimentar hotword detector. It's all a question of time ;)
    
    detect_with_callback() --> detects a hotword and if found, calls a function
    detect() --> detects a hotword and if found returns 1, else, returns 0
    detect_hotwords_with_list() --> searches for a hotword in a list, and if found returns 1, else, returns 0"""
    state = 0

    def __init__(self):
        super().__init__()

    def clear_all():
        import sys
        sys.exit(0)

    def timer(hotword):
        """Defines the maximum time for each audio recording made based on the length of the hotword"""
        if isinstance(hotword, list):
            hotword = hotword[0]
        def letter(word): 
            return [char for char in word]  
        letters = letter(hotword)
        time_for_each_letter = 0.4
        time=0
        time=time_for_each_letter*(len(letters))
        return time

    def change_audio(audio):
        aud.clear()

    def listen(time, timeout, print_=True):
        while flag == True:
            with sr.Microphone() as source:
                try:
                    audio = r.listen(source, timeout=timeout, phrase_time_limit=time)
                    aud.append(audio)
                    if print_ == True:
                        print('Listened ' + str(audio) + ' at func 1 -- ' + str(datetime.now().time()))
                except:
                    pass

    def listen2(time, timeout, audio = None, print_=True):
        while flag == True:
            with sr.Microphone() as source:
                try:
                    audio = r.listen(source, timeout=timeout, phrase_time_limit=time)
                    aud.append(audio)
                    if print_ == True:
                        print('Listened ' + str(audio) + ' at func 2 -- ' + str(datetime.now().time()))
                except:
                    pass

    def detect(audio, lang):
        try:
            hotword = r.recognize_google(audio, language=lang)
        except:
            pass

        try:
            if hotword != '' or hotword != None:
                return hotword
        except:
            pass

    def start_listener(hotwords, timeout = 0.15, number_of_threads = 3, print_=True):
        time = hotword_engine.timer(hotwords[0])
        if number_of_threads == 1:
            thread = threading.Thread(target=hotword_engine.listen, args=(time, timeout, print_,), daemon=True)
            thread.start()
            if print_ == True:
                print("\nNumber of threads: 1\nSTARTED!\n")
        elif number_of_threads == 2:
            thread = threading.Thread(target=hotword_engine.listen, args=(time, timeout, print_,), daemon=True)
            thread.start()
            sleep(time/3)
            thread2 = threading.Thread(target=hotword_engine.listen2, args=(time, (time/4), None, print_,), daemon=True)
            thread2.start()
            if print_ == True:
                print("\nNumber of threads: 2\nSTARTED!\n")
        else:
            thread = threading.Thread(target=hotword_engine.listen, args=(time, timeout, print_,), daemon=True)
            thread.start()
            sleep(time/3)
            thread2 = threading.Thread(target=hotword_engine.listen2, args=(time, (time/4), None, print_,), daemon=True)
            thread2.start()
            sleep(time/3)
            thread2 = threading.Thread(target=hotword_engine.listen2, args=(time, (time/3), None, print_,), daemon=True)
            thread2.start()
            if print_ == True:
                print("\nNumber of threads: 3\nSTARTED!\n")

    def hotword_detection(hotwords: list, language='pt_BR', timeout = 0.15, print_=True):  
        hwds = [] 
        for h in hotwords:
            h = str(h).lower()
            hwds.append(h)
        time = hotword_engine.timer(hwds[0])
        index = 0
        ind_list = []
        det = 0
        if len(aud) != 0:
            index=len(aud)-1
            if len(aud) != index-1:
                if len(aud) > index-1:
                    if index not in ind_list:
                        ind_list.append(index)
                        if len(buffer_clean) > 61:
                            hotword_engine.change_audio([])
                            buffer_clean.clear()
                            index = 0
                            ind_list = []
                            if print_ == True:
                                print("Clearing Temporary Audio for Memory clean:", aud)
                                print("\nEntering on sleep mode for 3s to clear out buffer, and reprocess Google Speech Data.\n")
                            sleep(3)
                            if print_==True:
                                print("\nSlept. Continuing\n")
                        result = hotword_engine.detect(aud[index], lang=language)
                        buffer_clean.append("Some Shit")
                        result = str(result).lower()
                        if (index > 10) and (result not in hwds):
                            hotword_engine.change_audio([])
                            index = 0
                            ind_list = []
                            if print_==True:
                                print("Clearing Temporary Audio:", aud)
                            hotword_engine.state = 0
                            return 0
                        try:
                            if result in hwds:
                                hotword_engine.change_audio([])
                                index = 0
                                ind_list = []
                                if print_ == True:
                                    print("Clearing Temporary Audio after HW Recognition:", aud)
                                hotword_engine.state = 1
                                return 1 
                            else:
                                hotword_engine.state = 0
                                return 0
                        except:
                            pass
                index=index+1
            else:
                index = len(aud)+1
        else:
            index=len(aud)