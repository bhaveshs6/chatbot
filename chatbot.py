# Imporing os, subprocess, shutil and pyjokes (installing if not present)
# modules and taking input inside while loop
import os
import subprocess as sp
import shutil
os.system("echo Getting to you in 3.. 2.. 1..")
sp.getstatusoutput("pip install pyjokes")
os.system("cls")
import pyjokes
while True:
    x=input("Hey what do you want me to do? ")
# What are the programs that you support?
    if "what" in x or "?" in x:
        print("You can ask me to open chrome, notepad, vlc, calculator, show disk usage and crack a joke! You can use your own command by typing the word command.")
# Running programs
    elif "run" in x or "launch" in x or "execute" in x or "open" in x:
        if "browser" in x or "chrome" in x:
            os.system(r'"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
        elif "media" in x or "player" in x or "vlc" in x:
            os.system(r'"C:\Program Files\VideoLAN\VLC\vlc.exe"')
        elif "editor" in x or "notepad" in x:
            os.system("notepad")
        elif "calculator" in x or "calc" in x:
            os.system("calc")
        else:
            print("I don't support that!")
    elif x == "command":
        os.system(input("Enter your own command: "))
# Exiting the loop
    elif "exit" in x or "bye" in x or "close" in x:
        break
# Disk usage and random joke
    elif "disk" in x or "space" in x:
        print("Amount of disk used: ", shutil.disk_usage("/").used * 100/ shutil.disk_usage("/").total, "%", sep="")
    elif "joke" in x:
        print(pyjokes.get_joke())
# Prompt to ask me what I do
    else:
        print("Ask me what can I do.")
# Exiting statement
print("Next time!")
