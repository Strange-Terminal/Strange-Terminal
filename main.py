import os,platform
print("Hello in Strange Terminal")
commands=["CW","CWV"]
while True:
    command=input(str(os.path.abspath(os.getcwd()))+">>")
    if "CW" in command:
            print(command[command.find('"')+1:-1])  
    elif "CWV" in command :
        print(globals()[str(command[3:]).replace(" ","")])   
    if "cw" in command:
            print(command[command.find('"')+1:-1])  
    elif "cwv" in command :
        print(globals()[str(command[3:]).replace(" ","")])  
    elif "=" in command :
       globals()[str(command[0])] = command[2:]
    elif "clear" in command:
        if platform.system() ==  "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
