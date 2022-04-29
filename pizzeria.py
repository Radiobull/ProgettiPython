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

bevanda1 = Prd("Birra bionda (media)", 5.50, True)
bevanda2 = Prd("Birra bionda (grande)", 7.00, True)

bevanda3 = Prd("Birra rossa (media)", 5.50, True)
bevanda4 = Prd("Birra rossa (grande)", 7.00, True)

bevanda5 = Prd("Bottiglietta d'acqua 0,5 L (naturale)", 2.00, True)
bevanda6 = Prd("Bottiglietta d'acqua 0,5 L (frizzante)", 2.50, True)

#variabili
totale = 0

numeroP = 0

inputerror001 = "errore: 0001 txt: hai sbagliato a digitare"

contatore = 0

#un ciclo while che simula un ciclo do (vedi sotto)
while True:
    #il menù
    print("benvenuto gentile cliente, il menù è il seguente:\n")
    #il commando altro e le pizze
    print("Altro:\n 0- vuoto\n \nPizze:\n", "1-", p1.nome, "vegana?:", p1.vegana, p1.prezzo, "euro\n", "2-", p2.nome, "vegana?:", p2.vegana, p2.prezzo, "euro\n", "3-", p3.nome, "vegana?:", p3.vegana, p3.prezzo, "euro\n", "4-", p4.nome, "vegana?:", p4.vegana, p4.prezzo, "euro\n")
    #le bevande
    print("Bevande:\n", "5-", bevanda1.nome, bevanda1.prezzo, "euro\n", "6-", bevanda2.nome, bevanda2.prezzo, "euro\n", "7-", bevanda3.nome, bevanda3.prezzo, "euro\n", "8-", bevanda4.nome, bevanda4.prezzo, "euro\n", "9-", bevanda5.nome, bevanda5.prezzo,"euro\n", "10-", bevanda6.nome, bevanda6.prezzo, "euro\n")

    #qua provo a vedere se funziona col try ma se e minore di 0 la richiesta manda errore
    try:
        numeroP = int(input("quante portate vuole ordinare?: "))

        if numeroP < 1:
            raise exception

    #qua c'è il blocco per il caso in qui ci sia un errore             
    except:
        print(inputerror001)
        continue

    else:
        while True:
            #chiedo cosa ordinare se non è un numero/è un numero al difuori del range 1:10 glielo dico, se lo è vado avanti
            try:
                scelta = int(input("scelta: "))

            except:
                print(inputerror001)
                continue

            else:
                if scelta == 0: pass

                elif scelta == 1: totale +=p1.prezzo

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

    sceltaC = str(input("continuare? si/no: "))

    #metto tutti i modi possibili di scrivere si e no
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