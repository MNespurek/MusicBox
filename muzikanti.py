import pickle
from typ_zanr import Zanr
from album import Album
from skladba import Skladba
from album_skladba import AlbumSkladba
from interpret import Interpret
from typ_narodnost import Narodnost
from typ_narodnost import Narodnost
from album_interpret import AlbumInterpret


class Muzikanti:
    seznam_zanru = []
    seznam_alb = []
    seznam_album_skladba = []
    seznam_skladeb = []
    seznam_album_interpret = []
    seznam_interpret = []
    seznam_narodnost = []
    
    seznamy = {
        'seznam_zanru' : seznam_zanru,
        'seznam_alb' : seznam_alb,
        'seznam_album_skladba' : seznam_album_skladba,
        'seznam_skladeb' : seznam_skladeb,
        'seznam_album_interpret' : seznam_album_interpret,
        'seznam_interpret' : seznam_interpret,
        'seznam_narodnost' : seznam_narodnost,
    }

    with open('seznamy.pickle', 'wb') as file:
        pickle.dump(seznamy, file)


# funkce pro přidání žánru
    def pridej_zanr(self, pridej_tz):
        zanr = Zanr(pridej_tz)
        self.seznam_zanru.append(zanr)
        self.seznamy['seznam_zanru'] = zanr
        return self.seznam_zanru

# vypiš žánry ze seznamu    
    def vypis_zanr(self):
        zanr_text = ""
        for zanr in self.seznam_zanru:
            zanr_text += f"{zanr.id}\t {zanr.nazev}\n"
        return zanr_text

# funkce pro přidání alba
    def pridej_album(self, id_typ_zanr, nazev, datum_vydani):
        album = Album(nazev, id_typ_zanr, datum_vydani)
        self.seznam_alb.append(album)
        self.seznamy['seznam_alb'] = album
        return self.seznam_alb

# vypis všech alb
    def vypis_alb(self):
        album_text = ""
        for album in self.seznam_alb:
            album_text += f"{album.id}\t {album.nazev}\t {album.datum_vydani}\n"
        return album_text
    
# funkce pro přidání skladby
    def pridej_skladbu(self, nazev, delka):
        skladba = Skladba(nazev, delka)
        self.seznamy['seznam_skladeb'] = skladba
        self.seznam_skladeb.append(skladba)
        return self.seznam_skladeb
    
# výpis všech skladeb
    def vypis_skladby(self):
        print("Id_skladba\tNázev\tDélka\n")
        skladby_text = ""
        for skladba in self.seznam_skladeb:
            skladby_text += f"{skladba.id}\t{skladba.nazev}\t{skladba.delka}\n"

# funkce pro přidání album skladeb
    def pridej_album_skladba(self, id_album, id_skladba, cislo_stopy):
        album_skladba = AlbumSkladba(id_album, id_skladba, cislo_stopy)
        self.seznam_album_skladba.append(album_skladba)
        self.seznamy['seznam_album_skladba'] = album_skladba

#vypis čísla stopy u skladeb v albech
    def vypis_cisla_stopy(self):
        print("id_album skladba\tčíslo stopy\n")
        cislo_stopy = ""
        for album_skladba in self.seznam_album_skladba:
            cislo_stopy += f"{album_skladba.id}\t {album_skladba.cislo_stopy}\n"

# funkce pro přidání národnosti
    def pridej_narodnost(self, nazev):
        narodnost = Narodnost(nazev)
        self.seznam_narodnost.append(narodnost)
        self.seznamy['seznam_narodnost'] = narodnost

#funkce pro vypsání národností
    def vypis_narodnost(self):
        print('id_narodnost\tnázev\n')
        narodnosti = ""
        for narodnost in self.seznam_narodnost:
            narodnost += f"{narodnost.id}\t{narodnost.nazev}\n"
        return narodnosti

# funkce pro přidání interpreta
    def pridej_interpreta(self, id_narodnost, nazev):
        interpret = Interpret(id_narodnost, nazev)
        self.seznam_narodnost.append(interpret)
        self.seznamy['seznam_narodnost'] = interpret

#funkce pro vypsání národností
    def vypis_narodnost(self):
        print('id_narodnost\tnázev\n')
        interpreti = ""
        for interpret in self.seznam_interpret:
            interpreti += f"{interpret.id}\t{interpret.nazev}\n"
        return interpreti

# funkce pro přidání interpreta
    def pridej_album_interpret(self, id_album, id_interpret):
        album_interpret = AlbumInterpret(id_album, id_interpret)
        self.seznam_album_interpret.append(album_interpret)
        self.seznamy['seznam_album_interpret'] = album_interpret

#funkce pro vypsání národností
    def vypis_album_interpret(self):
        print('id_album_interpret\tid_interpret\n')
        album_interpreti = ""
        for album_interpret in self.seznam_album_interpret:
            album_interpreti += f"{album_interpret.id}\t{album_interpret.id_interpret}\n"
        return album_interpreti


