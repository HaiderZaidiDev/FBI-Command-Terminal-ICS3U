from tkinter import *

gui = Tk()
gui.title('FBI: Command Terminal')

agentNumEntry = StringVar()
Label(gui, text = "Agent Number:").grid(row = 0)
Entry(gui, textvariable = agentNumEntry).grid(row = 0, column = 1)


deptPassEntry = StringVar()
Label(gui, text = "Dept. Password:").grid(row = 1)
deptPassAsk = Entry(gui, textvariable = deptPassEntry).grid(row = 1, column = 1)


def prints():
    agentNum = agentNumEntry.get()
    deptPass = deptPassEntry.get()
    loginInfo = agentNum + ':' + deptPass
    print(loginInfo)
Button(gui, text="Login", command = prints).grid(row = 2)




gui.mainloop()
