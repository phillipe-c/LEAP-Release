
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

##########################################################
#  LISA Update Engine (LUE)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

class update_main:

    # The LEAP GitHub
    leap_github_main = "https://github.com/phillipe-c/LEAP-Release/blob/main/update_files/"
    lisa_br_github = "https://github.com/phillipe-c/LEAP-Release/blob/main/lisa_br"

    # Online Files Download Directory
    pip_file_dir = "home/pi/lisa_updates/online/updates_pip.txt"
    pip3_file_dir = "home/pi/lisa_updates/online/updates_pip3.txt"
    apt_file_dir = "home/pi/lisa_updates/online/updates_apt.txt"

    version_online_dir = "home/pi/lisa_updates/online/updates_sys_version.txt"
    update_type_online_dir = "home/pi/lisa_updates/online/updates_sys_version.txt"
    self_dir = "home/pi/lisa_updates/online/update_handler.py"

    online_dir = "home/pi/lisa_updates/online/"

    online_cache = "home/pi/lisa_updates/cache/"

    # Online Updates File
    pip_file = leap_github_main + "updates_pip.txt"
    pip3_file = leap_github_main + "updates_pip3.txt"
    apt_file = leap_github_main + "updates_apt.txt"

    version_online = leap_github_main + "updates_sys_version.txt"
    update_type_online = leap_github_main + "updates_type.txt"
    self_online = leap_github_main + "update_handler.py"

    online_files = [pip_file, pip3_file, apt_file, version_online, update_type_online]

    main_online_files = [version_online, update_type_online]

    # Online Updates List
    pip_list = []
    pip3_list = []
    apt_list = []
    version_online_list = []

    # Local Updates File
    pip_file_local = "home/pi/lisa_updates/local/updates_pip.txt"
    pip3_file_local = "home/pi/lisa_updates/local/updates_pip3.txt"
    apt_file_local = "home/pi/lisa_updates/local/updates_apt.txt"

    version_local = "home/pi/lisa_updates/local/updates_sys_version.txt"
    update_type_local = "home/pi/lisa_updates/online/updates_sys_version.txt"

    # Local Updates List
    pip_local_list = []
    pip3_local_list = []
    apt_local_list = []
    version_local_list = []

    # New Updates List
    pip = []
    pip3 = []
    apt = []
    version = []

    # Downloads the online files
    def retrieve_online_files():
        # Removes the lisa_br/online folder to prevent any mistakes
        import os
        os.system('sudo rm -r ' + update_main.online_dir)
        os.system('sudo mkdir ' + update_main.online_dir)

        # Loops through all files, downloading each
        for i in update_main.online_files:
            os.system('sudo cd '+ update_main.online_dir +' && sudo wget ' + i)

    # Gets the latest packages (only the newest) and stores in New Updates List
    def get_latest_packages_list():
        ## LOCAL FILES
        # Saving pip_file_local to list
        with open(update_main.pip_file_local, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.pip_local_list.append(l)

        # Saving pip3_file_local to list
        with open(update_main.pip3_file_local, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.pip3_local_list.append(l)

        # Saving apt_file_local to list
        with open(update_main.apt_file_local, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.apt_local_list.append(l)

        # Saving Local Version
        with open(update_main.version_local, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.version_local_list.append(l)

        ## ONLINE FILES
        # Saving pip_file_dir to list
        with open(update_main.pip_file_dir, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.pip_list.append(l)

        # Saving pip3_file_dir to list
        with open(update_main.pip3_file_dir, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.pip3_list.append(l)

        # Saving apt_file_dir to list
        with open(update_main.apt_file_dir, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.apt_list.append(l)

        # Saving Version
        with open(update_main.version_online_dir, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                update_main.version_online_list.append(l)

    # Function that saves only the packages that are not in the local files
    def make_difference_of_packages():
        # Pip Packages
        update_main.pip = [item for item in update_main.pip_list if item not in update_main.pip_local_list]
        
        # Pip3 Packages
        update_main.pip3 = [item for item in update_main.pip3_list if item not in update_main.pip3_local_list]

        # APT Packages
        update_main.apt = [item for item in update_main.apt_list if item not in update_main.apt_local_list]

    # Function to check if there really is a new version
    def new_update(version_online = "home/pi/lisa_updates/cache/updates_sys_version.txt"):
        import os
        os.system('sudo rm -r ' + update_main.online_cache)
        os.system('sudo mkdir ' + update_main.online_cache)

        # Loops through all files, downloading each
        for i in update_main.main_online_files:
            os.system('sudo cd '+ update_main.online_cache +' && sudo wget ' + i)

        local_version = []
        online_version = []

        local_type = []
        online_type = []

        # Saving Local Version
        with open(update_main.version_local, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                local_version.append(l)

        # Saving Online Version
        with open(update_main.version_online_dir, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                online_version.append(l)

        # Saving Local Version
        with open(update_main.update_type_local, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                local_type.append(l)

        # Saving Online Version
        with open(update_main.update_type_online_dir, "r") as file_obj:
            f = file_obj.readlines()
            for l in f:
                l = l.strip()
                online_type.append(l)

        difference = [item for item in online_version if item not in local_version]

        new = False
        type_ = None # Can

        if difference == []:
            new = False
        else:
            new = True
            try:
                type_ = online_type[0]
                version = online_version[0]
                update_main.version.append(version)

            except Exception as e:
                print(e)
                version = None
                type_ = None
        
        return [new, type_, version]

    # Function that installs new packages
    def install_packages():
        state = update_main.new_update()
        import os

        if state[0] == True:

            update_main.retrieve_online_files()
            update_main.get_latest_packages_list()
            update_main.make_difference_of_packages()

            if state[1] == "entire_lisa":
                os.system('sudo cd /home/pi && sudo rm -r lisa_br && sudo wget ' + update_main.lisa_br_github)
                for py in update_main.pip:
                    print("\nInstalling {p}\n".format(p=py))
                    os.system('sudo pip install ' + str(py))
                
                for py in update_main.pip3:
                    print("\nInstalling {p}\n".format(p=py))
                    os.system('sudo pip3 install ' + str(py))

                for pack in update_main.apt:
                    print("\nInstalling {p}\n".format(p=pack))
                    os.system('sudo apt-get install ' + str(pack))
            
            else:
                for py in update_main.pip:
                    print("\nInstalling {p}\n".format(p=py))
                    os.system('sudo pip install ' + str(py))
                
                for py in update_main.pip3:
                    print("\nInstalling {p}\n".format(p=py))
                    os.system('sudo pip3 install ' + str(py))

                for pack in update_main.apt:
                    print("\nInstalling {p}\n".format(p=pack))
                    os.system('sudo apt-get install ' + str(pack))
        
    # Gets Version
    def get_version():
        if update_main.version == []:
            return update_main.new_update()[2]
        else:
            return update_main.version[0]
        
class update_service:
    def update():
        update_main.install_packages()
