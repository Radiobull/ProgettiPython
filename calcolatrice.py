#variabili
erroreInput = ("errore: 001 txt: errore nella digitazione")

totale = 0
num1 = 0
num2 = 0

while True:
        try:
                tipoCalcolo = int(input("benvenuto nella calcolatrice di Daniele Di Vita\n scegli un calcolo da fare tra:\n 1- addizione\n2- sotrazione\n3- moltiplicazione\n4- divisione\n5- potenza\n"))
                
                if tipoCalcolo < 1 or tipoCalcolo > 5:
                        raise exception
                        
                num1 = float(input("inserire il primo numero:\n"))
                num2 = float(input("inserire il secondo numero:\n "))
        except:
                print(erroreInput)
                continue
        else:
                try:
                        if tipoCalcolo == 1:
                                totale = num1 + num2
                                
                        elif tipoCalcolo == 2:
                                totale = num1 - num2
                                
                        elif tipoCalcolo == 3:
                                totale = num1 * num2
                                
                        elif tipoCalcolo == 4:
                                totale = num1 / num2
                                
                        elif tipoCalcolo == 5:
                                totale = num1 ** num2     
                except:
                        print(erroreInput)
                        continue
                else:
                        print("il risultato è ", totale)
                        try:
                                sceltaC = str(input("continuare? si o no\n"))
                        
                        except:
                                print(erroreInput)

                        else:        
                                if sceltaC == "si" or sceltaC == "SI" or sceltaC == "Si" or sceltaC == "sI" or sceltaC == "s" or sceltaC == "S":
                                        continue
                                
                                elif sceltaC == "no" or sceltaC == "NO" or sceltaC == "No" or sceltaC == "nO" or sceltaC == "n" or sceltaC == "N":
                                        print("programma arrestato")
                                        break
