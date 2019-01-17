### IMPORTANT: PLEASE STRETCH CONSOLE BEFORE RUNNING. 
### LOGIN INFO FOR TESTING PURPOSES:
                                    # AGENT NUMBER: admin
                                    # Dept. Password: adminpass
                                                      
#--- Imports
from colorama import init, Fore, Style # Imports Fore and style from Colorama. Allows for colored text. (https://pypi.org/project/colorama/)
import binascii # Imports Binascii module. Allows for conversion between number systems and ASCII. (https://docs.python.org/3.1/library/binascii.html)
import sys
import os
import random
import urllib.request # Imports Urllib.request module, allows for opening urls, reading the page source from urls amongst many other things. (https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
from termcolor import cprint # Imports cprint from the termcolor module. Allows for bolded, underlined and blinking text. (https://pypi.org/project/termcolor/)
from math import radians, cos, sin, sqrt, atan2 # Imports radians, cos, sin, sqrt and atan2 from the math module (https://docs.python.org/3/library/math.html)
import time # Imports time module. Allows for the delayed printing of text. (https://docs.python.org/3/library/time.html)

init(convert=True)
#--- Logging
import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program.')
#--- Launch Sequence
logging.debug('Launch screen assignment.')
launchScreen = ''' 
  ______ ____ _____             _____                                          _   _______                  _             _ 
 |  ____|  _ \_   _|           / ____|                                        | | |__   __|                (_)           | |
 | |__  | |_) || |    ______  | |     ___  _ __ ___  _ __ ___   __ _ _ __   __| |    | | ___ _ __ _ __ ___  _ _ __   __ _| |
 |  __| |  _ < | |   |______| | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |    | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
 | |    | |_) || |_           | |___| (_) | | | | | | | | | | | (_| | | | | (_| |    | |  __/ |  | | | | | | | | | | (_| | |
 |_|    |____/_____|           \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|    |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|

'''
# Assigns the launch screen header to the variable launchScreen.  

logging.debug('Variable assignment')
#--- Variable Assignment
acceptableAgentNum = ['5','6','7','admin'] # Acceptable inputs for an agent number.
acceptableDeptPass = ['9', '8','12','adminpass'] # Acceptable inputs for an department password. 
acceptableReturnMenu = ['yes'] # Acceptable inputs when the user is asked if they want to return to the menu.
remain = ['no'] # Acceptable inputs that will restart the function when the user is asked if they want to return to the menu. 
acceptableMenuOptions = ['1','2','3','4','5', '6', '7'] # Acceptable inputs for the menu options.
acceptableMenu = ['menu'] # Acceptable inputs, when any one of these are typed into a main input it will return the user back to the menu. 
acceptableBackupMenu = ['1', '2']

failedAttempts = {'failed': 0}

