## Level 1: Zahlen bis 10, 2 Fragen
## Level 2: Zahlen bis 20, 3 Fragen
## Level 3: Zahlen bis 100, 5 Fragen


#import KlasseAufgaben
#import K
import pandas as pd


#KlasseEnter.Enter().login_or_register()

#KlasseAufgaben.AufgabenAdd(1).execute()

print("Hallo")


df = pd.read_csv("/Users/Chris/Desktop/MatheProjekt/AufgabenGrundrechenarten.csv")


df2= df[df["ErsteZahl"] <= 10]
df3= df2[df2["Zahlenraum"] < 11]
df4= df3[df3["Rechenart"] == "/"]
df5= df4[df4["ZweiteZahl"] <= 9]

print(df5)
