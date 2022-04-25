#classi per ragruppare varie propieta per le pizze e bevande
class pizza1:
    def __init__(self, nomeP, prezzoP, vegana):
        
        self.nomeP = nomeP
        self.prezzoP = prezzoP
        self.vegana = vegana

p1 = pizza1("Margherita", 4.50, True)


class pizza2:
    def __init__(self, nomeP, prezzoP, vegana):

        self.nomeP = nomeP
        self.prezzoP = prezzoP
        self.vegana = vegana

p2 = pizza2("Patapizza", 6.50, True) 

class pizza3:
    def __init__(self, nomeP, prezzoP, vegana):

        self.nomeP = nomeP
        self.prezzoP = prezzoP
        self.vegana = vegana

p3 = pizza3("Pistacchiosa", 7.00, False)

class pizza4:
    def __init__(self, nomeP, prezzoP, vegana):

        self.nomeP = nomeP
        self.prezzoP = prezzoP
        self.vegana = vegana

p4 = pizza4("Norma", 8.50, True)

class bevanda1:
    def __init__(self, nomeB, prezzoB):

        self.nomeB = nomeB
        self.prezzoB = prezzoB

bevanda1a = bevanda1("Birra bionda (media)", 5.50)
bevanda1b = bevanda1("Birra bionda (grande)", 7.00)

class bevanda2:
    def __init__(self, nomeB, prezzoB):

        self.nomeB = nomeB
        self.prezzoB = prezzoB

bevanda2a = bevanda2("Birra rossa (media)", 5.50)
bevanda2b = bevanda2("Birra rossa (grande)", 7.00)

class bevanda3:
    def __init__(self, nomeB, prezzoB):

        self.nomeB = nomeB
        self.prezzoB = prezzoB

bevanda3a = bevanda3("Bottiglietta d'acqua (naturale)", 2.00)
bevanda3b = bevanda3("Bottiglietta d'acqua (frizzante)", 2.50)

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
    print("Altro:\n 0- vuoto\n \nPizze:\n", "1-", p1.nomeP, "vegana?:", p1.vegana, p1.prezzoP, "euro\n", "2-", p2.nomeP, "vegana?:", p2.vegana, p2.prezzoP, "euro\n", "3-", p3.nomeP, "vegana?:", p4.vegana, p3.prezzoP, "euro\n", "4-", p4.nomeP, "vegana?:", p4.vegana, p4.prezzoP, "euro\n")
    #le bevande
    print("Bevande:\n", "5-", bevanda1a.nomeB, bevanda1a.prezzoB, "euro\n", "6-", bevanda1b.nomeB, bevanda1b.prezzoB, "euro\n", "7-", bevanda2a.nomeB, bevanda2a.prezzoB, "euro\n", "8-", bevanda2b.nomeB, bevanda2b.prezzoB, "euro\n", "9-", bevanda3a.nomeB, bevanda3a.prezzoB,"euro\n", "10-", bevanda3b.nomeB, bevanda3b.prezzoB, "euro\n")

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

                elif scelta == 1: totale = totale + p1.prezzoP

                elif scelta == 2: totale = totale + p2.prezzoP

                elif scelta == 3: totale = totale + p3.prezzoP

                elif scelta == 4: totale = totale + p4.prezzoP

                elif scelta == 5: totale = totale + bevanda1a.prezzoB

                elif scelta == 6: totale = totale + bevanda1b.prezzoB

                elif scelta == 7: totale = totale + bevanda2a.prezzoB

                elif scelta == 8: totale = totale + bevanda2b.prezzoB

                elif scelta == 9: totale = totale + bevanda3a.prezzoB

                elif scelta == 10: totale = totale + bevanda3b.prezzoB

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