#--- Menu
logging.debug('Start of function Menu.')
def menu(): # Defines function menu. 
  '''
  A menu of options. 
  
  This function will print out a menu of options for the user to select, 
  it will then ask the user what option they would like to select and then 
  call a function based upon the option they selected. 

  Parameters
  ----------
  none
  
  Returns
  -------
  string 
    The input for menuAsk. 
  '''
  logging.debug('Displaying menu output.')
  print() # Prints blank space. 
  print(Style.BRIGHT + Fore.BLUE + "1. " + Style.RESET_ALL + "Encrypt/Decode Messages.") # Prints menu option #1, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "2. "+ Style.RESET_ALL + "Request backup/evacuation.") # Prints menu option #3, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "3. "+ Style.RESET_ALL + "Locate an IP Address.") # Prints menu option #4, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "4. "+ Style.RESET_ALL + "Detect financial fraud.") # Prints menu option #5, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "5. "+ Style.RESET_ALL + "Create/Find Hidden Messages.")
  print(Style.BRIGHT + Fore.BLUE + "6. "+ Style.RESET_ALL + "Logout.")
  print(Style.BRIGHT + Fore.GREEN + "Note: "+ Style.RESET_ALL + 'If you select the wrong option, type menu in an input to return to the main menu.') # Prints menu option #6, makes the option number blue.
  print() # Prints blank space. 
  
  menuAsk = input("What option would you like to select?:") # Asks the user what option they would like to select. 
  print() # Prints blank space. 
  
 #--- If Statements to call functions, part of menu(). 
  if menuAsk not in acceptableMenuOptions: # If the input for menuAsk isn't a number between 1 and 5 (acceptableMenuOptions), the follwing code is exectuted.
   print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, restarting menu.') # Prints error message. 
   time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
   print() # Prints a blank space.
   os.system('cls') # Clears the console.
   print() # Prints a blank space.
   print(launchScreen) # Prints the launch screen
   menu() # Calls the menu function. 
   logging.debug('Determining menu option selected.')
    #- Menu Option #1 (Decode encrypted messages.).
  elif menuAsk == str('1'): # If the input for menuAsk is 1, the following code is executed.
    encryptDecodeMenu() # Calls the function unhex (converts Hexadecimal to ASCII)
    
    #- Menu Option #2 (Encrypt messages.)
  elif menuAsk == str('2'): # If the input for menuAsk is 2, the following code is executed.
    backupEvac() # Calls the function asciiHex.
    
    #- Menu Option #3 (Request backup/evacuation)
  elif menuAsk == str('3'): # If the input for menuAsk is 3, the following code is executed.
    ipLocate()() # Calls the function backupEvac. 
    
    #- Menu Option #4 (Locate an IP Address.)
  elif menuAsk == str('4'): # If the input for menu ask is 4, the following code is executed.
    taxLaunder() # Calls the function ipLocate.
    
    #- Menu Option #5 (Create/Find Hidden Mes)
  elif menuAsk == str('5'): # If the input for menu ask is 5, the following code is executed. 
    hiddenMessages() # Calls the function hiddenMessages()
  
  elif menuAsk == str('6'):
    logoutConfirm = input(Fore.GREEN + 'Confirm -  ' + Style.RESET_ALL + 'Are you sure you want to logout?\n')
    if logoutConfirm == str(''):
      print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Logging out, standby.')
      time.sleep(2)
      sys.exit()
      
    if logoutConfirm.lower() in acceptableReturnMenu:
      print(Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Logging out, standby.')
      time.sleep(2)
      sys.exit()
    
    elif logoutConfirm.lower() in remain:
      print(Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to menu, standby.')
      time.sleep(2)
      menu()
    
    else:
      print(Fore.RED + 'Error: ' + Style.RESET_ALL + 'Unacceptable input, returning to menu.')
      time.sleep(2)
      menu()
    
  #assert isinstance(menuAsk, string), 'Expecting a string!'
    
  return menuAsk # Returns menuAsk (Causes function to exit).


#--- Converts Hexadecimal to ASCII
logging.debug('Start of function unHex')
def unHex(): # Defines the function "unHex"
  '''
  Converts hexadecimal to ASCII. 
  
  This function will take an input from the user in a Hexadecimal format
  and convert it to human readable text. 

  Parameters
  ----------
  none
  
  Returns
  -------
  string
    The input for unHexMenu. 
  '''
  try: # The program will attempt to run this code, if an error message is given it will run the code under "except:"
   logging.debug('Requesting user input.')
   hexInput = input("Please enter your encoded hex message:") # Prompts user for hexadecimal input.
   hexOutput = hexInput.replace(" ","") # Deletes spaces in the hexadecimal input to avoid error with decoding.
   hexToAscii = binascii.unhexlify(str(hexOutput)) # Takes the hexinput with deleted spaces (hexouput) and converts it to ASCII.
   print('Your message has been decrypted: ' + hexToAscii.decode('utf-8')) # Decodes the converted  input (hextoascii) to remove unwanted prefixes, prints it. 
   print() # Prints blank space. 
  
  except (binascii.Error, UnicodeDecodeError): # If an error message is given when the code under "try:" is ran, the following code will be executed. 
    if hexInput.lower() in acceptableMenu: # If the user types "Menu" or "menu" in hexInput the following code will execute.
     print() # Prints a blank space.
     print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to main menu, standby.') # Prints a notification message.
     time.sleep(3) # Adds a 3 second delay before the next line of code is executed.
     os.system('cls') # Clears the console.
     print() # Prints a blank space.
     print(launchScreen) # Prints the launch screen.
     menu() # Calls the menu function.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.RED + 'Error: ' + Style.RESET_ALL + 'Invalid hexadecimal string entered, restarting function.') # Prints a error message. 
    time.sleep(3) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console. 
    print(launchScreen) # Prints the launch screen.
    unHex() # Calls the function unHex
  
  unHexMenu = input('Would you like to go back to the main menu?: ') # Asks if the user would like to go back to the main menu. 
  #assert isinstance(unHexMenu, str), 'Expecting string!'
  if unHexMenu.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.
    
  elif unHexMenu.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
    print() # Prints a blank space.
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the console. 
    print(launchScreen) # Prints the launch screen
    unHex() # Calls the function asciiHex
    
  else: # If the user's input isn't in acceptableReturnMenu or remain the following code is executed.
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, returning to menu.') # Prints an error message.
    print() # Prints a blank space.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu funciton.
  return unHexMenu # Returns the function unHexMenu (Exits the function)

#--- Converts ASCII to Hexadecima
logging.debug('Start of asciiHex function.')
def asciiHex(): # Defines the function asciiHex
  '''
  Converts ASCII to Hexadecimal.
  
  This function will take a normal, human readable text from the user
  and convert it to a hexadecimal format. 

  Parameters
  ----------
  none
  
  Returns
  -------
  string
    The input of asciiHexMenu
  '''
  try: # The program will attempt to run this code, if an error message is given it will run the code under "except:"
   logging.debug('Requesting user input.')
   asciiInput = input("Please enter the message you'd like to encrypt:") # Prompts user for ASCII input.
   #assert isinstance(asciiInput, str), 'Expecting string!'
  
   if asciiInput.lower() in acceptableMenu: # If the user types "Menu" or "menu" into asciiInput the following code will be executed.
     print() # Prints a blank space.
     print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to main menu, standby.') # Prints a notification message.
     time.sleep(3) # Adds a 3 second delay before the next line of code is executed.
     os.system('cls') # Clears the console.
     print() # Prints a blank space.
     print(launchScreen) # Prints the launch screen.
     menu() # Calls the menu function.
              
   else: # If the user didn't type "Menu" or "menu" in asciiInput the following code is executed. 
    logging.debug('Encoding input.')
    asciiOutput = asciiInput.encode('utf-8') # Encodes user's inputs to bytes such that the input can be used as a variable for binascii.hexlify.
    asciiToHex = binascii.hexlify(asciiOutput) # Converts the users encoded input to a hexadecimal.
    print('Your message has been encoded: ' + asciiToHex.decode('utf-8')) # Decodes the converted input (asciiToHex) to remove unwanted prefixes, prints it.
    print() # Prints a blank space. 
  
  except binascii.Error: # If an error is given when the code under "try" is ran, the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.RED + 'Error: ' + Style.RESET_ALL + 'Invalid hexadecimal string entered, restarting function.') # Prints a error message. 
    time.sleep(3) # Adds a 3 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console. 
    print(launchScreen) # Prints the launch screen.
    unHex() # Calls the function unHex
  
  logging.debug('Requesting menu return input.')
  asciiHexMenu = input('Would you like to go back to the main menu?: ') # Asks if the user would like to go back to the main menu. 
  #assert isinstance(asciiHexMenu, str), 'Expecting string!'
  if asciiHexMenu.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
    os.system('cls') # Clears the console. 
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.
    
  elif asciiHexMenu.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    asciiHex() # Calls the function asciiHex
    
  else: # If the user's input isn't in acceptableReturnMenu or remain the following code is executed.
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, returning to menu.') # Prints an error message.
    print() #  Prints a blank nessage.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launchScreen
    menu() # Calls the menu function
  return asciiHexMenu # Returns the function unHexMenu (Exits the function)

def encryptDecodeMenu():
  os.system('cls')
  print(launchScreen)
  print(Style.BRIGHT + Fore.BLUE + '1. ' + Style.RESET_ALL + 'Encrypt Messages. ' ) # Prints menu option #1, makes the number blue.
  print(Style.BRIGHT + Fore.BLUE + '2. ' + Style.RESET_ALL + 'Decode Messages. ' ) # Prints menu option #2, makes the number blue.
  print() # Prints blank message.
  
  encryptDecodeAsk = input('What input would you like to select?:')
    
  if encryptDecodeAsk.lower() in acceptableMenu: # If the user types "Menu" or "menu" into asciiInput the following code will be executed.
     print() # Prints a blank space.
     print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to main menu, standby.') # Prints a notification message.
     time.sleep(3) # Adds a 3 second delay before the next line of code is executed.
     os.system('cls') # Clears the console.
     print() # Prints a blank space.
     print(launchScreen) # Prints the launch screen.
     menu() # Calls the menu function.  
      
  elif encryptDecodeAsk == str('1'):
    print() # Prints blank space.
    os.system('cls') # Clears terminal.
    time.sleep(1) # Adds a one second delay before the next line is executed.
    print(launchScreen) # Prints the launch screen.
    print() # Prints blank message.
    asciiHex() # Calls function asciiHex.
    
  elif encryptDecodeAsk == str('2'):
    print() # Prints blank space.
    os.system('cls') # Clears terminal
    time.sleep(1) # Adds a one second delay before the next line is executed.
    print(launchScreen) # Prints the launch screen.
    print() # Prints blank message.
    unHex() # Calls function asciiHex.
  
  else:
    print(Fore.RED + 'Error: ' + Style.RESET_ALL + 'Unacceptable input, restarting function.')
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
    print() # Prints a blank space.
    os.system('cls') # Clears the console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launch screen
    menu() # Calls the menu function. 
  

#--- Request backup/evacuation.
logging.debug('Start of backup/evac function.')
def backupEvac(): # Defines the function backupEvac
  '''
  Requests a backup or evacuation from FBI Headquarters..
  
  This function will find the users IP Address and use said IP Address to determine the approximate
  distance between the user and the FBI headquarters via the Haversine formula. The function will then either request for backup
  or an evacuation team based upon the users input. 
  
  Parameters
  ----------
  none
  
  Returns
  -------
  backupEvacMenu
    The input of backupEvacMenu
    
  '''
  
# --- BACKUP
  logging.debug('Start of backup.')
  print(Style.BRIGHT + Fore.BLUE + '1. ' + Style.RESET_ALL + 'Request backup. ' ) # Prints menu option #1, makes the number blue.
  print(Style.BRIGHT + Fore.BLUE + '2. ' + Style.RESET_ALL + 'Request an evacuation. ' ) # Prints menu option #2, makes the number blue.
  print()
  backupAsk = input('What option would you like to select?: ') # Asks the user what option they would like to select
  #assert isinstance(backupAsk, str), 'Expecting string!'
  
  if backupAsk.lower() in acceptableMenu: # If the user inputs "Menu" or "menu" for backupAsk the following code is executed, 
    print() # Prints a blank space.
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to main menu, standby.') # Notification message.
    time.sleep(3)  # Adds a 3 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launchScreen.
    menu() # Calls the menu function
    
  else: # If the user doesn't input "Menu" or "menu" for backupAsk the following code is executed. 
   if backupAsk == str('1'): # If the user selects option #1 the following code is execute.

    print() # Prints blank space.
    cprint('Requesting Backup', attrs=['blink']) # Prints the requesting backup header, while blinking. 
    logging.debug('Fetching ip location data from API.')
  
    for ipAddress in urllib.request.urlopen('https://ipapi.co/ip'): # Reads the page source of the url, grabs the IP Address of the user.
     ipAddressOutput = ipAddress.decode('utf-8') # Decodes the IP Address to avoid unwanted unwanted prefixes.
  
    for ipCountry in urllib.request.urlopen('https://ipapi.co/country_name'): # Reads the page source of the url, grabs the country the user resides in based upon their IP Address.
     ipCountryOutput = ipCountry.decode('utf-8') # Decodes the country name to avoid unwanted prefixes.
   
    for ipCity in urllib.request.urlopen('https://ipapi.co/city'): # Reads the page source of the url, grabs the city the user resides in based upon their IP Address.
     ipCityOutput = ipCity.decode('utf-8') # Decodes the city name to avoid unwanted prefixes.
  
    for ipRegion in urllib.request.urlopen('https://ipapi.co/region'): # Reads the page source of the url, grabs the region the user resides in based upon their IP Address.
     ipRegionOutput = ipRegion.decode('utf-8') # Decodes the region name to avoid unwanted prefixes.
  
    for ipPostal in urllib.request.urlopen('https://ipapi.co/postal'): # Reads the page source of the url, grabs the postal code the user resides in based upon their IP Address.
     ipPostalOutput = ipPostal.decode('utf-8') # Decodes the postal code to avoid unwanted prefixes.
   
    for ipLatLong in urllib.request.urlopen('https://ipinfo.io/loc'): # Reads the page source of the url, grabs the lattitude and longitude of the user based upon the geo location of the user's ip address.
     ipLatLongOutput = ipLatLong.decode('utf-8') # Decodes the lattitude and longitude to avoid unwanted prefixes. 
     latOutput = float(ipLatLongOutput[0:7]) # Seperates the lattitude from the longitude in the string and converts it to a float value.
     longOutput = float(ipLatLongOutput[8:16]) # Seperates the longitude from the lattitude in the string and converts it to a float value.
  
  #--- Haversine Formula Pre-requisites. 
    logging.debug('Defining variables for haversine formula.')
    R = 6371 # Radius of the Earth (KM).
    #assert R == 6371, 'Incorrect radius!'
    lat1 = radians(38.895370) # Lattitude for FBI Headquarters, converts value to a radian.
    #assert lat1 == radians(38.895370), 'Incorrect lattitude for headquarters!'
    lon1 = radians(-77.024971) # Longitude for FBI Headquarters, converts value to a radian.
    #assert lon1 == radians(-77.024971), 'Incorrect longitude for headquarters!'
    lat2 = radians(latOutput) # Converts the lattitude of the user to a radian.
    lon2 = radians(longOutput) # Converts the longitude of the user to a radian.
    dlon = lon2 - lon1 # Subtracts the 2nd longitude point from the first longitude point, assigns it to a variable.
    dlat = lat2 - lat1 # Subtracts the 2nd lattitude point from the first lattitude point, assigns it to a vairable. 

  #--- Haversine Formula
    ''' 
     Formula to calculate the distance (KM) between two lattitude and longitude points.
     
     This formula is used to calculate the distance between the lattitude and longitude coordinates of the FBI Headquarters
     and the users geo location determined by their IP Address.
     
     Source: http://mathforum.org/library/drmath/view/51879.html (Explanation and demonstration of the Formula)
    '''
    logging.debug('Executing haversine formula.')
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2 # Straight line distance. 
    c = 2 * atan2(sqrt(a), sqrt(1-a)) # Great circle distance. 
    distance = R * c  # Total distance between the coordinates. 
    distanceOutput = str(R * c) # Converts the total distance to a string.
    travelTime = str(distance/100) # Determines the time in hours for backup to arrive, assuming the 'backup' is travelling 100 KM/h
    
    print() # Prints blank space. 
    print('IP Address: ' + ipAddressOutput) # Prints the user's decoded IP Address. 
    print() # Prtins blank space. 
    print('Coordinates: ' + str(latOutput) + ', ' + str(longOutput)) # Prints the users decoded lattitude and longitude coordinates based upon the geo location of their ip address. 
    print('Location: ' + str(ipCountryOutput) + ', ' + str(ipRegionOutput) + ', ' + str(ipCityOutput) + ', ' + str(ipPostalOutput) + '.') # Prints the users decoded country, region, city and postal code. 
    print('Distance from FBI Headquarters: ' + str(distanceOutput[0:5]) + ' KM') # Prints the distance the user is from the FBI Headquarters to the nearest hundreth. 
    print() # Prints blank space. 
    print('Backup is on the way, ETA: ' + str(travelTime[0:5]) + ' Hours' ) # Prints the time estimated in hours till the backup arrives. 

#--- EVACUATION
  logging.debug('Start of evacuation')
  if backupAsk in str('2'): # If the user selects option #2 the following code is executed. 
  
   print() # Prints blank space.
   cprint('Requesting Evacuation', attrs=['blink']) # Prints the requesting evacuation header, while blinking. 
   logging.debug('Fetching ip location data from API')

   for ipAddress in urllib.request.urlopen('https://ipapi.co/ip'): # Reads the page source of the url, grabs the IP Address of the user.
    ipAddressOutput = ipAddress.decode('utf-8') # Decodes the IP Address to avoid unwanted unwanted prefixes.
  
   for ipCountry in urllib.request.urlopen('https://ipapi.co/country_name'): # Reads the page source of the url, grabs the country the user resides in based upon their IP Address.
    ipCountryOutput = ipCountry.decode('utf-8') # Decodes the country name to avoid unwanted prefixes.
   
   for ipCity in urllib.request.urlopen('https://ipapi.co/city'): # Reads the page source of the url, grabs the city the user resides in based upon their IP Address.
    ipCityOutput = ipCity.decode('utf-8') # Decodes the city name to avoid unwanted prefixes.
  
   for ipRegion in urllib.request.urlopen('https://ipapi.co/region'): # Reads the page source of the url, grabs the region the user resides in based upon their IP Address.
    ipRegionOutput = ipRegion.decode('utf-8') # Decodes the region name to avoid unwanted prefixes.
  
   for ipPostal in urllib.request.urlopen('https://ipapi.co/postal'): # Reads the page source of the url, grabs the postal code the user resides in based upon their IP Address.
    ipPostalOutput = ipPostal.decode('utf-8') # Decodes the postal code to avoid unwanted prefixes.
   
   for ipLatLong in urllib.request.urlopen('https://ipinfo.io/loc'): # Reads the page source of the url, grabs the lattitude and longitude of the user based upon the geo location of the user's ip address.
    ipLatLongOutput = ipLatLong.decode('utf-8') # Decodes the lattitude and longitude to avoid unwanted prefixes. 
    latOutput = float(ipLatLongOutput[0:7]) # Seperates the lattitude from the longitude in the string and converts it to a float value.
    longOutput = float(ipLatLongOutput[8:16]) # Seperates the longitude from the lattitude in the string and converts it to a float value.
  
  #--- Haversine Formula Pre-requisites. 
    logging.debug('Haversine formula variable assignment.')
    R = 6371 # Radius of the Earth (KM).
    #assert R == 6371, 'Incorrect radius!'
    lat1 = radians(38.895370) # Lattitude for FBI Headquarters, converts value to a radian.
    #assert lat1 == radians(38.895370), 'Incorrect lattitude for headquarters!'
    lon1 = radians(-77.024971) # Longitude for FBI Headquarters, converts value to a radian.
    #assert lon1 == radians(-77.024971), 'Incorrect longitude for headquarters!'
    lat2 = radians(latOutput) # Converts the lattitude of the user to a radian.
    lon2 = radians(longOutput) # Converts the longitude of the user to a radian.
    dlon = lon2 - lon1 # Subtracts the 2nd longitude point from the first longitude point, assigns it to a variable.
    dlat = lat2 - lat1 # Subtracts the 2nd lattitude point from the first lattitude point, assigns it to a vairable. 
    
  #--- Haversine Formula
    ''' 
     Formula to calculate the distance (KM) between two lattitude and longitude points.
     
     This formula is used to calculate the distance between the lattitude and longitude coordinates of the FBI Headquarters
     and the users geo location determined by their IP Address.
     
     Source: http://mathforum.org/library/drmath/view/51879.html (Explanation and demonstration of the Formula)
    '''
    logging.debug('Haversine formula variable execution.')
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2 # Straight line distance. 
    c = 2 * atan2(sqrt(a), sqrt(1-a)) # Great circle distance. 
    distance = R * c  # Total distance between the coordinates. 
    distanceOutput = str(R * c) # Converts the total distance to a string.
    travelTime = str(distance/100) # Determines the time in hours for the evacuation team to arrive, assuming the 'backup' is travelling 100 KM/h
    
    print() # Prints blank space. 
    print('IP Address: ' + ipAddressOutput) # Prints the user's decoded IP Address. 
    print() # Prints a blank space. 
    print('Coordinates: ' + str(latOutput) + ', ' + str(longOutput)) # Prints the users decoded lattitude and longitude coordinates based upon the geo location of their ip address. 
    print('Location: ' + str(ipCountryOutput) + ', ' + str(ipRegionOutput) + ', ' + str(ipCityOutput) + ', ' + str(ipPostalOutput) + '.') # Prints the users decoded country, region, city and postal code. 
    print('Distance from FBI Headquarters: ' + str(distanceOutput[0:5]) + ' KM') # Prints the distance the user is from the FBI Headquarters to the nearest hundreth. 
    print() # Prints blank space. 
    print('An evacuation team is on the way, ETA: ' + str(travelTime[0:5]) + ' Hours' ) # Prints the time estimated in hours till the evacuation team arrives. 
    
  elif backupAsk.lower() not in acceptableBackupMenu and acceptableMenu: # If the user doesn't enter a word in either acceptableBackupMenu and acceptableMenu, the following code is executed. 
    print() # Prints a blank space.
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, restarting function.') # Prints an error message. 
    print() # Prints a blank space.
    time.sleep(2)# Adds a 2 second delay before the next line of code is executed. 
    print() # Prints a blank space. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launchScreen
    backupEvac() # Calls the function backupEvac.
  print() # Prints a blank space. 
  
  #--- MENU RETURN
  logging.debug('Requesting menu return input.')
  backupEvacMenu = input('Would you like to go back to the main menu?: ') # Asks if the user would like to go back to the main menu. 
  #assert isinstance(backupEvacMenu, str), 'Expecting string!'
  
  if backupEvacMenu.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
    os.system('cls') # Clears the terminal/console.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.
    
  elif backupEvacMenu.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message. 
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    backupEvac() # Calls the function backupEvac
    
  else: # If the user's input isn't in acceptableReturnMenu or remain the following code is executed.
    print() # Prints a blank space. 
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, returning to menu.') # Prints an error message.
    print() # Prints a blank message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the onsole.
    print() # Prints a blank space
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the function menu.
  return backupEvacMenu # Returns backupEvacMenu (Exits the function)
  
  
#--- Track an IP Address
logging.debug('Start of function ip locate.')
def ipLocate():
  '''
  Determines the geolocation of an IP Address.
  
  This function will prompt the user to input an IP Address, the function will then
  output information about the geolocation of said IP Address (Approximate coordinates, country, city, region, postal code.)

  Parameters
  ----------
  none
  
  Returns
  -------
  string
    The input of ipLocateMenu
  '''
  logging.debug('Requesting user for ip input.')
  ipLocateAsk = input("Please enter the IP Address you would like to locate: ") # Prompts the user to input an IP Address.
  #assert isinstance (ipLocateAsk, str), 'Expecting string!'
  
  if ipLocateAsk in acceptableMenu:
    print()
    os.system('cls')
    print(launchScreen)
    menu()
  
  try: # The program will attempt to run the following code, if an error is given the code under "except:"i will be executed.
   logging.debug('Fetching ip location data from API.')
   for ipCountry in urllib.request.urlopen('https://ipapi.co/' + ipLocateAsk + '/country_name'): # Reads the page source of the url, grabs the country of the ip address given. 
     ipCountryOutput = ipCountry.decode('utf-8') # Decodes the country name to avoid unwanted prefixes.
    
   for ipCity in urllib.request.urlopen('https://ipapi.co/' + ipLocateAsk + '/city'): # Reads the page source of the url, grabs the city of the ip address given. 
     ipCityOutput = ipCity.decode('utf-8') # Decodes the city name to avoid unwanted prefixes.
  
   for ipRegion in urllib.request.urlopen('https://ipapi.co/' + ipLocateAsk + '/region'): # Reads the page source of the url, grabs the region of the ip address given. 
     ipRegionOutput = ipRegion.decode('utf-8') # Decodes the region name to avoid unwanted prefixes.
  
   for ipPostal in urllib.request.urlopen('https://ipapi.co/' + ipLocateAsk + '/postal'): # Reads the page source of the url, grabs the postal code of the ip address given. .
     ipPostalOutput = ipPostal.decode('utf-8') # Decodes the postal code to avoid unwanted prefixes.  
  
   for ipLatLong in urllib.request.urlopen('https://ipinfo.io/' + ipLocateAsk + '/loc'): # Reads the page source of the url, grabs the lattitude and longitude of the ip address given. 
     ipLatLongOutput = ipLatLong.decode('utf-8') # Decodes the lattitude and longitude to avoid unwanted prefixes. 
     latOutput = float(ipLatLongOutput[0:7]) # Seperates the lattitude from the longitude in the string and converts it to a float value.
     longOutput = float(ipLatLongOutput[8:16]) # Seperates the longitude from the lattitude in the string and converts it to a float value.
     
  except urllib.error.HTTPError: # If an urllib error is given when the code under "try:" is attempted to be ran, the following code will be executed. 
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.RED + 'Error: ' + Style.RESET_ALL + 'Invalid IP Address entered, restarting function.') # Prints a error message. 
    time.sleep(3) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    ipLocate() # Calls the function ipLocate
 
  print() # Prints a blank space.
  cprint('Tracking IP Address...', attrs=['blink']) # Prints the requesting backup header, while blinking. 
  print() # Prints a blank space.
  time.sleep(3) # Adds a 3 second delay before the next line of code is executed. 
  print('Coordinates: ' + str(latOutput) + ', ' + str(longOutput)) # Prints the users decoded lattitude and longitude coordinates based upon the geo location of the ip address providws.. 
  print('Location: ' + str(ipCountryOutput) + ', ' + str(ipRegionOutput) + ', ' + str(ipCityOutput) + ', ' + str(ipPostalOutput) + '.') # Prints the   country, region, city and postal code  of the ip address given.
  
  print() # Prints a blank space. 
  ipLocateMenu = input('Would you like to go back to the main menu?: ') # Asks if the user would like to go back to the main menu. 
  #assert isinstance(ipLocateMenu, str), 'Expecting string!'
  
  if ipLocateMenu.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.
    
  elif ipLocateMenu.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message. 
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    ipLocate() # Calls the function ipLocate
    
  else: # If the user's input isn't in acceptableReturnMenu or remain the following code is executed.
    print() # Prints a blank space. 
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, returning to menu.') # Prints an error message.
    print() # Prints a blank message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the function menu.
  return ipLocateMenu # Returns ipLocateMenu (Exits the function)
  
  
#--- Detect financial fraud.
logging.debug('Start of function taxEvade.')
def taxEvade(netIncome, taxPaid, taxRate): # Defines the function taxEvade with the parameters netIncome and taxPaid
  '''
  Determines if tax evasion has occured. 
  
  This function will determine if tax evasion has occured, based upon the 
  net income, amount of taxes paid and tax rate provided by the users input. 

  Parameters
  ----------
  netIncome: float
    The total amount of income the suspect has made.
  
  taxPaid: float
    The total amount of income tax that the suspect has paid.
    
  taxRate: float
    The income tax rate of the area the suspect resides in. 
  
  Returns
  -------
  none
  '''
  taxRateEq = taxRate/100 # Converts the tax rate to a percentage. 
  
  taxPayConfirm = netIncome * taxRateEq # Amount of taxes that should of been paid.
  missingTax = taxPayConfirm - taxPaid # The amount of taxes that haven't been paid (if any).
  overTax = str(missingTax) # Assigns the string of missingTax to the variable overTax.
  overTaxOutput = overTax.replace('-', '') # Replaces the - in overTax, assigns new value to overTaxOutput

  logging.debug('Determining tax status.')
  if taxPaid < taxPayConfirm: # If the amount of taxes paid, is less than the amount of taxes that should've been paid the following code is executed. 
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.RED + 'Alert: ' + Style.RESET_ALL + 'Tax evasion has been detected '+ '$' + str(missingTax) + ' has not been paid.') # Prints an error message, along with the amount of taxes not paid. 
  
  elif taxPaid == taxPayConfirm: # If the amount of taxes is equal to what should've been paid the following code is executed. 
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: '+ Style.RESET_ALL + 'No tax evasion detected') # Prints a notification message. 
  
  else: # If the taxes paid were greater then what should've been paid the following code is executed. 
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: '+ Style.RESET_ALL + 'No tax evasion detected, taxes have been overpaid by $' + str(overTaxOutput)) # Prints a notification message with the amount of taxes overpaid. 
  
  #assert taxRate <= 100, 'Expecting tax rate less than 100!'

