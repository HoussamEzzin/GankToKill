#os.system('cmd /k "Your Command Prompt Command"')
import os

def push_to_github():
    print("Adding to github ...")
    os.system('cmd /k "git add ."')
    os.system('cmd /k "git commit -m "update""')
    os.system('cmd /k "git push"')
    print("DONE")
    