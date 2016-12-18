from core import colors

def printerror(message):
    if "\n" in message[0:1]:
            message = message.replace(message[0:1], "")
            print(colors.red+'\nerror:',message+colors.end)
    else:
        print(colors.red+'error:',message+colors.end)

def printsuccess(message):
    if "\n" in message[0:1]:
        message = message.replace(message[0:1], "")
        print(colors.green+'\n'+message+colors.end)
    else:
         print(colors.green+message+colors.end)