logging.debug('Start of function moneyLaunder.')
def moneyLaunder(reportedNetIncome, revenue, expenses):  # Defines the function moneyLaunder with parameters reportedNetIncome, revenue and expenses.
  '''
  Determines if money laundering has occured. . 
  
  This function will determine if money laundering has occured, based upon the 
  net income, revenue and expenses of the businesses inputted by the user. 

  Parameters
  ----------
  reportedNetIncome: float
    The total amount of net income the businesses has recorded on their financial statements for the fiscal period. 
  
  revenue: float
    The total amount of revenue the businesses has made in the fiscal period. 
    
  expenses: float
    The costs occured to achieve the revenue the businesses earned in the fiscal period. 
  
  Returns
  -------
  none
  '''
  netIncomeConfirm = int(revenue) - int(expenses) # Calculates what should be the net income.
  incomeOutput = int(reportedNetIncome) - netIncomeConfirm # Subtracts the reportoed net incoem by what should actually be the net income. 
  incomeError = str(incomeOutput)
  incomeErrorOutput = incomeError.replace('-','')
  #assert isinstance (incomeErrorOutput, str), 'Expecting string!'
  
  logging.debug('Determining net income status.')
  if reportedNetIncome > netIncomeConfirm: # If the reported net income is greater then the actual net income the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.RED + 'Alert: ' + Style.RESET_ALL + 'Money laundering has been detected '+ '$' + str(incomeOutput) + ' were omitted from the financial statements.') # Prints an alert with the amount of money laundered. 
  
  elif reportedNetIncome == netIncomeConfirm: # If the reported net income equals what should've been the net income the following code is executed.
    print() # Prints a blank space.
    print(Style.BRIGHT + Fore.GREEN + 'Notification: '+ Style.RESET_ALL + 'No money laundering detected') # Prints a notification message.
    
  else: # If the reportedNetIncome is less than what the actual net income should be the following code is executed. 
    print() # Prints a blank space.
    print(Style.BRIGHT + Fore.GREEN + 'Notification: '+ Style.RESET_ALL + 'No money laundering, $' + str(incomeErrorOutput) + 'has been omitted from the financial statements. ') # Prints a notification message with the amount 

