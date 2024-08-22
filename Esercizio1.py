import math
def main():
    #Chiedo all-utente di fare la scelta per il calcolo
    scelta = int(input("\nPremi:\n 1) per calcolo perimetro quadrato\n2) per calcolo circonferenza\n3) per perimetro rettangolo\n"))
    if (scelta == 1) : calcolo_perimetro_quadrato()
    elif (scelta == 2) : calcolo_circonferenza()
    elif (scelta == 3) : calcolo_perimetro_rettangolo()
    else: print ("Scelta non consentita")

#Funzione di calcolo perimetro quadrato
def calcolo_perimetro_quadrato():
    l = int(input("Inserisci lunghezza lato quadrato: "))
    p = l * 4
    print(f"Il perimetro e' {p}")

#Funzione di calcolo circonferenza cerchio
def calcolo_circonferenza():
    r = float(input("Inserisci circonferenza cerchio: "))
    c = 2 * math.pi * r
    print(f"La circonferenza è {c}")

#Funzione di calcolo perimetro rettangolo
def calcolo_perimetro_rettangolo():
    b = int(input("Inserisci lunghezza base rettangolo: "))
    h = int(input("Inserisci lunghezza base rettangolo: "))
    p = b * 2 + h * 2
    print(f"Il perimetro è {p}")

main()    