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

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?=#@$%<>^&*().,' #Richtlinie: Groß- und Kleinschreibung, Zahlen und Sonderzeichen

number = input('Wieviele Passwörter sollen generiert werden? ') #Anzahl der Passwörter
number = int(number)

length = input('Wie lang soll das Passwort sein? ') #Anzahl der Zeichen
length = int(length)

print('\nHier sind die Passwörter:')
print()
for pwd in range(number): #Anzahl der Passwörter
  password = ''
  for c in range(length): #Länge des Passworts
    password += random.choice(chars) #Randomisiert die Zeichen im Passwort
  print(password)
print('''
Fertig!
''')
input('Drücke "Enter" um das Fenster zu schließen.') #Fenster schließen