#--- Detect financial fraud menu.
logging.debug('Start of function taxLaunder')
def taxLaunder(): # Defines the function taxLaunder
  '''
  Displays a list of options. 
  
  This function will display a list of sub-menu options and will
  call a function based upon the sub-menu option the user selected.

  Parameters
  ----------
  none
  
  Returns
  -------
  taxLaunderMenu
    The input of taxLaunderMenu
  '''
  
  logging.debug('Outputting financial fraud menu.')
  print(Style.BRIGHT + Fore.BLUE + '1. ' + Style.RESET_ALL + 'Detect tax evasion. ' ) # Prints menu option #1, makes the number blue.
  print(Style.BRIGHT + Fore.BLUE + '2. ' + Style.RESET_ALL + 'Detect money laundering. ' ) # Prints menu option #2, makes the number blue.
  
  print() # Prints a blank space.
  taxLaunderAsk = input('What option would you like to select?:') # Prompts the user to select an option.
  #assert isinstance(taxLaunderAsk, str), 'Expecting string!'
  
  if taxLaunderAsk.lower() in acceptableMenu: # If the user enters "Menu" or "menu" the following code is executed.
    print() # Prints a blank space.
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to main menu, standby.') # Prints a notification message.
    time.sleep(3) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    print() # Prints a blank message.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function. 
              
  logging.debug('Determining menu option selected.')
  if taxLaunderAsk == str('1'): # If the user selects option #1, the following code is executed.
    print() # Prints a blank space. 
    
    try: # The program will attempt to run the following code, if there is an error the code under "except:" will be executed.
     taxEvade(float(input('What was the total reported net income for the fiscal period?:')), float(input('What was the reported amount of taxes paid for the fiscal period?:')), float(input('What is the tax rate of the area the suspect resides in?:'))) # Calls the function taxEvade with the parameters as inputs. 
    
    except ValueError: # If there is an error when the code under "try:" is ran the following code will be executed.
      print() # Prints a blank message.
      print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, restarting function.') # Prints error message. 
      time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
      print() # Prints a blank message.
      os.system('cls') # Clears the console.
      print() # Prints a blank message.
      print(launchScreen) # Prints the launchScreen
      taxLaunder() # Calls the taxLaunder function. 
      
  elif taxLaunderAsk == str('2'): # If the user selects option #2, the following code is executed. 
    try: # The program will attempt to run the following code, if an error is given the code under "except:" will be ran.
      print() # Prints a blank space.
      moneyLaunder(int(input('What was the total reported net income for the fiscal period?:')), input('What was the total reported revenue for the fiscal period?'), input('What was the total reported expenses for the fiscal period?')) # Calls the function moneyLaunder with parameters as inputs
    
    except ValueError: # If the code under "try:" is executed and a ValueError is given the following code will be executed.
      print() # Prints a blank space. 
      print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, restarting function.') # Prints an error message. 
      time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
      print() # Prints a blank space.
      os.system('cls') # Clears the console.
      print() # Prints a blank space.
      print(launchScreen) # Prints the launchScreen
      taxLaunder() # Calls the taxLaunder function. 
      
  else: # If the user input is other than "1, 2, Menu or menu" the following code is executed.
   print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, restarting function.') # Prints an error message. 
   time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
   print() # Prints a blank message.
   os.system('cls') # Clears the console.
   print() # Prints a blank message.
   print(launchScreen) # Prints the launchScreen
   taxLaunder() # Calls the taxLaunder function. 
  
  print()# Prints a blank message. 
  taxLaunderMenu = input('Would you like to go back to the main menu?: ') # Asks if the user would like to go back to the main menu. 
  #assert isinstance(taxLaunderMenu, str), 'Expecting string!'
  
  if taxLaunderMenu.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
    os.system('cls') # Clears the terminal/console.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.
    
  elif taxLaunderMenu.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message. 
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    taxLaunder() # Calls the function taxLaunder
    
  else: # If the user's input isn't in acceptableReturnMenu or remain the following code is executed.
    print() # Prints a blank space. 
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, returning to menu.') # Prints an error message.
    print() # Prints a blank message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the terminal/console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the function menu.
  return taxLaunderMenu # Returns taxLaunderMenu (Exits the function)

