
import csv


n = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   # Lista där varje siffra står för en postion på spelbrädet.

games = 0
wins1 = 0
wins2 = 0
draw = 0
count = 0                                            # Variabler som samlar data för statistik.
moves1 = 0
moves2 = 0

draws = []
moves = []                                           # Listor för att lagra in statistik.
moves_list1 = []
moves_list2 = []

def store_stats(number):
    """Funktion som lagar variabelvärde i CVS filen.""" 
    statsfile = open("stats.csv","a")
    statsfile.write(str(number))
    statsfile. write(" ")                            # Skriver in ett mellanrum efter varje siffra som kommer användas i print_stats.
    statsfile.close()
    

def print_stats():
    """Funktion som skriver ut variabelvärden från CVS filen."""
    statsfile = open("stats.csv")
    reader = csv.reader(statsfile, delimiter=" ")
    line = 0
    for row in reader:                                         # Läser varje värde i filen och skiljer dem med mellanrummet.
        if line == 0:
            print(f'Antal spelade spel: {row[0]}')             # Läser rad ett i filen på index 0.
            print(f'Antal vinster spelare 1: {row[1]}')
            print(f'Antal vinster spelare 2: {row[2]}')
            print(f'Antal oavgjorda: {row[3]}')
            print(f'Procent oavgjorda: {row[4]}%')
            print(f'Procent vunna av spelare 1: {row[5]}%')
            print(f'Procent vunna av spelare 2: {row[6]}%')
            print(f'Genomsnitt antal drag per spel: {row[7]}')
            print(f'Genomsnitt antal drag för vinst spelare 1: {row[8]}')
            print(f'Genomsnitt antal drag för vinst spelare 2: {row[9]} ')
    statsfile.close()

def printboard():
    """Funktion som skriver ut hur spelbrädet ser ut."""
    numb_list1 = " ".join(n)
    print(f'| {n[0]} | {n[1]} | {n[2]} |\n| {n[3]} | {n[4]} | {n[5]} |\n| {n[6]} | {n[7]} | {n[8]} |') # Skriver ut listan "n" och vad som finns i varje index.

def reset_board():
    """Återställer spelbrädet."""
    n.clear()                                               # Nollställer listan.
    n.extend(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) # Fyller på med nya värden.     

def move():
    """Låter spelare 1 göra ett drag, hanterar också om spelaren gör ett felaktigt drag."""
    global moves1                                                                                                   # Importerar variabel som ska räkna antal drag för spelare1  
    while True:
        try:
            pos = int(input("\nSpelare 1!\nVar vill du göra din markering, skriv en siffra: "))
            pos = pos-1                                                                                             # Minskar input för att matcha listans index. 
        
            if n[pos] == "O":
                print("Ajdå du gjorde ett felaktigt drag positionen var redan upptagen\nVi gör ett nytt försök! ")
                moves1 - 1                                                                                          # Ser till att ett felaktigt drag inte räknas med.
                printboard()
            elif n[pos] == "X":
                print("Ajdå du gjorde ett felaktigt drag positionen var redan upptagen\nVi gör ett nytt försök! ")
                moves1 - 1
                printboard()
            else:
                n[pos] = "X"                                                                                        # Ändrar listans index till X.
                moves1 += 1                                                                                         # Ett godkänt drag räknas med. 
                break
        except ValueError:
            print("Skriv in en siffra som matchar positionen du vill placera din markör!")                          # Felmeddelande för felaktig input.
            printboard()

def move2():
    """Låter spelare 2 göra ett drag, hanterar också om spelaren gör ett felaktigt drag."""
    global moves2
    while True:
        try:
            pos = int(input("\nSpelare 2!\nVar vill du göra din markering, skriv en siffra: "))
            pos = pos-1
        
            if n[pos] == "X":
                print("Ajdå du gjorde ett felaktigt drag positionen var redan upptagen\nVi gör ett nytt försök!")
                moves2 - 1
                printboard()
            elif n[pos] == "O":
                print("Ajdå du gjorde ett felaktigt drag positionen var redan upptagen\nVi gör ett nytt försök!")
                moves2 - 1
                printboard()    
            else:
                n[pos] = "O"
                moves2 += 1
                break
        except ValueError:
            print("Skriv in en siffra som matchar positionen du vill placera din markör!")
            printboard()

def win():
    """Kollar om spelaren gjort ett vinnande drag"""
    if (n[0] == n[1] == n[2]):                          
        return True                                   # Om listans olika index inehåller samma värde returneras True, alltså ett vinnande drag.
    elif(n[3] == n[4] == n[5]):
        return True
    elif(n[6] == n[7] == n[8]):
        return True
    elif(n[0] == n[3] == n[6]):
        return True
    elif(n[1] == n[4] == n[7]):
        return True
    elif(n[2] == n[5] == n[8]):
        return True
    elif(n[0] == n[4] == n[8]):
        return True
    elif(n[2] == n[4] == n[6]):
        return True
    
