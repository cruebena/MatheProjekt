import csv



class Enter():
    def __init__(self):
        self.vorname = 0
        self.nachname = 0
        self.username = 0
        self.passwort = 0
        self.geburtsdatum = 0
        self.klasse = 0

    def login_or_register(self):
        print("Willst du dich einloggen (l) oder dich registrieren (r) ?")
        a = input("")
        if str(a) == "l":
            print("Du wirst dich einloggen")
            self.login()
        else:
            print("Niels geht mir auf die EIER")
            self.register()

    def login(self):
        self.username = input("Gib deinen Nutzernamen ein: ")
        self.passwort = input("Wie lautet deine Passwort? ")
        print(self.username)
        print(self.passwort)

        d = {}
        with open('logindata.csv', 'r', newline= '') as f:
            for i in f:
                data = i.strip().split(";")
                d[data[0]] = data[1]

        if self.username in d:
            if self.passwort == d[self.username]:
                print("Username und Passwort richtig")
            else:
                print("Versuch dich erneut einzuloggen.")
                self.login()
        else:
            print("Du bist leider noch nicht registriert. Du wirst automatisch zum registrieren geschickt.")
            self.register()


    def register(self):
        self.vorname = input("Gibt deinen Vornamen einL: ")
        self.nachname = input("Gib deinen Nachnamen ein: ")
        self.username = input("Lege einen Nutzernamen ein: ")
        self.passwort = input("Gib ein Passwort ein: ")
        self.geburtsdatum = input("Wann bist du geboren? (xx.xx.xxxx)")
        self.klasse = input("In welche Klasse gehst du?")
        l = []
        l = [self.vorname, self.nachname, self.username, self.geburtsdatum, self.klasse]

        with open('pupils.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(l)

        l2 = [self.username, self.passwort]

        with open('logindata.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(l2)

        print("Du bischt ein neuer Nutzer, du Hund!!")
        print()
        print("Kannst dich jetzt einloggen!!")
        self.login()