import os
import subprocess as sp

paths = {
    'vscode': "C:\\Users\\mihai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'skype': "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_vscode():
    os.startfile(paths['vscode'])

def open_skype():
    os.startfile(paths['skype'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])