def check_win():
    """Kollar vem som har vunnit och lagar vinster i variabel."""
    global wins1                                       # Importerar variabler vars värden ska öka om en vinst registreras.
    global wins2
    ply1 = n.count("X")                                # Räknar igenom listan och kollar hur många det finns av respektive markör. 
    ply2 = n.count("O")                                
    if ply1 > ply2:                                    # Om det finns fler X än O på brädet när en vinst registrerats är det spelare 1 som är vinnare.  
        wins1 += 1                                     # Adderar en vinst till spelare 1.
        print("\nGrattis spelare 1 du är vinnaren!\n")
    elif ply1 == ply2:                                 # Om det finns lika många av varje markör när en vinst registrerats är det spelare 2 som är vinnare.
        wins2 += 1                                     # Adderar vinst till spelare 2.
        print("\nGrattis spelare 2 du är vinnaren!\n")

def play():
    """Kör igenom spelsekvensen"""
    global count                             # Importerar variabel för att räkna om det har blivit oavgjort. 
    global draw                              # Variabel som adderas varje gång det blir oavgjort.
    while count < 13:                        # Programmet körs så länge brädet inte är fullt.
        move()                               # Gör draget.
        count += 1
        win()                                # Kollar om det blev en vinst.
        if win() == True:                    # Om vi får en vinst.
            check_win()                      # Kolla vem som har vunnit.
            printboard()                     
            moves_list1.append(moves1)       # Hur många drag som har gjorts läggs till i listan på drag för spelare 1.
            moves.append(moves1 + moves2)    # Drag för spelare 1 och 2 lägg till i listan för totala antal drag.
            return count
            break
        if count == 13:                      # Eftersom att spelare 1 kommer göra det sista draget kollar vi om count har blivit 13, om så är fallet har det blivit oavgjort.
            moves.append(moves1 + moves2)    # Totala antalet drag läggs till i listan för totala antal drag.
            draw += 1                        # Oavgjort läggs till.
            draws.append(draw)               # Oavgjort läggs till i lista.  
            print("\nDet blev oagjort!\n")
            break
        printboard()
        move2()
        count += 1
        win()
        if win() == True:
            check_win()
            printboard()
            moves_list2.append(moves2)
            moves.append(moves1 + moves2)
            return count
            break
        printboard()
        count += 1
        


games = 0

while True:
    inp = input("Hej och välkommen till luffarschack!\nFör att spela tryck: 1\nFör att avsluta och få statistik tryck: 2\n>:")
    reset_board()
    count = 0            # Återställer count för ett nytt spel.
    moves1 = 0           # Återställer antal drag för spelare 1.
    moves2 = 0           # Återställer antal drag för spelare 2.
    if inp == "1":       # Väljer att spela.
        printboard()
        games += 1       # Registrera att ett spel har spelats.
        play()           # Spelet körs.
    elif inp == "2":     # Spelet avslutas. 
        break
    else:
        print(">Skriv en siffra 1 eller 2<")    


"""Nedanför lagrar jag in data från spelet"""

store_stats(games)                                 # Antal spelade matcher.  
store_stats(wins1)                                 # Antal vinster spelare 1.
store_stats(wins2)                                 # Antel vinster spelare 2.
store_stats(draw)                                  # Antal oavgjorda.
if draw == 0:
    store_stats(0)                                 # Om det inte blivit oavgjort lagras 0.
else:
    store_stats(draw/games*100)                    # Procent oavjorda.

if wins1 == 0:
    store_stats(0)                                 # Om spelare 1 inte vunnit lagaras 0.
else:
    store_stats(wins1/games*100)                   # procent vinster spelare 1.

if wins2 == 0:                                     
    store_stats(0)                                 # Om spelare 2 inte vunnit lagaras 0.
else:
    store_stats(wins2/games*100)                   # Procent vinster spelare 2.

store_stats(sum(moves)/len(moves))                 # Drag i genomsnitt per spel.  
if moves_list1 == []:
    store_stats(0)
else:
    store_stats(sum(moves_list1)/len(moves_list1)) # drag i genomsnitt för vinst spelare 1.

if moves_list2 == []:
    store_stats(0)
else:
    store_stats(sum(moves_list2)/len(moves_list2)) # Drag i genomsnitt för vinst spelare 2.
print_stats()                                      # Skriver ut all statistik.


open('stats.csv', 'w').close()                     # Återställer filen.
"""
Kvar att göra: 
Lägga till input-kontroll
Klasser

"""


