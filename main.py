# Import
import os
import time
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
import subprocess
from os import system

cmd = 'WMIC PROCESS get Caption,Commandline,Processid'

root = tk.Tk()
root.withdraw()


# Colors
cyan = '\u001b[36m'
green = '\033[0;32m'
red = '\033[0;31m'
reset = '\033[0m'


# Def 
def cls():
    try:os.system('cls')
    except:os.system('clear')

def ascii():
    cls()
    print(f"{cyan}        d8b                                                                                                            ")
    print(f"{cyan}        ?88                                                                                                            ")
    print(f"{cyan}         88b                                                                                                           ")
    print(f"{cyan} d8888b  888888b   88bd88b d8888b   88bd8b,d88b  d8888b     .d888b, d8888b  88bd88b d888b8b  ?88,.d88b, d8888b  88bd88b")
    print(f"{cyan}d8P' `P  88P `?8b  88P'  `d8P' ?88  88P'`?8P'?8bd8b_,dP     ?8b,   d8P' `P  88P'  `d8P' ?88  `?88'  ?88d8b_,dP  88P'  `")
    print(f"{cyan}88b     d88   88P d88     88b  d88 d88  d88  88P88b           `?8b 88b     d88     88b  ,88b   88b  d8P88b     d88     ")
    print(f"{cyan}`?888P'd88'   88bd88'     `?8888P'd88' d88'  88b`?888P'    `?888P' `?888P'd88'     `?88P'`88b  888888P'`?888P'd88'     ")
    print(f"{cyan}                                                                                               88P'                    ")
    print(f"{cyan}                                                                                              d88                      ")
    print(f"{cyan}                                                                                              ?8P                      \n")

def printnb(nb, text):
    print(f'{reset}[{cyan}{nb}{reset}] {text}')

def getdirectory():
    try:return [True, os.path.expanduser( '~' )]
    except:return [False, None]

def printtf(statut, text):
    if not statut == None:
        if statut == True:print(f'{green}{text}')
        if statut == False:print(f'{red}{text}')

def yesorno(fichier, dossier):
    res=mb.askquestion("Fichier Existant", f"Le fichier '{fichier}' est existant dans le dossier '{dossier}' voulez vous l'écrasez ?")
    if res == 'yes' :return True
    else :return False
def importyesorno():
    res=mb.askquestion("Voulez vous importer", f"Voulez vous vraiment importer les configurations dans chrome ?")
    if res == 'yes' :return True
    else :return False
def chromeopen():
    res=mb.askquestion("Chrome est ouvert", f"Chrome est en cours d'éxécution, vous ne pouvez par importer si chrome est ouvert ! Voulez vous fermez Google Chrome ?")
    if res == 'yes' :return True
    else :return False

def existant(path):
    try:
        with open(path, 'r') as f:return True
    except:return False

                    
# Scraper
chromehistory = f"{getdirectory()[1]}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
chromefavicons = f"{getdirectory()[1]}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Favicons"
chromebookmarks = f"{getdirectory()[1]}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"
chromedefault = f"{getdirectory()[1]}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"


