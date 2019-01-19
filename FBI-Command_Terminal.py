
### LOGIN INFO FOR TESTING PURPOSES:
# AGENT NUMBER: admin
# Dept. Password: adminpass

#--- Imports
from colorama import init, Fore, Style # Imports Fore and style from Colorama. Allows for colored text. (https://pypi.org/project/colorama/)
import binascii # Imports Binascii module. Allows for conversion between number systems and ASCII. (https://docs.python.org/3.1/library/binascii.html)
import sys # Imports sys module. ALlows for numerous system related features.
import os # Imports OS module. Allows for numerous operation system related features.
import random # Imports random, allows for random objects to be generated. (https://docs.python.org/3/library/random.html)
import urllib.request # Imports Urllib.request module, allows for opening urls, reading the page source from urls amongst many other things. (https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
from termcolor import cprint # Imports cprint from the termcolor module. Allows for bolded, underlined and blinking text. (https://pypi.org/project/termcolor/)
from math import radians, cos, sin, sqrt, atan2 # Imports radians, cos, sin, sqrt and atan2 from the math module (https://docs.python.org/3/library/math.html)
import time # Imports time module. Allows for the delayed printing of text. (https://docs.python.org/3/library/time.html)
from tkinter import * # Imports everything from the tkinter module; GUI Platform. (https://wiki.python.org/moin/TkInter)
from PIL import ImageTk, Image # Imports ImageTk & Image from Pillow. Used to display images in the gui with tkinter.

init(convert=True) # Allows colorama to overwrite Ansi color codes.
os.system('mode con: cols=150 lines=30') # Designates cmd-prompt size.



#--- Logging
import logging # Imports logging module.
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') # Designates logging file and format.

logging.debug('Resetting debug.txt file.')
#--- Debug Clearing
with open('debug.txt', 'w') as debugFile: # Opens file debug.txt with intent to write.
  debugFile.write('') # Clears all data in debug.txt
  debugFile.close() # Closes all operations on file debug.txt

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

