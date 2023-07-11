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

    print('9 pro ukončení')
    vstup = input()
    if not vstup.isdigit():
        print("zadaná hodnota není číselná, opakujte zadání")
    else:
        if vstup == "1":
            pridej_tz = input("Zadejte název žánru, který chcete přidat:\n")
            print(muzikanti.pridej_zanr(pridej_tz))
            print("Žánr byl uložen")
        if vstup == "2":
            print(muzikanti.vypis_zanr())
        if vstup == "3":
            print("Vyberte ze seznamu žánrů id_zanru, ke kterému album chcete přidat")
            print(muzikanti.vypis_zanr())
            id_typ_zanr = input()
            nazev = input("Zadejte název alba:\n")
            datum_vydani = input("Zadejte datum vydání alba")
            muzikanti.pridej_album(id_typ_zanr, nazev, datum_vydani)
            print("album bylo přidáno")
        if vstup == "4":
            print(muzikanti.vypis_alb())
        if vstup == "5":
            nazev = input("Zadejte název skladby:\n")
            delka = input("Zadejte délku skladby v sekundách:\n")
            print(muzikanti.pridej_skladbu())
            print("skladba byla přidána")
        if vstup == "6":
            print(muzikanti.vypis_skladby)
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
        if vstup == "13":
            print('Zadejte národnost, kterou chcete přidat do seznamu')
            print(muzikanti.pridej_narodnost())
            print('Národnost byla úspěšně přidána')
        if vstup == "14":
            print(muzikanti.vypis_narodnost())
        


        if vstup == "9":
            pokracovat = False
