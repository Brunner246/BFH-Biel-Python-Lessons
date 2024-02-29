# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def add_one(aNumber):
    return aNumber + 1


def printtest(something):
    print(f'something {something}')


name = input("Wie ist Ihr Name? ")
print("Hallo, " + name + "!")

a = float(input("Geben Sie die erste Zahl ein: "))
b = float(input("Geben Sie die zweite Zahl ein: "))

summe = a + b
differenz = a - b
produkt = a * b
quotient = a / b

print("Summe:", summe)
print("Differenz:", differenz)
print("Produkt:", produkt)
print("Quotient:", quotient)


def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False


for zahl in range(1, 101):
    if zahl % 3 == 0:
        print(zahl)


def durchschnitt(liste):
    return sum(liste) / len(liste)


liste = [2, 7, 1, 9, 4, 6]

max_zahl = max(liste)
min_zahl = min(liste)

print("Höchste Zahl:", max_zahl)
print("Niedrigste Zahl:", min_zahl)


def ist_palindrom(string):
    string = string.lower()
    string = string.replace(" ", "")
    return string == string[::-1]


def ist_primzahl(zahl):
    if zahl < 2:
        return False
    for i in range(2, zahl):
        if zahl % i == 0:
            return False
    return True


def primzahlen_bis(zahl):
    for i in range(2, zahl + 1):
        if ist_primzahl(i):
            print(i)


woerter = ["Apfel", "Banane", "Erdbeere", "Melone", "Kirsche", "Mango"]

for wort in woerter:
    if len(wort) > 5:
        print(wort)

# mein_tupel = (1, 2, 3)
# mein_tupel[0] = 4 # Dieser Code wird einen Fehler verursachen, da Tupel unveränderlich sind

mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}

# Variablen in Python

# Deklaration und Zuweisung von Werten
x = 5
y = 3.14
z = "Hallo, Welt!"

# Ausgabe der Werte
print("Der Wert von x ist:", x)
print("Der Wert von y ist:", y)
print("Der Wert von z ist:", z)

# Verwendung von Variablen in Ausdrücken
a = x + 10
b = y * 2
c = z + " Wie geht es dir?"

# Ausgabe der Ergebnisse
print("Der Wert von a ist:", a)
print("Der Wert von b ist:", b)
print("Der Wert von c ist:", c)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hallo BFH')
    printtest(3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