#--- Create/Find Hidden Messages Menu
def hiddenMessages():
  print(Style.BRIGHT + Fore.BLUE + "1. " + Style.RESET_ALL + "Create a hidden message.") # Prints menu option #1, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "2. "+ Style.RESET_ALL + "Find a hidden message.") # Prints menu option #3, makes the option number blue.
  hiddenAsk = input('\nWhat option would you like to select?: ')
  
  if hiddenAsk in acceptableMenu:
    print(Fore.GREEN + 'Notification: ' + Style.RESET_ALL +'Returning to menu, standby.')
    time.sleep(2)
    os.system('cls')
  
  elif hiddenAsk == str('1'):
    os.system('cls')
    print(launchScreen)
    createMessage()
  
  elif hiddenAsk == str('2'):
    os.system('cls')
    print(launchScreen)
    findMessages()
  
  else:
    print(Fore.RED + 'Error: ' + Style.RESET_ALL + 'Unacceptable input, returning to menu.')
    
#--- Create hidden messages.  
def createMessage():
  #--- Rewrites original Romeo and Juliet to storyEdit, clears hiddenOutput. 
  with open('storyMaster.txt', 'r') as storyMaster:
    storyMasterContents = storyMaster.readlines()
    storyMaster.close()
    
  rewrite = ''
  for data in storyMasterContents:
    rewrite += data
  
  with open('story.txt', 'w') as storyEdit: # Rewrites storyMaster in storyEdit
    storyEdit.write(rewrite)
    storyEdit.close()
  
  with open('hiddenOutput.txt', 'w') as hiddenOutput: # clears story Output
    hiddenOutput.write('')
    hiddenOutput.close()

  
  #---
  
  hiddenAsk = input('What message would you like to hide?: ')
  randomNum = random.randint(1, len(storyMasterContents))
  
  with open('story.txt', 'a') as storyAppend: # Appends hidden message to story
    storyAppend.write('\n' + hiddenAsk.capitalize() + '. \n')
    storyAppend.close()
    
  storyRead = open('story.txt', 'r')
  storyReadContents = storyRead.readlines()

  lastLine = len(storyReadContents) - 1

  storyReadContents[lastLine], storyReadContents[randomNum] = storyReadContents[randomNum], storyReadContents[lastLine]

