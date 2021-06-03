import os, time, random
from os import system
from random import randint
import sys

os.system('clear')

from pydub import AudioSegment
from pydub.playback import play



from colorama import init
init(strip=not sys.stdout.isatty()) 
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Pydos ALPHA 2', font='isometric1'),
       'green', attrs=['bold'])

from colorama import init
init(strip=not sys.stdout.isatty()) 
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('by Lissard Technologies', font='standard'),
       'blue', attrs=['bold'])

sound = AudioSegment.from_wav('pds.wav')
play(sound)
##Notes 'n' stuff###

## Scripts borrowed from my recent pydos alpha. I was too lazy to write new scripts :p ##


def clear():
    return os.system('clear')

def dir():
    return os.system('ls')


print("welcome to Pydos alpha 2! type 'help' for a list of current commands...")
while True:
    ans = input(os.getcwd() + ": " )

    if ans == "dir":
        dir()

    if ans == "cd":
        os.system('ls')
        cd_a = input("to directory: ")

        if os.path.exists(cd_a):
            os.chdir(cd_a)
        else:
            print("invalid directory!")

    if ans == "bash":
        soundshd = AudioSegment.from_wav('pdss.wav')
        play(soundshd)
        exit("returning to bash...")
    if ans == "exit":
        soundshd = AudioSegment.from_wav('pdss.wav')
        play(soundshd)
        exit("returning to bash...")

    if ans == "help":

        print("help: this command\nInfo: info about software version and pc/laptop specs\nbash/exit: exit pydos and return to the bash shell\ncd: change directory\ndir: display directory\nnano: enter a gnu nano session (new buffer)\nmatrix: activate the cmatrix command\nNote that all commands must be lowercase. I'm gonna fix this during the summer break.\nalso, there are secret commands! find them all ;)")

    if ans == "info":
        os.system('neofetch')
        print("pydos version -1.1")

    if ans == "nano":



        os.system('nano')

    if ans == "pymod":
        pymod_a = input("Warning! You are about to access Pydos code! Do you want to continue? y = yes n = no: ")
        if pymod_a == "y":
            pymod_b = input("are you sure? y = yes n = no: ")
            if pymod_b == "y":
                pymod_c = input("really REALLY? y = DO IT ALREADY n = no: ")
                if pymod_c == "y":
                    print("ok, boss")
                    time.sleep(3)
                    os.system('nano "pydosalpha2.py"')

    if ans == "clear":
        clear()

    if ans == "echo":
        echo_a = input("what to repeat?: ")
        print(echo_a)
        os.system('echo "successfully printed text"')

    if ans == "su":
        os.system('sudo su')

    if  ans == "rmdir":
        rmdir_a = input("file/directory to remove: ")
        if rmdir_a == "pydosalpha2.py":
            print("no, I'm not gonna delete myself!")
        if os.path.isfile(rmdir_a):
            os.remove(rmdir_a)
        else:
            if os.path.exists(rmdir_a):
                os.rmdir(rmdir_a)
            else:
                print("invalid directory/file!")


    if ans == "mdir":
        mdir_a = input("new folder name: ")
        if os.path.exists(mdir_a):
            print("that folder already exists!")
        else:
            os.mkdir(mdir_a)

    if ans == "open":
        opn_a = input("bash or other (b/o): ")
        if opn_a == "b":
            opn_b = input("file name: ")
            if os.path.isfile("opn_b"):
                os.system('./' + opn_b)
            else:
                print("invalid file! make sure that it is a bash file")
        if opn_a == "o":
            opn_c = input("file name: ")
            if os.path.isfile(opn_c):
                os.system('nano' + " " + opn_c)
            else:
                print("invalid file!")

    if  ans == "snano":
        print("you need a password to access this!")
        os.system('sudo nano')


    if ans == "thanx":
        print("special thanks to: ")
        time.sleep(2)
        print("my beta testers")
        time.sleep(2)
        input("Alexander bell")
        input("##PLACEHOLDER##")

        print("Ideas by: ")
        time.sleep(3)
        input("Oscar laura garcia")
        input("ben.")
        
        print("Startup and Shutdown sounds by:")
        time.sleep(3)
        input("IBM, and their 'better than windows' operating system, OS/2 WARP 3!")



        



    if ans == "matrix":
        os.system('cmatrix')



    if ans == "eye":
        print("<    ()     >")


    
