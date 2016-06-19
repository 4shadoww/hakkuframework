from core import bcolors

def printerror(message):
    if "\n" in message[0:1]:
            message = message.replace(message[0:1], "")
            print(bcolors.WARNING+'\nerror:',message+bcolors.END)
    else:
        print(bcolors.WARNING+'error:',message+bcolors.END)

def printsuccess(message):
    if "\n" in message[0:1]:
        message = message.replace(message[0:1], "")
        print(bcolors.OKGREEN+'\n[*]', message+bcolors.END)
    else:
         print(bcolors.OKGREEN+'[*]', message+bcolors.END)