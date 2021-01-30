#!/usr/bin/env python3
# Pyinstaller Customizer Tool as described in Pythons and Dragons Paper
import argparse
import psutil
import os
import string
import random
import logging
import requests
import tempfile
import zipfile
import sys
import glob 

from logger import TerminalColors,LoggingFormater

class ReplaceStrings:
    def __init__(self,user_string):
        self.pyi_string = user_string
        self.pyinstaller_string = user_string

        if user_string == None:
            self.pyi_string = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(8,12)))
            self.pyinstaller_string = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(12,15)))


def banner():

    print(TerminalColors.CYAN+"  _____       _   _                            _____                                  "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" |  __ \     | | | |                   ___    |  __ \                                 "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" | |__) |   _| |_| |__   ___  _ __    ( _ )   | |  | |_ __ __ _  __ _  ___  _ __  ___ "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" |  ___/ | | | __| '_ \ / _ \| '_ \   / _ \/\ | |  | | '__/ _` |/ _` |/ _ \| '_ \/ __|"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" | |   | |_| | |_| | | | (_) | | | | | (_>  < | |__| | | | (_| | (_| | (_) | | | \__ \\"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" |_|    \__, |\__|_| |_|\___/|_| |_|  \___/\/ |_____/|_|  \__,_|\__, |\___/|_| |_|___/"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+"         __/ |                                                   __/ |                "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+"        |___/                                                   |___/                 "+TerminalColors.ENDC)

   
def arg_parser():

    banner()

    usage_text = '''usage:

    python3 PnD.py C:/path/to/Pyinstaller/Directory # full path
    ./PnD.py ../path/to/Pyinstaller/ # relative ppath
    '''

    parser = argparse.ArgumentParser(description="Pythons and Dragons Pyinstaller static analysis evasion tool ",epilog=usage_text,formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-d','--download',action='store_true',help='Version of Pyinstaller that you want to make stealth (Default and RECOMMENDED :4.0)') # TODO
    parser.add_argument('-s','--string', type=str, help='String to replace detectable strings (eg. pyi pyinstaller etc.) (Default: Random)',) # TODO
    parser.add_argument('path', help='Path to Pyinstaller that you want to make stealth')

    args = parser.parse_args()

    return args


def init_logging():

    logger = logging.getLogger("PnD")
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(LoggingFormater())
    logger.addHandler(ch)
    
    return logger


def is_running_in_powershell():

    parent_pid = os.getppid()
    process = psutil.Process(parent_pid)
    if "powershell" in process.name().lower():
        return True
    return False


def download_pyi():

    url = "https://github.com/pyinstaller/pyinstaller/archive/v4.0.zip"
    pyi = os.path.join(tempfile.gettempdir(), "pyi.zip")

    # r = requests.get(url,stream=True)
    # logger.info("Downloading pyinstaller v4.0")    

    # with open(pyi, 'wb') as fd:
    #     for chunk in r.iter_content(chunk_size=128):
    #         fd.write(chunk)
    
    logger.info("Unzipping pyinstaller")    

    # try:
    #     with zipfile.ZipFile(pyi, 'r') as zip_ref:
    #         zip_ref.extractall(os.path.join(tempfile.gettempdir(), "pyinstaller"))
    # except Exception as e:
    #     logger.error("Unzipping pyinstaller failed")    
    #     return 1

def rename_pyi():

    logger.info("Renaming Pyinstaller AV detectable strings")
    
    folder = os.path.join(tempfile.gettempdir(), "pyinstaller")
    pyi_folder = os.listdir(folder)[0]
    folder = os.path.join(folder,pyi_folder)

    if "pyinstaller-" not in folder:
        logger.error("Pyinstaller folder not found")
        return 1

    # get all files in pyinstaller directory
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(folder) for f in filenames ]
    print(len(files))
    counter = 0
    for file in files:
        try:
            if os.path.splitext(files) not in ["py","c"] :
                print( os.path.splitext(files))
                with open(file,'r') as f:
                    if 'pyi_' in f.read():
                        counter = counter + 1
                        print(counter)
        except Exception as e:
            logger.error(e)
            print(file)
            


if __name__ == '__main__':
    
    logger = init_logging()

    args = arg_parser()

    path = args.path
    download = args.download  
    user_string = args.string

    if not user_string:
        logger.info("Generating random strings")
    replace_strings = ReplaceStrings(user_string)

    err = download_pyi()

    if err:
        logger.critical("Unzip failed can't continue ")
        sys.exit()    

    err = rename_pyi()
    if err:
        logger.critical("Renaming failed can't continue ")
        sys.exit()  