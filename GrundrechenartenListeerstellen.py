
### Erstellt Liste mit foglendem Schema
### Nummer; Rechnung; ErsteZahl; ZweiteZahl; Ergebnis; Rechenart; Zahlenraum
### 6 Zeilen

import csv

with open('AufgabenGrundrechenarten.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerow(["Nummer", "Rechnung", "ErsteZahl", "ZweiteZahl",
                     "Ergebnis", "Rechenart", "Zahlenraum", "Rest"])


l = []
b = []

a = 1001

## +
counter = 0
for i in range(0, a):
    for z in range(0, a):
        counter = counter + 1
        with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=",")

            writer.writerow([counter, str(i) + " + " + str(z) + "= ", str(i), str(z),
                             str(i + z), "+", str(i + z)])



for i in range(0, a):
    for z in range(0, a):

        if i > z:
            counter = counter + 1
            with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
                writer = csv.writer(f, delimiter=",")

                writer.writerow([counter, str(i) + " - " + str(z) + "= ", str(i), str(z),
                                 str(i - z), "-", str(i)])


for i in range(0, a):
    for z in range(0, a):
            if z != 0 and i != 0:
                counter = counter + 1
                with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=",")

                    writer.writerow([counter, str(i) + " * " + str(z) + "= ", str(i), str(z),
                                     str(i * z), "*", str(i * z)])
            elif z == 0 and i != 0:
                counter = counter + 1
                with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=",")

                    writer.writerow([counter, str(i) + " * " + str(z) + "= ", str(i), str(z),
                                     str(i * z), "*", str(i)])

            elif z != 0 and i ==0:
                counter = counter + 1
                with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=",")

                    writer.writerow([counter, str(i) + " * " + str(z) + "= ", str(i), str(z),
                                     str(i * z), "*", str(z)])

            elif z == 0 and i == 0:
                counter = counter + 1
                with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=",")

                    writer.writerow([counter, str(i) + " * " + str(z) + "= ", str(i), str(z),
                                     str(i * z), "*", "0"])


for i in range(0, a):
    for z in range(0, a):
            if z != 0 and i != 0 and i > z:
                counter = counter + 1
                with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=",")

                    writer.writerow([counter, str(i) + " / " + str(z) + "= ", str(i), str(z),
                                     str(round(i / z, 2)), "/", str(i), str(i % z)])

            elif i == 0 and z != 0:
                counter = counter + 1
                with open('AufgabenGrundrechenarten.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=",")

                    writer.writerow([counter, str(i) + " / " + str(z) + "= ", str(i), str(z),
                                     str(i / z), "/", str(z)])

            elif z == 0:
                pass







