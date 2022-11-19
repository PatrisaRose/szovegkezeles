szoveg = input("Kérlek adj meg egy szöveget: ")
def nagybetu():
    print(szoveg.upper())

def hosszabb10nel():
    if len(szoveg) >= 10:
        print("Nagyobb mint 10.")
    else:
        print("Nem nagyobb mint 10.")

def legalabb3():
    sz = input("Kérlek adj meg egy 3 betűs szót: ")
    while len(sz) < 3:
        sz = input("Hiba! Nem éri el a szavad a 3 karaktert: ")


def betu():
    betuk = 0
    for betu in szoveg:
        if betu == "a":
            betuk += 1
            eredmeny = "Van benne 'a' betű"
        else:
            eredmeny = "Nincs benne 'a' betű"
    print(eredmeny)

    print(betuk)

def elsoa():
    i = 0
    while i < len(szoveg):
        if szoveg[i] == "a":
            eredmeny = f"Az első 'a' betű pozíciója: {i}"
            break
        else:
            eredmeny = "A szöveg nem tartalmaz 'a' betűt!"

        i += 1
    print(eredmeny)

def nevek():
    nevek = []
    nev = input("Kérlek adj meg neveket, ha nem szeretnél több nevet megadni, a név után használj @-t")
    while nev != "@":
        nevek.append(nev)
        nev = input("Kérlek adj meg neveket, ha nem szeretnél több nevet megadni, a név után használj @-t: ")

    print(nevek)


