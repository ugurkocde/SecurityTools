# Code ist auf Github
# Privates Repository
# Dokumentation ist auf Orgavision

import random

print('''
Passwort Generator - Version 0.3
----------------------
 Für: IMMAC Holding AG
----------------------
   Autor: Ugur Koc
----------------------
  Stand: 17.01.2020
----------------------
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?=@£$%^&*().,0123456789' #Richtlinie: Groß- und Kleinschreibung, Sonderzeichen und Zahlen

number = input('Wieviele Passwörter sollen generiert werden? ') #Anzahl der Passwörter
number = int(number)

length = input('Wie lange soll das Passwort sein? ') #Anzahl der Zeichen
length = int(length)

print('\nHier sind die Passwörter:')

for pwd in range(number): #
  password = ''
  for c in range(length):
    password += random.choice(chars) #Randomisiert die Zeichen im Passwort
  print(password)
print('''
Fertig!
''')
input('Drücken Sie eine Taste um das Fenster zu schließen') #Fenster schließen