# copies story.txt and pastes in hiddenOutput
  new = ''
  for lines in storyReadContents:
    new += lines

  with open('hiddenOutput.txt', 'w') as hiddenOutput:
    hiddenOutput.write(new)
    os.fsync(hiddenOutput)
    hiddenOutput.close()
  
  
  print(Style.BRIGHT + Fore.GREEN + 'Success: ' + Style.RESET_ALL + 'Your message has been hidden in the contents of the file "hiddenOutput.txt"')
  
  createMessageAsk = input('\nWould you like to go back to the main menu?:')
  if createMessageAsk.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
    os.system('cls') # Clears the terminal/console.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.
    
  elif createMessageAsk.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message. 
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    hiddenMessages() # Calls the function taxLaunder
    
  else: # If the user's input isn't in acceptableReturnMenu or remain the following code is executed.
    print() # Prints a blank space. 
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, returning to menu.') # Prints an error message.
    print() # Prints a blank message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the terminal/console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the function menu.
  return createMessageAsk # Returns createMessageAsk (Exits the function)
  
#--- Find hidden messages.
def findMessages():
  print('''To find the hidden message, copy and paste the text into the file "hiddenOutput.txt".''')
  hiddenAsk = input('\n' + Fore.GREEN + 'Confirm: ' + Style.RESET_ALL + '''Press enter once you have pasted to the file:''')

  if hiddenAsk == str(''):
    with open('storyMaster.txt', 'r') as storyMaster:
      with open('hiddenMessageInput.txt', 'r') as hiddenInput:
        storyMasterContents = storyMaster.readlines()
        hiddenInputContents = hiddenInput.readlines()

    for i in range(0, len(storyMasterContents) - 1, 1):
      if storyMasterContents[i] != hiddenInputContents[i]:
        print('Hidden Message: ' + hiddenInputContents[i])
  
  findMessageAsk = input('\nWould you like to go back to the main menu?:')
  if findMessageAsk.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
    os.system('cls') # Clears the terminal/console.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.
    
  elif findMessageAsk.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
    print() # Prints a blank space. 
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message. 
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    hiddenMessages() # Calls the function taxLaunder
    
  else: # If the user's input isn't in acceptableReturnMenu or remain the following code is executed.
    print() # Prints a blank space. 
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, returning to menu.') # Prints an error message.
    print() # Prints a blank message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the terminal/console.
    print() # Prints a blank space.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the function menu.
  return findMessageAsk # Returns findMessageAsk (Exits the function)

  
  
  
  
