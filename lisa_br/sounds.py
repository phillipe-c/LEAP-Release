
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  LISA Sound Service (LSS)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

import os
import sys
import platform

def play(sound):
    if platform.system() == 'Darwin':
        os.system("afplay " + sound)
    elif platform.system() == 'Linux':
        if ".m4a" not in sound:
            os.system("mpg123 " + sound)
        else:
            print("Cannot play sound! m4a fileformat is not supported")
            try:
                from LAS import lisa_core
                lisa_core.save("Could not play sound " + sound + " because it's in m4a format", lisa_core.error_file, "Errors In The Lisa Code:", w_t=True)
                from leds import GradLed
                GradLed.error_msg_led()
            except:
                pass
    else:
        os.system("start " + sound)