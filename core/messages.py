from core import bcolors

def printerror(message):
    print(bcolors.WARNING+'error:',message+bcolors.END)

def printsuccess(message):
    print(bcolors.OKGREEN+'[*]', message+bcolors.END)