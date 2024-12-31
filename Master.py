from Main import *
import time
import pandas as pd


while True:
    print("----------------------------------------------------------------------------------------------------")
    print("Benvenuto nel generatore di password sicuro:\n")
    try:
        sc  = int(input("Scegli una voce da menù:\n1)Crea Password\n2)Leggi Password\n3)Chiudi\n"))
    except ValueError:
        print("Deve essere un NUMERO!!!")

    if sc == 1:      
        try:
            dom = int(input('Quante password vuoi creare?\n'))
        except ValueError:
            print('Deve essere un NUMERO!!!')
            time.sleep(2)
            break
        
        for x in range(dom):
            print(crea_psw())

    if sc == 2:
        print("Ecco le password salvate sul file presente nella directory:\n")
        print(read_psw())

    if sc == 3:
        print("Grazie per aver utilizzato il generatore!")
        time.sleep(3)
        break
