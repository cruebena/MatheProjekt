import pandas as pd
import csv

class AdditionZahlenraum10():

    def __init__(self):
        pass

    def definiere_Liste(self):
        liste = []
        with open('WechselndeAufgaben.csv', 'w', newline='') as g:
            writer = csv.writer(g, delimiter=";")
            writer.writerow(["Nummer", "Rechnung", "ErsteZahl", "ZweiteZahl",
                     "Ergebnis", "Rechenart", "Zahlenraum", "Rest"])

        with open('/Users/Chris/Desktop/MatheProjekt/AufgabenGrundrechenarten.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            for i in reader:
                if str(i[2])=="ErsteZahl":
                    print("Header")
                    continue
                else:
                    if int(i[2]) <= 10 and int(i[3]) <= 10 and i[5] =="+" and int(i[6]) <= 10:
                        with open('WechselndeAufgaben.csv', 'a', newline='') as g:
                            writer = csv.writer(g, delimiter=";")
                            writer.writerow(i)


    def erstelle_Aufgaben(self):
        counter = 0
        with open('WechselndeAufgaben.csv', 'r', newline='') as g:
            reader = csv.reader(g, delimiter=";")
            for i in reader:
                counter = counter + 1
        print(counter)

#
#    #  for a in range(1,4):
#          with open('WechselndeAufgaben.csv', 'r', newline='') as g:
#              reader = csv.reader(g, delimiter=";")
#              for i in reader:
#


l = []

object = AdditionZahlenraum10()
object.definiere_Liste()
object.erstelle_Aufgaben()
