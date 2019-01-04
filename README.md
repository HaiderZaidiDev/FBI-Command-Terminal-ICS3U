# FBI-Command-Terminal
This is an "FBI-Command Terminal" made in Python. This program was made as an assignment for a university preperation computer science course in high-school (ICS3U). 

This program has the following features: 
* Login system that requires an input for the agent number and password. Due to this being a preparation course, there was no use of databases so a list system was used to create the acceptable agent number and password, therefore, agent numbers and passwords can be mixed and matched. 

* Encode ASCII messages into Hexadecimal. 
* Decode Hexadecimal messages into ASCII. 
* Request backup/evacuation; This uses an API to determine the users IP address which then determines their geolocation and approximate longitude and lattiude cordinates, said cordinates are then used in the Haversine formula (a formula to calculate the distance between two cordinates) in partnership with the cordinates for the FBI headquarters to determine the approximate distance between the "agent" using the command terminal and the FBI Headquarters. In addition to determining the distance between the agent and the FBI headquarters, this program will also determine the time it would take to reach the agent, under the assumption that the backup and or evacuation team is travelling at 100Km/h. 
* Locate an IP Address. Works similar to the previous function, however, requires an input in the form of an IP Address from the agent. Using the previously mentioned API, information in regards to the approximate geo location of the IP Address is determined. 
* Detect financial fraud. 
  * Ability to detect tax evasion. Contrasts the tax rate inputted by the agent with the amount of taxes an entity has paid, determines if said entity paid the right amount of taxes based upon the tax rate inputted by the agent and if they did not pay the right amount, how much they were under/over. 
  * Ability to detect money laundering. Uses the basic account formula (Revenue - Expenses = Net Income), contrasts the net income figure and the difference from the formula to determine if they were any discrepencies, this may not always be accurate in terms of determining money laundering as a simple mistake could have been made in the accounting proccess. 
  
