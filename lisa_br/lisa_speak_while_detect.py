
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
import multiprocessing
from playsound import playsound

hotwords = ['parar', 'para', 'pare', 'pausa', 'pause', 'chega', 'parô', 'parou', 'lisa', 'elisa', 'linda']

def gen():
    playsound("temporary_answer.mp3")
    print("A")

if __name__ == "__main__":
		p = multiprocessing.Process(target=gen)
		p.start()
		from hotword_detection import hotword_engine
		hotword_engine.start_listener(hotwords, print_=False)
		while True:
			try:
				if hotword_engine.hotword_detection(hotwords, print_=False) == 1:
					print("OK") # this line is absolutely necessary for lisa to continue working 
					p.terminate()
					hotword_engine.clear_all()
			except:
				break
