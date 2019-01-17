import random
from colorama import Fore, Style

def createMessage():
  #--- Rewrites original Romeo and Juliet to storyEdit, clears storyOutput. 
  with open('storyMaster.txt', 'r') as storyMaster:
    storyMasterContents = storyMaster.readlines()
    storyMaster.close()
    
  rewrite = ''
  for data in storyMasterContents:
    rewrite += data
  
  with open('story.txt', 'w') as storyEdit: # Rewrites storyMaster in storyEdit
    storyEdit.write(rewrite)
    storyEdit.close()
  
  with open('storyOutput.txt', 'w') as storyOutput: # clears story Output
    storyOutput.write('')
    storyOutput.close()
  
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

# copies story.txt and pastes in storyOutput
  new = ''
  for lines in storyReadContents:
    new += lines

  with open('storyOutput.txt', 'w') as storyOutput:
    storyOutput.write(new)
    storyOutput.close()


def findMessages():
  print('''To find the hidden message, copy and paste the text into the file "storyOutput.txt".''')
  hiddenAsk = input('\n' + Fore.GREEN + 'Confirm: ' + Style.RESET_ALL + '''Press enter once you have pasted to the file:''')

  if hiddenAsk == str(''):
    with open('storyMaster.txt', 'r') as storyMaster:
      with open('hiddenMessageInput.txt', 'r') as hiddenInput:
        storyMasterContents = storyMaster.readlines()
        hiddenInputContents = hiddenInput.readlines()

    for i in range(0, len(storyMasterContents) - 1, 1):
      if storyMasterContents[i] != hiddenInputContents[i]:
        print('Hidden Message: ' + hiddenInputContents[i])