while True:
    try:
        ascii()
        printnb(0, 'Sortie')
        printnb(1, 'Import')
        printnb(2, 'Export')
        print()
        choice = int(input(f'{cyan}Veuillez entrer un chiffre associé au nom > {reset}'))

        # Exit
        if choice == 0:break 

        # Sortie
        if choice == 1:
            kill = None
            while True:
                try:
                    ascii()
                    printnb(0, 'Sortie')
                    printnb(1, 'Tout')
                    printnb(2, 'Import Raccourci')
                    printnb(3, 'Import Favoris')
                    print()

                    choice = int(input(f'{cyan}Veuillez entrer un chiffre associé au nom > {reset}'))

                    if choice == 0:break

                    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                    for line in proc.stdout:
                        if 'chrome.exe' in str(line):
                            statut = chromeopen()
                            if statut == True:
                                with open(os.devnull, 'w') as devnull:
                                    subprocess.call(['taskkill', '/IM', 'chrome.exe', '/F'], stdout=devnull, stderr=subprocess.STDOUT)
                                kill = True
                            elif statut == False:
                                kill = False
                            break

                    if kill == False:break

                    if choice == 1:
                        dossier = filedialog.askdirectory()
                        if dossier != "":
                            if importyesorno() == True:

                                # Favoris
                                try:
                                    print(f'{dossier}/Bookmarks')
                                    shutil.copy(f'{dossier}/Bookmarks', chromedefault)
                                    print(f'{green}la copie des Favoris "Bookmarks" vers Chrome a bien été effectué.')
                                except:None

                                # Raccourci
                                try:
                                    shutil.copy(f'{dossier}/Favicons', chromedefault)
                                    print(f'{green}la copie des icone "Favicons" vers Chrome a bien été effectué.')
                                except:None

                                try:
                                    shutil.copy(f'{dossier}/History', chromedefault)
                                    print(f'{green}la copie des raccourci "History" vers Chrome a bien été effectué.')
                                except:None
                                time.sleep(5)

                    
                    # Get Shortcut
                    if choice == 2:
                        dossier = filedialog.askdirectory()
                        if dossier != "":
                            if importyesorno() == True:
                                try:
                                    shutil.copy(f'{dossier}/Favicons', chromedefault)
                                    shutil.copy(f'{dossier}/History', chromedefault)
                                    print(f'{green}la copie des raccourci "History" vers Chrome a bien été effectué.')
                                    print(f'{green}la copie des icone "Favicons" vers Chrome a bien été effectué.')
                                except:None
                                time.sleep(5)
                    
                    # Get Favoris
                    if choice == 3:
                        dossier = filedialog.askdirectory()
                        if dossier != "":
                            if importyesorno() == True:
                                try:
                                    shutil.copy(f'{dossier}/Bookmarks', chromedefault)
                                    print(f'{green}la copie des Favoris "Bookmarks" vers Chrome a bien été effectué.')
                                except:None
                                time.sleep(5)

                except:None



        if choice == 2:
            while True:
                try:
                    ascii()
                    printnb(0, 'Sortie')
                    printnb(1, 'Tout')
                    printnb(2, 'Export Raccourci')
                    printnb(3, 'Export Favoris')
                    print()

                    choice = int(input(f'{cyan}Veuillez entrer un chiffre associé au nom > {reset}'))

                    if choice == 0:break

                    if choice == 1:
                        dossier = filedialog.askdirectory()
                        if dossier != "":
                        
                            # Favicons
                            try:
                                if existant(f'{dossier}/Favicons') == True:
                                    if yesorno('Favicons', dossier) == True:
                                        shutil.copy(chromefavicons, dossier)
                                        print(f'{green}la copie de {chromefavicons} vers {dossier} a bien été effectué.')
                                else:
                                        shutil.copy(chromefavicons, dossier)
                                        print(f'{green}la copie de {chromefavicons} vers {dossier} a bien été effectué.')
                            except:None

                            # History 
                            try:
                                if existant(f'{dossier}/History') == True:
                                    if yesorno('History', dossier) == True:
                                        shutil.copy(chromehistory, dossier)
                                        print(f'{green}la copie de {chromehistory} vers {dossier} a bien été effectué.')
                                else:
                                        shutil.copy(chromehistory, dossier)
                                        print(f'{green}la copie de {chromehistory} vers {dossier} a bien été effectué.')                         
                            except:None
                        
                            # Bookmarks
                            try:
                                if existant(f'{dossier}/Bookmarks') == True:
                                    if yesorno('Bookmarks', dossier) == True:
                                        shutil.copy(chromebookmarks, dossier)
                                        print(f'{green}la copie de {chromebookmarks} vers {dossier} a bien été effectué.')
                                else:
                                    shutil.copy(chromebookmarks, dossier)
                                    print(f'{green}la copie de {chromebookmarks} vers {dossier} a bien été effectué.')
                            except:None

                            time.sleep(3)

                        # Get Shortcut
                    if choice == 2:
                        dossier = filedialog.askdirectory()
                        if dossier != "":
                            try:
                                if existant(f'{dossier}/Favicons') == True:
                                    if yesorno('Favicons', dossier) == True:
                                        shutil.copy(chromefavicons, dossier)
                                else:shutil.copy(chromefavicons, dossier)
                            except:None

                            try:
                                if existant(f'{dossier}/History') == True:
                                    if yesorno('History', dossier) == True:                           
                                        shutil.copy(chromehistory, dossier)
                                else:shutil.copy(chromehistory, dossier)     
                            except:None
                    
                    # Get Favoris
                    if choice == 3:
                        dossier = filedialog.askdirectory()
                        if dossier != "":
                            try:
                                if existant(f'{dossier}/Bookmarks') == True:
                                    if yesorno('Bookmarks', dossier) == True:
                                        shutil.copy(chromebookmarks, dossier)
                                else:shutil.copy(chromebookmarks, dossier)
                            except:None
                except:None
    except:None