logging.debug('Variable and list assignment.')
#--- Variable & List Assignment
acceptableAgentNum = ['5','6','7','admin'] # Acceptable inputs for an agent number.
acceptableDeptPass = ['9', '8','12','adminpass'] # Acceptable inputs for an department password.
acceptableReturnMenu = ['yes'] # Acceptable inputs when the user is asked if they want to return to the menu.
remain = ['no'] # Acceptable inputs that will restart the function when the user is asked if they want to return to the menu.
acceptableMenuOptions = ['1','2','3','4','5', '6', '7'] # Acceptable inputs for the menu options.
acceptableMenu = ['menu'] # Acceptable inputs, when any one of these are typed into a main input it will return the user back to the menu.
acceptableBackupMenu = ['1', '2'] # Acceptable inputs for sub-menus.
failedAttempts = {'failed': 0} # Dictionary to track number of failed login attempts.




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
  print(Style.BRIGHT + Fore.BLUE + "2. "+ Style.RESET_ALL + "Request backup/evacuation.") # Prints menu option #2, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "3. "+ Style.RESET_ALL + "Locate an IP Address.") # Prints menu option #3, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "4. "+ Style.RESET_ALL + "Detect financial fraud.") # Prints menu option #4, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "5. "+ Style.RESET_ALL + "Create/Find Hidden Messages.") # Prints menu option #5, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "6. "+ Style.RESET_ALL + "Logout.") # Prints menu option #6, makes the option number blue.
  print(Style.BRIGHT + Fore.GREEN + "Note: "+ Style.RESET_ALL + 'If you select the wrong option, type menu in an input to return to the main menu.') # Prints menu option #6, makes the option number blue.
  print() # Prints blank space.

  menuAsk = input("What option would you like to select?:").strip() # Asks the user what option they would like to select.
  print() # Prints blank space.

 #--- If Statements to call functions, part of menu().
  logging.debug('Determining menu option selected.')
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
    os.system('cls')
    print(launchScreen)
    encryptDecodeMenu() # Calls the function unhex (converts Hexadecimal to ASCII)

    #- Menu Option #2 (Encrypt messages.)
  elif menuAsk == str('2'): # If the input for menuAsk is 2, the following code is executed.
    os.system('cls')
    print(launchScreen)
    backupEvac() # Calls the function asciiHex.


    #- Menu Option #3 (Request backup/evacuation)
  elif menuAsk == str('3'): # If the input for menuAsk is 3, the following code is executed.
    os.system('cls')
    print(launchScreen)
    ipLocate()# Calls the function backupEvac.

    #- Menu Option #4 (Locate an IP Address.)
  elif menuAsk == str('4'): # If the input for menu ask is 4, the following code is executed.
    os.system('cls')
    print(launchScreen)
    taxLaunder() # Calls the function ipLocate.

    #- Menu Option #5 (Create/Find Hidden Mes)
  elif menuAsk == str('5'): # If the input for menu ask is 5, the following code is executed.
    os.system('cls')
    print(launchScreen)
    hiddenMessages() # Calls the function hiddenMessages()

  	#- Menu Option #6 (Loguout)
  elif menuAsk == str('6'):
    logoutConfirm = input(Fore.GREEN + 'Confirm -  ' + Style.RESET_ALL + 'Are you sure you want to logout? (Press enter, anything else will return to menu):').strip(' ') # Prompts user to confirm logout.
    if logoutConfirm == str(''): # If the user presses the enter key, the following code is executed.
      print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Logging out, standby.') # Prints notification message.
      time.sleep(2) # Delays execution of the next line of code by 2 seconds.
      os.system('cls') # Clears the terminal/console.
      print(launchScreen) # Prints launchScreen.
      sys.exit() # Exits the program.

    if logoutConfirm.lower() in acceptableReturnMenu:
      print(Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Logging out, standby.')
      time.sleep(2) #Delays execution of the next line of code by 2 seconds.
      sys.exit() # Exits the program.

    elif logoutConfirm.lower() in remain:
      print(Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to menu, standby.')
      time.sleep(2) #Delays execution of the next line of code by 2 seconds.
      os.system('cls') # Clears the terminal/console.
      print(launchScreen) # Prints launchScreen.
      menu() # Calls menu function.

    else:
      print(Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to menu, standby.')
      time.sleep(2) # Delays execution of the next line of code by 2 seconds.
      os.system('cls') # Clears the terminal/console.
      print(launchScreen) # Prints launchScreen.
      menu() # Exits the program.

  #assert isinstance(menuAsk, string), 'Expecting a string!'

  return menuAsk # Returns menuAsk (Causes function to exit).
  logging.debug('End of function menu.')


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

  logging.debug('Requesting meun return input.')
  unHexMenu = input('Would you like to go back to the main menu?: ').strip(' ') # Asks if the user would like to go back to the main menu.
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
  logging.debug('End of function unHex')

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
   logging.debug('Requesting input user would like encrypted.')
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
    logging.debug('Encoding user input.')
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
  asciiHexMenu = input('Would you like to go back to the main menu?: ').strip(' ') # Asks if the user would like to go back to the main menu.
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

  encryptDecodeAsk = input('What input would you like to select?:').strip(' ')

  if encryptDecodeAsk.lower() in acceptableMenu: # If the user types "Menu" or "menu" into asciiInput the following code will be executed.
     print() # Prints a blank space.
     print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to main menu, standby.') # Prints a notification message.
     time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
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
  logging.debug('End of function AsciiHex.')


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

# --- Submenu.
  logging.debug('Displaying menu options.')
  print(Style.BRIGHT + Fore.BLUE + '1. ' + Style.RESET_ALL + 'Request backup. ' ) # Prints menu option #1, makes the number blue.
  print(Style.BRIGHT + Fore.BLUE + '2. ' + Style.RESET_ALL + 'Request an evacuation. ' ) # Prints menu option #2, makes the number blue.
  print()

  backupAsk = input('What option would you like to select?: ').strip(' ') # Asks the user what option they would like to select
  #assert isinstance(backupAsk, str), 'Expecting string!'
  logging.debug('Determining menu option selected.')
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
    logging.debug('End of backup portion.')

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
  logging.debug('End of evacuation portion.')

  #--- MENU RETURN
  logging.debug('Requesting menu return input.')
  backupEvacMenu = input('Would you like to go back to the main menu?: ').strip(' ') # Asks if the user would like to go back to the main menu.
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
  logging.debug('End of function backupEvac.')


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

  Raises (this section is only applicable if your function raises an exception)
  ------
  TypeError
    If the users input is less than 7 characters, minimum number of charaters for a dns server (i.e 8.8.8.8)

  TypeError
    If the users input contains characters from the alphabet, presumably indiciating the users provided an IPV6 address.
  '''
  logging.debug('Requesting user for ip input.')
  ipLocateAsk = input("Please enter the IP Address you would like to locate: ").strip(' ') # Prompts the user to input an IP Address.
  #assert isinstance (ipLocateAsk, str), 'Expecting string!'

  if ipLocateAsk in acceptableMenu:
    print() # Prints blank message.
    os.system('cls') # Clears console.
    print(launchScreen) # Prints launchScreen.
    menu() # Calls menu function.

  elif ipLocateAsk.isspace() or ipLocateAsk == str(''):
    print(Style.BRIGHT + Fore.RED + 'Error: ' + Style.RESET_ALL + 'No IP Address entered, restarting function.')
    time.sleep(2) # Delays execution of next line of code by 2 seconds.
    os.system('cls') # Clears console.
    print(launchScreen) # Prints launchScreen.
    ipLocate() # Calls function ipLocate




  try: # The program will attempt to run the following code, if an error is given the code under "except:" will be executed.
   if len(ipLocateAsk) < 7: # If ipLocateAsk is less than 7 chars the following code is executed.
        raise TypeError('An invalid ip address was given.') # Raises TypeError.
   elif ipLocateAsk.isalpha(): # If ipLocateAsk contains chars from the alphabet, the following code is executed.
       raise TypeError("IPV6 Address' are not supported at this time.") # Raises TypeError

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
    print(Style.BRIGHT + Fore.RED + 'Error: ' + Style.RESET_ALL + 'Oops! Looks like an invalid IP Address was given, please try again.') # Prints a error message.
    time.sleep(3) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    print(launchScreen) # Prints the launch screen.
    ipLocate() # Calls the function ipLocate

  except TypeError as errorMsg: # If an urllib error is given when the code under "try:" is attempted to be ran, the following code will be executed.
    print() # Prints a blank space.
    print(Style.BRIGHT + Fore.RED + 'Error: ' + Style.RESET_ALL + 'Oops! Something went wrong: {}'.format(errorMsg)) # Prints a error message.
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
  logging.debug('Requesting menu return input.')
  ipLocateMenu = input('Would you like to go back to the main menu?: ').strip(' ') # Asks if the user would like to go back to the main menu.
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
  logging.debug('End of function ip location.')


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
  logging.debug('End of function taxEvade.')

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
  logging.debug('End of function moneyLaunder')

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
  taxLaunderAsk = input('What option would you like to select?:').strip(' ') # Prompts the user to select an option.
  #assert isinstance(taxLaunderAsk, str), 'Expecting string!'

  logging.debug('Determining menu option selected.')
  if taxLaunderAsk.lower() in acceptableMenu: # If the user enters "Menu" or "menu" the following code is executed.
    print() # Prints a blank space.
    print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to main menu, standby.') # Prints a notification message.
    time.sleep(3) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears the console.
    print() # Prints a blank message.
    print(launchScreen) # Prints the launch screen.
    menu() # Calls the menu function.


  if taxLaunderAsk == str('1'):
      try:
          taxEvade(float(input('What was the total reported net income for the fiscal period?:').strip(' ')), float(input('What was the reported amount of taxes paid for the fiscal period?:').strip(' ')), float(input('What is the tax rate of the area the suspect resides in?:').strip(' '))) # Calls the function taxEvade with the parameters as inputs.
      except:
          print() # Prints a blank space.
          print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Unacceptable input, restarting function.') # Prints an error message.
          time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
          print() # Prints a blank space.
          os.system('cls') # Clears the console.
          print() # Prints a blank space.
          print(launchScreen) # Prints the launchScreen
          taxLaunder() # Calls the taxLaunder function.



  elif taxLaunderAsk == str('2'): # If the user selects option #2, the following code is executed.
    try: # The program will attempt to run the following code, if an error is given the code under "except:" will be ran.
      print() # Prints a blank space.
      moneyLaunder(int(input('What was the total reported net income for the fiscal period?:').strip(' ')), input('What was the total reported revenue for the fiscal period?:').strip(' '), input('What was the total reported expenses for the fiscal period?:').strip(' ')) # Calls the function moneyLaunder with parameters as inputs

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
  taxLaunderMenu = input('Would you like to go back to the main menu?: ').strip(' ') # Asks if the user would like to go back to the main menu.
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
  logging.debug('End of function taxEvade.')

#--- Create/Find Hidden Messages Menu
logging.debug('Start of function hiddenMessages.')
def hiddenMessages():
  '''
  Sub-menu for creating/finding a hidden message.

  This function provides displays a sub-menu of options related to creating and or finding a hidden message in a piece of text,
  specifically in Romeo and Juluet

  Parameters
  ----------
  none

  Returns
  -------
  string
    The input of hiddenMenuAsk.

  Raises (this section is only applicable if your function raises an exception)
  ------
  none
  '''
  logging.debug('Displaying menu options.')
  print(Style.BRIGHT + Fore.BLUE + "1. " + Style.RESET_ALL + "Create a hidden message.") # Prints menu option #1, makes the option number blue.
  print(Style.BRIGHT + Fore.BLUE + "2. "+ Style.RESET_ALL + "Find a hidden message.") # Prints menu option #2, makes the option number blue.
  hiddenMenuAsk = input('\nWhat option would you like to select?: ').strip(' ') # Prompts the user to select a menu item.

  logging.debug('Determining menu option selected.')
  if hiddenMenuAsk in acceptableMenu: # If the user inputs 'menu', the following code is executed.
    print(Fore.GREEN + 'Notification: ' + Style.RESET_ALL +'Returning to menu, standby.') # Prints notification message
    time.sleep(2) # Adds a 2 second delay to the execution of the next line of code.
    os.system('cls') # Clears terminal/console.
    print(launchScreen) # Prints launchScreen.
    menu() # Calls menu function.

  elif hiddenMenuAsk == str('1'): # If the user inputs '1', the following code is executed.
    os.system('cls') # Clears terminal/console.
    print(launchScreen) # Prints launchScreen.
    createMessage() # Calls function createMessage

  elif hiddenMenuAsk == str('2'):
    os.system('cls') # Clears terminal/console.
    print(launchScreen) # Prints launchScreen.
    findMessages() # Calls function findMessages


  else:
    print(Fore.RED + 'Error: ' + Style.RESET_ALL + 'Unacceptable input, returning to menu.') # Prints error message
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    os.system('cls') # Clears terminal/console.
    menu() # Calls menu function/
  return hiddenMenuAsk # Returns hiddenMenuAsk (exits the function)
  logging.debug('End of function hiddenMessages.')


#--- Create hidden messages.
logging.debug('Start of function createMessage.')
def createMessage():
      '''
      Create hidden messages in Romeo and Juliet.

      This function can create hidden messages inside Shakespeare's Romeo and Juliet. It takes an input from the user, appends
      the input to the text, replaced the appended line with a random line in the story and the outputs it to a file; hiddenOutput.txt. All files
      except for storyMaster.txt and userdata.txt are cleared when this function is ran.

      Parameters
      ----------
      none

      Returns
      -------
      string
        The input of createMessageAsk


      Raises (this section is only applicable if your function raises an exception)
      ------
      Exception
        Raised when the message the user would like to hide is, or less than 2 words.
        This is done because if the message contains 2 words or less, it would
        stand out when scrolling threw hiddenOutput.txt; defeating the purpose of hiding it.
      '''
      try:
        logging.debug('Rewriting content in story.txt and hiddenOutput.txt.')
        #-- Rewrites data in storyEdit & hiddenOutput to match storyMaster.
        with open('storyMaster.txt', 'r') as storyMaster: # Opens file storyMaster.txt with intent to read.
          storyMasterContents = storyMaster.readlines() # Reads all lines in storyMaster.txt
          storyMaster.close() # Closes all operations on storyMaster.txt

        rewrite = '' # Creates empty variable 'rewrite'
        for data in storyMasterContents: # For loop to access indexes (each line) of storyMaster.txt
          rewrite += data # Creates one large string of all the lines in storyMaster.txt

        with open('story.txt', 'w') as storyEdit: # Opens file story.txt with intent to write.
          storyEdit.write(rewrite) # Writes all contents from storyMaster.txt
          storyEdit.close() # Closes all operations on file story.txt

        with open('hiddenOutput.txt', 'w') as hiddenOutput: # clears story Output
          hiddenOutput.write('') # Writes all contents from storyMaster.txt
          hiddenOutput.close() # Closes all operations on file hiddenOutput.txt


        logging.debug('Requesting user input for hidden message.')
        hiddenAsk = input('What message would you like to hide?: ') # Prompts user for input
        hiddenAskWordCount = hiddenAsk.split() # Takes each word seperated by a space in hiddenAsk and places it into a list.
        if len(hiddenAskWordCount) <= 2: # If the number of indexes in hiddenAskWordCount is 2 or less, the following code is executed.
            raise Exception('Requested message to be hidden is too small') # Raises exception

        if hiddenAsk in acceptableMenu:
            print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to menu, standby.') # If the user inputs 'menu' in hiddenAsk the following code is executed.
            time.sleep(2) # Delays execution of the next line of code by 2 seconds.
            os.system('cls') # Clears the terminal/console.
            print(launchScreen) # Prints launch screen.
            menu() # Calls menu function.
        randomNum = random.randint(1, len(storyMasterContents)) # Generates a random integer within range of the number of lines in storyMaster.txt

        logging.debug('Creating hidden message.')
        with open('story.txt', 'a') as storyAppend: # Opens file story.txt with intent to append.
          storyAppend.write('\n' + hiddenAsk.capitalize() + '. \n') # Capitalizes the first letter in hiddenAsk and adds a period at the end - done so the hidden message blends into the text.
          storyAppend.close() # Closes all operations on file story.txt

        storyRead = open('story.txt', 'r') # Opens file story.txt with intent to read.
        storyReadContents = storyRead.readlines() # Reads all lines in story.txt

        lastLine = len(storyReadContents) - 1 # Subtrats one from the total number of lines in story.txt (the line which the appended message a.k.a the users input is currently on)

        storyReadContents[lastLine], storyReadContents[randomNum] = storyReadContents[randomNum], storyReadContents[lastLine] # Repalces the line which the users input is currently on (the second last one) with a random line in story.txt


        new = '' # Creates empty variable 'new'
        for lines in storyReadContents: # For loop to access indexes (each line) in story.txt
          new += lines # Creates one large string of all the lines in story.txt

        logging.debug('Outputting hidden message.')
        with open('hiddenOutput.txt', 'w') as hiddenOutput: # Opens file hiddenOutput.txt with intent to write.
          hiddenOutput.write(new) # Writes all contents from story.txt (the story with the hidden message inside) to file hiddenOutput.txt
          os.fsync(hiddenOutput) # Forces buffer to write to hiddenOutput
          hiddenOutput.close() # Closes all operations on file hiddenOutput.txt


        print(Style.BRIGHT + Fore.GREEN + 'Success: ' + Style.RESET_ALL + 'Your message has been hidden in the contents of the file "hiddenOutput.txt"') # Prints success message.

        logging.debug('Requesting input for menu return.')
        createMessageAsk = input('\nWould you like to go back to the main menu?:').strip(' ') # Asks the user if they would like to go back to the menu.
        if createMessageAsk.lower() in acceptableReturnMenu: # If the user enters "Yes" or "yes" (acceptableReturnMenu) the following code is executed.
          os.system('cls') # Clears the terminal/console.
          print(launchScreen) # Prints the launch screen.
          menu() # Calls the menu function

        elif createMessageAsk.lower() in remain: # If the user enters "No" or "no" (remain) the following code is executed.
          print() # Prints a blank space.
          print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Restarting function, standby.') # Prints a notification message.
          time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
          os.system('cls') # Clears the console.
          print(launchScreen) # Prints the launch screen.
          hiddenMessages() # Calls the function hiddenMessages.

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
      except Exception as lowCount:
        print() # Prints a blank space.
        print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Oops! Something went wrong: {} (It would be spotted easily).'.format(str(lowCount))) # Prints an error message.
        print() # Prints a blank message.
        time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
        os.system('cls') # Clears the terminal/console.
        print() # Prints a blank space.
        print(launchScreen) # Prints the launch screen.
        menu() # Calls the function menu.
        return createMessageAsk # Returns createMessageAsk (Exits the function)
        logging.debug('End of function createMessage')


#--- Find hidden messages.
logging.debug('Start of function findMessages.')
def findMessages(): # Defines function findMessages.
  '''
      Find hidden messages in Romeo and Juliet.

      This function takes an input from the user, from a file (hiddenMessageInput.txt) and compares the input to storyMaster.txt and
      outputs any differences between the two files, the purpose of this function is to find/locate a hidden message in the text from another agent.

      Parameters
      ----------
      none

      Returns
      -------
      string
        The input of findMessageAsk

      Raises (this section is only applicable if your function raises an exception)
      ------
      none
  '''
  with open('hiddenMessageInput.txt', 'w') as hiddenMessageInputOutput: # clears story Output
    hiddenMessageInputOutput.write('') # Writes all contents from hiddenMessageInputOutput.txt
    hiddenMessageInputOutput.close() # Closes all operations on file hiddenMessageInputOutput.txt

  logging.debug('Displaying confirmation screen.')
  print('''To find the hidden message, copy and paste the text into the file "hiddenMessageInput.txt".''') # Prompts user to paste message to file hiddenMessageInput.txt
  hiddenAsk = input('\n' + Fore.GREEN + 'Confirm - ' + Style.RESET_ALL + '''Press enter once you have pasted to the file:''') # Prompts user to confirm that they've pasted the message.

  if hiddenAsk == str(''): # If the user presses enter when prompted to confirm, the following code is executed.
    with open('storyMaster.txt', 'r') as storyMaster: # Opens storyMaster.txt with intent to read.
      with open('hiddenMessageInput.txt', 'r') as hiddenInput: # Opens hiddenMessageInput.txt with intent to read.
        storyMasterContents = storyMaster.readlines() # Reads all lines in storyMaster.txt, assigns to variable.
        hiddenInputContents = hiddenInput.readlines() # Reads all lines in hiddenInputContents.txt, assigns to variable.

    logging.debug('Contrasting hiddenMessageInput.txt with storyMaster.txt')
    try:
        for i in range(0, len(storyMasterContents) - 1, 1): # For loop, counts number of lines in storyMaster.txt
          if storyMasterContents[i] != hiddenInputContents[i]: # If a line in storyMaster has different text then hiddenMessageInput the following code is executed.
            print('Hidden Message: ' + hiddenInputContents[i]) # Prints different text (hidden message) from hiddenMessageInput
    except IndexError:
        print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'There was an error finding the hidden message, make sure you saved the file "hiddenMessageInput.txt"')
        time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
        os.system('cls') # Clears the terminal/console.
        print(launchScreen) # Prints the launch screen.
        findMessages() # Calls the function findMessages

  elif hiddenAsk in acceptableMenu: # If the user inputs 'menu', the following code is executed.
      print() # Prints blank space.
      print(Style.BRIGHT + Fore.GREEN + 'Notification: ' + Style.RESET_ALL + 'Returning to menu, standby.') # Prints notification message.
      time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
      os.system('cls') # Clears the terminal/console.
      print(launchScreen) # Prints the launch screen.
      menu() # Calls the menu function.

  logging.debug('Requesting menu return input.')
  findMessageAsk = input('\nWould you like to go back to the main menu?:').strip(' ') # Asks user if they'd like to go back to the menu.
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
  logging.debug('End of function findMessages.')





#--- Login GUI
logging.debug('Initalizing GUI.')
gui = Tk() # Assigns Tk() to variable gui.
gui.title('FBI: Command Terminal') # Sets title of gui.
gui.geometry('350x400') # Sets size of gui.

logoLoad = ImageTk.PhotoImage(Image.open("badge.png").resize((300,225))) # Loads FBI-Command-Terminal logo.
logo = Label(gui, image = logoLoad) # Displays FBI-Command-Terminal logo.
logo.place(x = 23, y = -25) # Alignment of logo in pixels.



agentNumEntry = StringVar() # Variable to get user input of agent number.
AgentNumText = Label(gui, text = "Agent Number") # Displays agent number label.
AgentNumText.place(x = 27, y = 155 ) # Aligns agent number label in pixels.

agentNumAsk = Entry(gui, textvariable = agentNumEntry, width = 47) # Creates input field for agent number.
agentNumAsk.place(x = 30, y = 175) # Aligns agent number input field in pixels


deptPassEntry = StringVar() # Variable to get user input of dept. passwords
deptPassText = Label(gui, text = "Dept. Password") # Displays dept. pass label.
deptPassText.place(x = 27, y = 210) # Aligns dept. pass label in pixels.

deptPassAsk = Entry(gui, textvariable = deptPassEntry, show='*', width = 47) # Creates input field for dept. pass, hides input with asteriks.
deptPassAsk.place(x = 30, y = 230) # Aligns dept. pass input field in pixels.

logging.debug('Start of function loginPage.')
def loginPage(): # Defines function loginPage()
    agentNum = agentNumEntry.get().lstrip(' ') # Gets agentNum from agentNumEntry.
    deptPass = deptPassEntry.get().lstrip(' ') # Gets deptPass from deptPassEntry.
    deptPassUTF = deptPass.encode('utf-8') # Encodes deptPass to utf-8 so it can be converted to a hexadecimal.
    deptPassHex = binascii.hexlify(deptPassUTF).decode('utf-8') # Converts deptPass to a hexadecimal, decodes to utf-8 (removes unwanted prefixes).
    loginInfo = agentNum + ':' + deptPassHex # Assigns varibale loginInfo with formatting of userdata.
    userData = open('userdata.txt', 'r') # Opens userdata.txt (location of usernames and passwords)
    userDataContent = userData.read() # Reads userdata.txt
    userData.close() # Closes all operations on userdata.txt


    if loginInfo in userDataContent: # If the user's login information is located in the userdata file, the following code is executed.
      gui.destroy() # Closes the gui.
      print(launchScreen) # Prints the launch screen.
      print() # Prints blank space.
      print(Style.BRIGHT + Fore.GREEN + 'Access granted.' + Style.RESET_ALL) # Prints access granted message in bright green.
      print() # Prints blank space.
      print('Welcome back agent ' + str(agentNum.strip(' ')) +'!') # Prints welcome message based upon the inputted agent number.
      menu() # Calls the menu function.


    else: # If the user's login information isn't located in the userdata file, the following code is executed.
      failedAttempts['failed'] += 1 # Adds 1 to the key value of dictionary failedAttempts (counts how many times the user inputted invalid credentials)
      attemptsRemaining = 3 - failedAttempts['failed'] # Variable for amount of attempts the user has left before their locked out the system.
      print() # Prints blank space.

      if failedAttempts['failed'] == 3: # If the user has entered invalid credentials 3 times, the following code is executed.
        print(Fore.RED + 'Denied: ' + Style.RESET_ALL + 'Maximum failed attempts reached, you have been locked out of the terminal.') # Notifies user that they've been locked out of the terminal.
        time.sleep(2) #  Adds a 2 second delay before the next line of code is executed.
        sys.exit() # Exits terminal.

      if agentNum.isupper() or deptPass.isupper(): # If the user's agent number or password is in all uppercase chars the following code is executed.
          print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Incorrect agent number/password entered, try again. You have ' + str(attemptsRemaining) + ' attempts remaining.' + Style.BRIGHT + Fore.GREEN + '\nNote: ' + Style.RESET_ALL + 'It appears that your capslock is on, if this is a mistake make sure to disable it!') # Notifies the user of remaining login attempts and that they may have capslock on.
          time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
          os.system('cls') # Clears the console.


      print() # Prints a blank space.
      print(Fore.RED + 'Error: ' + Style.RESET_ALL +  'Incorrect agent number/password entered, try again. You have ' + str(attemptsRemaining) + ' attempts remaining.') # Prints an error message and remaining login attempts.
      time.sleep(3) # Adds a 3 second delay before the next line of code is executed.
      os.system('cls') # Clears the console.
logging.debug('End of function loginPage')
loginButton = Button(gui, text="Login", command = loginPage, width = 40) # Login button for the gui, when clicked, the function loginPage is ran.
loginButton.place(x = 28, y = 270) # Alignment of loginButton in pixels.




gui.mainloop() # Runs gui.


logging.debug('End of program.')
#--- End of code.
