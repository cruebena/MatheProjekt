## Level 1: Zahlen bis 10, 2 Fragen
## Level 2: Zahlen bis 20, 3 Fragen
## Level 3: Zahlen bis 100, 5 Fragen
from random import randint


class Aufgaben():
    def __init__(self, level):
        self.level = level
        if self.level == 1:
            self.zahlen_raum = 10
            self.anzahl_fragen = 2
        elif self.level == 2:
            self.zahlen_raum = 20
            self.anzahl_fragen = 3
        elif self.level == 3:
            self.zahlen_raum = 100
            self.anzahl_fragen = 5
        self.erste_zahl = 0
        self.zweite_zahl = 0
        self.ergebnis = 0
        self.richtige_antwort = 0
        self.falsche_antwort = 0

    def erstelle_aufgabe(self):
        print("Was gibt folgende Aufgabe?")

    def teste(self):
        eingabe = input("Gebe dein Ergebnis ein: ")
        if str(self.ergebnis) == eingabe:
            print("Sehr gut!")
            print()
            return True
        else:
            print("Leider nicht richtig. Das Ergebnis ist: " + str(self.ergebnis))
            print()
            return False

    def antwort_counter(self):
        antwort = self.teste()
        if antwort == True:
            self.richtige_antwort = self.richtige_antwort + 1
        else:
            self.falsche_antwort = self.falsche_antwort + 1

    def execute(self):
        for i in range(1, self.anzahl_fragen + 1):
            self.berechnen()
            self.erstelle_aufgabe()
            self.antwort_counter()
        print("Du hast " + str(self.richtige_antwort) + " richtig und "
              + str(self.falsche_antwort) + " falsch beantwortet.")
        print()
        if self.falsche_antwort == 0:
            return True
        else:
            return False


class AufgabenAdd(Aufgaben):
    def __init__(self, level):
        super().__init__(level)

    def berechnen(self):
        self.erste_zahl = randint(0, self.zahlen_raum + 1)
        self.zweite_zahl = randint(0, self.zahlen_raum + 1)
        self.ergebnis = self.erste_zahl + self.zweite_zahl
        while self.ergebnis > self.zahlen_raum:
            self.erste_zahl = randint(0, self.zahlen_raum + 1)
            self.zweite_zahl = randint(0, self.zahlen_raum + 1)
            self.ergebnis = self.erste_zahl + self.zweite_zahl

    def erstelle_aufgabe(self):
        super().erstelle_aufgabe()
        print(str(self.erste_zahl) + " + " + str(self.zweite_zahl))


class AufgabenSub(Aufgaben):
    def __init__(self, level):
        super().__init__(level)

    def berechnen(self):
        self.erste_zahl = randint(0, self.zahlen_raum + 1)
        self.zweite_zahl = randint(0, self.zahlen_raum + 1)
        self.ergebnis = self.erste_zahl - self.zweite_zahl
        while self.ergebnis < 0:
            self.erste_zahl = randint(0, self.zahlen_raum + 1)
            self.zweite_zahl = randint(0, self.zahlen_raum + 1)
            self.ergebnis = self.erste_zahl - self.zweite_zahl

    def erstelle_aufgabe(self):
        super().erstelle_aufgabe()
        print(str(self.erste_zahl) + " - " + str(self.zweite_zahl))


class AufgabenMul(Aufgaben):
    def __init__(self, level):
        super().__init__(level)

    def berechnen(self):
        self.erste_zahl = randint(0, self.zahlen_raum + 1)
        self.zweite_zahl = randint(0, self.zahlen_raum + 1)
        self.ergebnis = self.erste_zahl * self.zweite_zahl
        while self.ergebnis > self.zahlen_raum:
            self.erste_zahl = randint(0, self.zahlen_raum + 1)
            self.zweite_zahl = randint(0, self.zahlen_raum + 1)
            self.ergebnis = self.erste_zahl * self.zweite_zahl

    def erstelle_aufgabe(self):
        super().erstelle_aufgabe()
        print(str(self.erste_zahl) + " * " + str(self.zweite_zahl))


class AufgabenDiv(Aufgaben):
    def __init__(self, level):
        super().__init__(level)

    def berechnen(self):
        self.erste_zahl = randint(0, self.zahlen_raum + 1)
        self.zweite_zahl = randint(1, self.zahlen_raum + 1)
        self.ergebnis = self.erste_zahl / self.zweite_zahl
        self.ergebnis = int(self.ergebnis)
        modulo = self.erste_zahl % self.zweite_zahl
        while modulo > 0:
            self.erste_zahl = randint(0, self.zahlen_raum + 1)
            self.zweite_zahl = randint(1, self.zahlen_raum + 1)
            self.ergebnis = self.erste_zahl / self.zweite_zahl
            self.ergebnis = int(self.ergebnis)
            modulo = self.erste_zahl % self.zweite_zahl

    def erstelle_aufgabe(self):
        super().erstelle_aufgabe()
        print(str(self.erste_zahl) + " / " + str(self.zweite_zahl))


objekt = AufgabenDiv(1)
perfect = objekt.execute()