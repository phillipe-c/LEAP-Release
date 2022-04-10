
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  LISA Full Code (Using LAS)
# 
#  LISA with stop function while saying
#  
#  Created by Phillipe Caetano.
#  Copyright © 2022 Phillipe Caetano. All rights reserved.
##########################################################

# First thing, we import the necessary modules for the program to work.
# LAS (Lisa API Service) is the module that gives us all the tools we need 
# in order to create a LISA interface
from LAS import lisa_service, lisa_interaction, lisa_prebuilt_voice, lisa_core
import hotword_detection
import os
from playsound import playsound

hotwords = lisa_core.stop_words

# The next thing to do, is to load the AIML kernel and store it in this variable
kernel = lisa_service.load_kernel()

# Calling lisa_service.mode() will return the mode we started in, and will later
# be used to decide which type of text-to-speak engine we will need.
mode = lisa_service.mode()

# If we didn't started the program in gTTS voice mode, we could configure this manually now.
# mode = lisa_service.mode('gTTS')

# Now, we create a function that will be our voice interface.
#def lisa_voice_mode():

# This function underneath loads the listener: an always on background thread 
# that listens for a hotword
lisa_prebuilt_voice.load_listener(play_startup_sound=True)

# This is the loop to detect the hotwords.
while True:

    # We store the user input in this variable, if a hotword is detected.
    user_input = lisa_prebuilt_voice.detect_and_listen()
    
    # We check if the hotword was detected and if the microphone caught something. 
    # If it heard anything after the hotword, we run what's below.
    if user_input != None:
        
        # We display what we just said (the variable user_input).
        print(str(user_input))

        # Now, we process the input and get an answer, that will be stored in this variable.
        answer = lisa_prebuilt_voice.process_and_answer(user_input, kernel)

        # We can finally print the answer we got.
        print(str(answer))

        # And now we say the answer, while setting up the mode that we want.
        lisa_interaction.generate_speech_audio_file_gtts(answer, "temporary_answer.mp3")

        os.system("python3 lisa_LAS_beta_stop_complement.py")
        
# Now we can run the function we just created.
#lisa_voice_mode()