#--- Login Validator
logging.debug('Start of function login.')
def login():  # Defines the function login.
  '''
  Prompts the user to login. 
  
  This function will prompt the user to login via their
  agent number/password. Ther function will then check if the
  login information is correct and act accordingly based upon if
  it is or not. . 

  Parameters
  ----------
  none
  
  Returns
  -------
  none
  '''
  print(launchScreen) # Prints the launchscreen. 
#--- Agent Login 
  agentNum = input('Agent Number:') # Prompts user to input their agent number.
  #assert isinstance(agentNum, str), 'Expecting string!'
  deptPass = input('Dept. Password:') # Prompts user to input their department password. 
  deptPassUTF = deptPass.encode('utf-8') 
  deptPassHex = binascii.hexlify(deptPassUTF).decode('utf-8')
  

  loginInfo = agentNum + ':' + deptPassHex
  userData = open('userdata.txt', 'r')
  userDataContent = userData.read()
  

  if loginInfo in userDataContent:
    print() # Prints blank space.
    print(Style.BRIGHT + Fore.GREEN + 'Access granted.' + Style.RESET_ALL) # Prints access granted message in bright green.
    print() # Prints blank space.
    print('Welcome back agent ' + str(agentNum) +'!') # Prints welcome message based upon the inputted agent number.
    menu() # Calls the menu function.
  
  else: 
    failedAttempts['failed'] += 1
    attemptsRemaining = 3 - failedAttempts['failed']
    print() # Prints blank space.
    
    if failedAttempts['failed'] == 3:
      print(Fore.RED + 'Denied: ' + Style.RESET_ALL + 'Maximum failed attempts reached, you have been locked out of the terminal.')
      time.sleep(2)
      sys.exit()
    
    print() # Prints a blank space. 
    print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Incorrect agent number/password entered, try again. You have ' + str(attemptsRemaining) + ' attempts remaining.') # Prints an error message.
    time.sleep(3) # Adds a 3 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    login() # Calls the login function

    
login() # Calls the login function
   
#--- End of code. 

  

