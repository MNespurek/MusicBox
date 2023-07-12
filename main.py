import pickle
from muzikanti import Muzikanti

muzikanti = Muzikanti()
pokracovat = True
while pokracovat:
    print('------MusicBox------')
    print('Vypište číslo pro další akci:')
    print('1 přidej žánr')
    print('2 vypiš žánr')
    print('3 přidej album')
    print('4 vypiš alba')
    print('5 přidej skladbu')
    print('6 vypiš skladby')
    print('7 přidej album skladbu')
    print('8 vypiš album skladby')
    print('9 přidej interpreta')
    print('10 vypiš interprety')
    print('11 přidej album interpreta')
    print('12 vypiš album interpreta')
    print('13 přidej národnost')
    print('14 vypiš národnosti')
    print('15 konec')

    vstup = input()
    if not vstup.isdigit():
        print("zadaná hodnota není číselná, opakujte zadání")
    else:
        if vstup == "1":
            pridej_z = input("Zadejte název žánru, který chcete přidat:\n")
            print(muzikanti.pridej_zanr(pridej_z))
            print("Žánr byl uložen")
        if vstup == "2":
            muzikanti.vypis_zanr()
            id_typ_zanr = input()
        if vstup == "3":    
            print(("Vyberte ze seznamu žánrů id_zanru, ke kterému album chcete přidat"))
            muzikanti.vypis_zanr()
            id_typ_zanr = input()
            nazev = input("Zadejte název alba:\n")
            datum_vydani = input("Zadejte datum vydání alba")
            muzikanti.pridej_album(nazev, id_typ_zanr, datum_vydani)
            print("album bylo přidáno")
        if vstup == "4":
            muzikanti.vypis_alb()
        if vstup == "5":
            nazev = input("Zadejte název skladby:\n")
            delka = input("Zadejte délku skladby v sekundách:\n")
            print(muzikanti.pridej_skladbu(nazev, delka))
            print("skladba byla přidána")
        if vstup == "6":
            print(muzikanti.vypis_skladby())
        if vstup == "7":
            print("Vyberte id_album ze kterého chcete vytvořit album skladbu\n")
            print(muzikanti.vypis_alb())
            id_album = input()
            print("vyberte skladbu ze které chcete vytvořit album skladbu:\n")
            print(muzikanti.vypis_skladby())
            id_skladba = input()
            cislo_stopy = input("Vložte číslo stopy, které chcete skladbě určit:\n")
            muzikanti.pridej_album_skladba(id_album, id_skladba, cislo_stopy)
            print("Album skladba byla úspěšně vytvořena")
        if vstup == "8":
            print(muzikanti.vypis_cisla_stopy())
        if vstup == "9":
            print("Vypište id_narodnost, kterou interpret má:\n")
            print(muzikanti.vypis_narodnost())
            id_narodnost = input()
            nazev = input("Vložte název interpreta:\n")
            muzikanti.pridej_interpreta(id_narodnost, nazev)
            print("Interpret byl přidán")                
        if vstup == "10":
            print(muzikanti.vypis_interpreta())
        if vstup == "11":
            print("Vypište id_album ze kterého chcete vytvořit album skladbu\n")
            print(muzikanti.vypis_alb())
            id_album = input()
            print("Vypište id_interpreta, kterého chcete přidat:\n")
            print(muzikanti.vypis_interpreta())
            id_interpret = input()
            muzikanti.pridej_album_interpret(id_album, id_interpret)
            print("Album interpret byla úspěšně vytvořena")
        if vstup == "12":
            print(muzikanti.vypis_album_interpret())
        if vstup == "13":
            print('Zadejte národnost, kterou chcete přidat do seznamu')
            nazev = input()
            print(muzikanti.pridej_narodnost(nazev))
            print('Národnost byla úspěšně přidána')
        if vstup == "14":
            print(muzikanti.vypis_narodnost())
        if vstup == "15":
            pokracovat = False
