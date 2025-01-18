import random
import bcrypt
import os
import pandas as pd

def crea_psw():
    name_s = input('Per quale sito tiserve:\n')
    
    letter_max = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    letter_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    
    prima = random.sample(letter_max,8)
    seconda = random.sample(letter_min,8)

    
    prima_psw = prima+seconda
    random.shuffle(prima_psw)
    psw_ok = "".join(prima_psw)

    
    hashed=bcrypt.hashpw(psw_ok.encode(),bcrypt.gensalt())
    hashed = str(hashed)

    hansw = input('Salvare le credenziali in un file? (S/N)\n').strip().upper()

    
    if hansw == "S":
        lista = os.listdir()

        if 'psw.csv' not in lista:
            with open('psw.csv','w') as file:
                file.write('nome_sito,password'+'\n')
                file.write(name_s)
                file.write(',')
                file.write(hashed)
        else:
            with open('psw.csv','a') as file:
                file.write('\n')
                file.write(name_s)
                file.write(',')
                file.write(hashed)

    elif hansw == "N":
        print(f"Ok non salvate!")
    else:
        print(f"Risposta errata!\n")

    print()

    return f"Password Hash: {hashed} per l'account di {name_s}"


def read_psw():
    df = pd.read_csv('psw.csv')
    df_ok = pd.DataFrame(df)
    return df_ok.to_string(index=False)
    

