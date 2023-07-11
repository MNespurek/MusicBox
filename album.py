
class Album:

# statická proměnná pro ukládání posledního ID    
    posledni_id = 0

# posun ID o 1
    @staticmethod
    def vytvor_id():
        Album.posledni_id += 1
        return Album.posledni_id

# volaná funkce při vytváření objektu    
    def __init__(self, id_typ_zanr, nazev, datum_vydani):
        self.id_typ_zanr = id_typ_zanr
        self.nazev = nazev
        self.datum_vydani = datum_vydani
        self.id = Album.vytvor_id()

