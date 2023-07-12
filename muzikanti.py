import pickle
from zanr import Zanr
from album import Album
from skladba import Skladba
from album_skladba import AlbumSkladba
from interpret import Interpret
from narodnost import Narodnost
from album_interpret import AlbumInterpret

class Muzikanti:
    seznam_zanru = []
    seznam_alb = []
    seznam_album_skladba = []
    seznam_skladeb = []
    seznam_album_interpret = []
    seznam_interpret = []
    seznam_narodnost = []
   

# funkce pro přidání žánru
    def pridej_zanr(self, pridej_z):
        zanr = Zanr(pridej_z)
        self.seznam_zanru.append(zanr)
        file = open('zanr', 'wb')
        pickle.dump(self.seznam_zanru, file)

# vypiš žánry ze seznamu    
    def vypis_zanr(self):
        print('ID žánru\tNázev\n')
        file = open('zanr', 'rb')
        data = pickle.load(file)
        for item in data:
            print(item.id, item.nazev)
    
# funkce pro přidání alba
    def pridej_album(self, id_typ_zanr, nazev, datum_vydani):
        album = Album(nazev, id_typ_zanr, datum_vydani)
        self.seznam_alb.append(album)
        file = open('album', 'wb')
        pickle.dump(self.seznam_alb, file)

# vypis všech alb
    def vypis_alb(self):
        print('ID alba\tNázev alba\n')
        file = open('album', 'rb')
        data = pickle.load(file)
        for item in data:
            print(item.id, item.nazev)
    
# funkce pro přidání skladby
    def pridej_skladbu(self, nazev, delka):
        skladba = Skladba(nazev, delka)
        self.seznam_skladeb.append(skladba)
        file = open('skladby', 'wb')
        pickle.dump(self.seznam_skladeb, file)

# výpis všech skladeb
    def vypis_skladby(self):
        print('ID skladby\tNázev\n')
        file = open('skladby', 'rb')
        data = pickle.load(file)
        for item in data:
            print(f"{item.id}\t{item.nazev}")

# funkce pro přidání album skladeb
    def pridej_album_skladba(self, id_album, id_skladba, cislo_stopy):
        album_skladba = AlbumSkladba(id_album, id_skladba, cislo_stopy)
        self.seznam_album_skladba.append(album_skladba)
        file = open('album_skladba', 'wb')
        pickle.dump(self.seznam_album_skladba, file)


#vypis čísla stopy u skladeb v albech
    def vypis_cisla_stopy(self):
        print('ID album_skladba\tČíslo stopy\n')
        file = open('album_skladba', 'rb')
        data = pickle.load(file)
        for item in data:
            print(f"{item.id}\t{item.cislo_stopy}")

# funkce pro přidání národnosti
    def pridej_narodnost(self, nazev):
        narodnost = Narodnost(nazev)
        print(narodnost.id)
        self.seznam_narodnost.append(narodnost)
        file = open('narodnost', 'wb')
        pickle.dump(self.seznam_narodnost, file)

#funkce pro vypsání národností
    def vypis_narodnost(self):
        print('ID Národnost\tNárodnost\n')
        file = open('narodnost', 'rb')
        data = pickle.load(file)
        for item in data:
            print(f"{item.id}\t{item.nazev}")

# funkce pro přidání interpreta
    def pridej_interpreta(self, id_narodnost, nazev):
        interpret = Interpret(id_narodnost, nazev)
        self.seznam_interpret.append(interpret)
        file = open('interpret', 'wb')
        pickle.dump(self.seznam_interpret, file)

#funkce pro vypsání národností
    def vypis_interpreta(self):
        print('id_iterpreta\tnázev\n')
        file = open('interpret', 'rb')
        data = pickle.load(file)
        for item in data:
            print(f"{item.id}\t{item.nazev}")

# funkce pro přidání interpreta
    def pridej_album_interpret(self, id_album, id_interpret):
        album_interpret = AlbumInterpret(id_album, id_interpret)
        self.seznam_album_interpret.append(album_interpret)
        file = open('album_interpret', 'wb')
        pickle.dump(self.seznam_album_interpret, file)

#funkce pro vypsání národností
    def vypis_album_interpret(self):
        print('id_album_interpret\tid_interpret\n')
        file = open('album_interpret', 'rb')
        data = pickle.load(file)
        for item in data:
            print(f"{item.id}\t{item.id_interpret}")





