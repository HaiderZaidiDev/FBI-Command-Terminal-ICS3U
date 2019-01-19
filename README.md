# FBI-Command-Terminal
This is an "FBI-Command Terminal" made in Python. 

## Features
* A GUI (Graphical-User-Interface) based login system that requires credentials from the user in terms of the Agent Number and Department Password.  
  * The login system scans the file userdata.txt to determine if the credentials inputted by the user is valid. If the credentials are invalid, an error message is given. The user can make a maximum of 3 failed login attempts before their locked out of the terminal.

* Encode ASCII messages into Hexadecimal. 
* Decode Hexadecimal messages into ASCII. 
* Request backup/evacuation
  * The backup/evacuation function uses an API to determine the users IP Address. Then, using the IP Address and the previously mentioned API, the users geolocation and approximate cordinates (in terms of longitude and lattitude are determined). Following, the Haversine formula (a formula used to determine the distance between a pair of lattitude and longitude points) is used to determine the distance the Agent (user) is away from the FBI Head Quarters (Washington D.C) in killometers. This also provides an approximate time figure for when the backup and or evacuation team would arrive, by taking the distance figure and dividing it by 100, acting under the assumption that the backup/evacuation team is travelling at a speed of 100Km/h. 
  
* Locate an IP Address. 
  * Uses an API to determine the approximate geo location and cordinates of an IP address inputted by the user.  
* Detect financial fraud. 
  * Ability to detect tax evasion. Contrasts the tax rate inputted by the agent with the amount of taxes an entity has paid, determines if said entity paid the right amount of taxes based upon the tax rate inputted by the agent and if they did not pay the right amount, how much they were under/over. 
  * Ability to detect money laundering. Uses the basic account formula (Revenue - Expenses = Net Income), contrasts the net income figure and the difference from the formula to determine if they were any discrepencies, this may not always be accurate in terms of determining money laundering as a simple mistake could have been made in the accounting proccess. 
* Create/find hidden messages in a text.
  * Ability to hide a message, based upon the users input in a random line of Romeo and Juliet. 
  * Ability to find a hidden message in Romeo and Juliet based upon the users input (contrasts the users input to a file with a master copy of Romeo and Juliet and outputs the differences). 
