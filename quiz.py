#variabili
error001 = "errore: 001 exp: errore nell'inserimento (ricomincerai)"

while True:
   #qua chiedo se vuole iniziare
    pronto = str(input("sei pronto?\nsi o no?\n"))
    
    #cascata di condizione per procedete nel quiz
    if pronto == "si" or pronto == "SI" or pronto == "Si" or pronto == "sI":
        risposta1 = str(input("jojo è un romanzo?\nsi o no?\n"))
        
        if risposta1 == "si" or risposta1 == "SI" or risposta1 == "Si" or risposta1 == "sI":
            print("hai perso, ricomincerai")
            continue

        elif risposta1 == "no" or risposta1 == "NO" or risposta1 == "No" or risposta1 == "nO":
            print("corretto, passiamo alla prossima domanda")
            risposta2 = str(input("la luna è un semi satellite?\nsi o no?\n"))
            
            if risposta2 == "si" or risposta2 == "SI" or risposta2 == "Si" or risposta2 == "sI":
                print("hai perso, ricomincerai")
                continue

            elif risposta2 == "no" or risposta2 == "NO" or risposta2 == "No" or risposta2 == "nO":
                print("hai vinto!!!")
                break

            else:
                print(error001)
                
        else:
            print(error001)

    elif pronto == "no" or pronto == "NO" or pronto == "No" or pronto == "nO":
        print("ok, uscirai dal programma")
        break

    else:
        print(error001)
        continue
