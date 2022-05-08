#classi per ragruppare varie propieta per le pizze e bevande
class Prd:
    def __init__(self, nome, prezzo, vegana):
        
        self.nome = nome
        self.prezzo = prezzo
        self.vegana = vegana

p1 = Prd("Margherita", 4.50, "si")

p2 = Prd("Patapizza", 6.50, "si") 

p3 = Prd("Pistacchiosa", 7.00, "no")

p4 = Prd("Norma", 8.50, "si")

bevanda1 = Prd("Birra bionda (media)", 5.50, "no")
bevanda2 = Prd("Birra bionda (grande)", 7.00, "no")

bevanda3 = Prd("Birra rossa (media)", 5.50, "no")
bevanda4 = Prd("Birra rossa (grande)", 7.00, "no")

bevanda5 = Prd("Bottiglietta d'acqua 0,5 L (naturale)", 2.00, "si")
bevanda6 = Prd("Bottiglietta d'acqua 0,5 L (frizzante)", 2.50, "si")

#variabili
totale = 0

numeroP = 0

#qua metto una variabile per scrivere un certo messagio che ripeto sempre
inputerror001 = "errore: 0001 txt: hai sbagliato a digitare"

contatore = 0

#un ciclo while che simula un ciclo do (vedi sotto), racchiude tutto il programma
while True:
    try:
        utente = int(input("salve utente, specificare il propio ruolo.\n1- cliente\n2- ristoratore\n"))
        
    except:
        print(inputerror001)
        continue

    else:
        if utente == 1:
            print("\nil menù è il seguente:\n")
            #il commando altro e le pizze
            print("Altro:\n 0- vuoto\n \nPizze:\n", "1-", p1.nome, "vegana?:", p1.vegana, p1.prezzo, "euro\n", "2-", p2.nome, "vegana?:", p2.vegana, p2.prezzo, "euro\n", "3-", p3.nome, "vegana?:", p3.vegana, p3.prezzo, "euro\n", "4-", p4.nome, "vegana?:", p4.vegana, p4.prezzo, "euro\n")
            #le bevande
            print("Bevande:\n", "5-", bevanda1.nome, "vegana?", bevanda1.vegana, bevanda1.prezzo, "euro\n", "6-", bevanda2.nome, "vegana?", bevanda2.vegana, bevanda2.prezzo, "euro\n", "7-", bevanda3.nome, "vegana?", bevanda3.vegana, bevanda3.prezzo, "euro\n", "8-", bevanda4.nome, "vegana?", bevanda4.vegana, bevanda4.prezzo, "euro\n", "9-", bevanda5.nome, "vegana?", bevanda5.vegana, bevanda5.prezzo,"euro\n", "10-", bevanda6.nome, "vegana?", bevanda6.vegana, bevanda6.prezzo, "euro\n")

            #provo a vedere se funziona con il try ma se e minore di 0 la richiesta manda errore.(si potrebbero usare degl'if, elif ed else per fare le stesse mansioni in questo caso, ma ho deciso cosi perchè li volevo provare)
            try:
                numeroP = int(input("quante portate vuole ordinare?: "))

                if numeroP < 1:
                    raise exception

            #qua c'è il blocco per il caso in qui ci sia un errore             
            except:
                print(inputerror001)
                continue

            else:
                #qua il secondo ciclo adebito a mettere più di una risposta per avere più prodotti
                while True:
                    #chiedo cosa ordinare se non è un numero/è un numero al difuori del range 1:10 glielo dico, se lo è vado avanti
                    try:
                        scelta = int(input("scelta: "))

                    except:
                        print(inputerror001)
                        continue

                    else:
                        #la cascata di condizioni con il += che significa di aggungere al totale p1.prezzo o gli altri.
                        if scelta == 0: pass

                        elif scelta == 1: totale += p1.prezzo

                        elif scelta == 2: totale += p2.prezzo

                        elif scelta == 3: totale += p3.prezzo

                        elif scelta == 4: totale += p4.prezzo

                        elif scelta == 5: totale += bevanda1.prezzo

                        elif scelta == 6: totale += bevanda2.prezzo

                        elif scelta == 7: totale += bevanda3.prezzo

                        elif scelta == 8: totale += bevanda4.prezzo

                        elif scelta == 9: totale += bevanda5.prezzo

                        elif scelta == 10: totale += bevanda6.prezzo

                        else:
                            print(inputerror001)
                            continue

                    #contatore che si aggiunge ogni ciclo fino a superare il numeroP, in que caso si fermera prima (questo è il ciclo for)       
                    contatore += 1
                    
                    if contatore >= numeroP:
                        print("il totale è ", totale, "euro")
                        break

            sceltaC = input("continuare? si/no: ")

            #metto tutti i modi possibili di scrivere si e no
            if sceltaC == "si" or sceltaC == "SI" or sceltaC == "Si" or sceltaC == "sI" or sceltaC == "s" or sceltaC == "S":
                totale = 0
                numeroP = 0
                contatore = 0
                continue

            elif sceltaC == "no" or sceltaC == "NO" or sceltaC == "No" or sceltaC == "nO" or sceltaC == "n" or sceltaC == "N":
                print("programma arrestato")
                break

            #qua metto un else come se fosse un except
            else:
                print(inputerror001)
                continue

        elif utente == 2:
            try:
                #qua faccio cambiare tutti i nomi vegana o no e prezzi delle pizze, c sta per cambiamento
                c = str(input("scelta nome: "))
                p1.nome = c

                c2 = str(input("scelta vegana: "))
                p1.vegana = c2

                c3 = int(input("scelta prezzo: "))
                p1.prezzo = c3

                c4 = str(input("\nscelta nome: "))
                p2.nome = c4

                c5 = str(input("scelta vegana: "))
                p2.vegana = c5

                c6 = int(input("scelta prezzo: "))
                p2.prezzo = c6

                c7 = str(input("\nscelta nome: "))
                p3.nome = c7

                c8 = str(input("scelta vegana: "))
                p3.vegana = c8

                c9 = int(input("scelta prezzo: "))
                p3.prezzo = c9

                c10 = str(input("\nscelta nome: "))
                p4.nome = c10

                c11 = str(input("scelta vegana: "))
                p4.vegana = c11

                c12 = int(input("scelta prezzo: "))
                p4.prezzo = c12

                c13 = str(input("\nscelta nome: "))
                bevanda1.nome = c13

                c14 = str(input("scelta vegana: "))
                bevanda1.vegana = c14

                c15 = int(input("scelta prezzo: "))
                bevanda1.prezzo = c15

                c16 = str(input("\nscelta nome: "))
                bevanda2.nome = c16

                c17 = str(input("scelta vegana: "))
                bevanda2.vegana = c17

                c18 = int(input("scelta prezzo: "))
                bevanda2.prezzo = c18

                c19 = str(input("\nscelta nome: "))
                bevanda3.nome = c19

                c20 = str(input("scelta vegana: "))
                bevanda3.vegana = c20

                c21 = int(input("scelta prezzo: "))
                bevanda3.prezzo = c21

                c22 = str(input("\nscelta nome: "))
                bevanda4.nome = c22

                c23 = str(input("scelta vegana: "))
                bevanda4.vegana = c23

                c24 = int(input("scelta prezzo: "))
                bevanda4.prezzo = c24

                c25 = str(input("\nscelta nome: "))
                bevanda5.nome = c25

                c26 = str(input("scelta vegana: "))
                bevanda5.vegana = c26

                c27 = int(input("scelta prezzo: "))
                bevanda5.prezzo = c27

                c28 = str(input("\nscelta nome: "))
                bevanda6.nome = c28

                c29 = str(input("scelta vegana: "))
                bevanda6.vegana = c29

                c30 = str(input("scelta prezzo: "))
                bevanda6.prezzo = c30

            except:
                print(inputerror001)
                continue

            else:
                #menù appena creato delle pizze
                print("\nIl menu appena creato è il seguente:\nPizze:\n", "1-", p1.nome, "vegana?:", p1.vegana, p1.prezzo, "euro\n", "2-", p2.nome, "vegana?:", p2.vegana, p2.prezzo, "euro\n", "3-", p3.nome, "vegana?:", p3.vegana, p3.prezzo, "euro\n", "4-", p4.nome, "vegana?:", p4.vegana, p4.prezzo, "euro\n")
                #menu appena creato delle bevande(non perforza devono essere ragruppati cosi i prodotti ovviamente)
                print("Bevande:\n", "5-", bevanda1.nome, "vegana?", bevanda1.vegana, bevanda1.prezzo, "euro\n", "6-", bevanda2.nome, "vegana?", bevanda2.vegana, bevanda2.prezzo, "euro\n", "7-", bevanda3.nome, "vegana?", bevanda3.vegana, bevanda3.prezzo, "euro\n", "8-", bevanda4.nome, "vegana?", bevanda4.vegana, bevanda4.prezzo, "euro\n", "9-", bevanda5.nome, "vegana?", bevanda5.vegana, bevanda5.prezzo,"euro\n", "10-", bevanda6.nome, "vegana?", bevanda6.vegana, bevanda6.prezzo, "euro\n")

                #metto tutti i modi possibili di scrivere si e no

                sceltaC = input("continuare? si/no: ")

                if sceltaC == "si" or sceltaC == "SI" or sceltaC == "Si" or sceltaC == "sI" or sceltaC == "s" or sceltaC == "S":
                    totale = 0
                    numeroP = 0
                    contatore = 0
                    continue

                elif sceltaC == "no" or sceltaC == "NO" or sceltaC == "No" or sceltaC == "nO" or sceltaC == "n" or sceltaC == "N":
                    print("programma arrestato")
                    break

                else:
                    print(inputerror001)
                    continue
        
        else:
            print(inputerror001)
            continue