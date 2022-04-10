import argparse

parser = argparse.ArgumentParser('Get Wifi')
parser.add_argument('-s', '--ssid')
parser.add_argument('-p', '--password')
parser.add_argument('-o', '--overwrite')
argv = vars(parser.parse_args())
ssid = argv['ssid']
password = argv['password']
overwrite = argv['overwrite']

print('SSID: ' + str(ssid) + '\nPassword: ' + str(password) + '\nOverwrite: ' + str(overwrite))

path = '/etc/wpa_supplicant/wpa_supplicant.conf'
path = 'wpa_supplicant.conf'

if overwrite == None:
    opt = 'a'
elif overwrite == 'True' or overwrite == 'TRUE':
    opt = 'w'
else:
    opt = 'a'

try:
    with open(str(path), 'a') as file_object:
        file_object.write('\nnetwork={\n')
        file_object.write('        ssid="' + str(ssid).strip() + '"\n')
        file_object.write('        psk="' + str(password).strip() + '"\n')
        file_object.write("}\n")
    print('SUCCESS')
except Exception as e:
    print('Failed\nError: ' + str(e))