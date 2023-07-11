class Zanr:

# list pro ukládání žánrů
    seznam_zanru = []
# statická proměnná pro ukládání posledního ID
    posledni_id = 0

# posun ID o 1
    @staticmethod
    def vytvor_id():
        Zanr.posledni_id +=1
        return Zanr.posledni_id

# volaná funkce při vytváření objektu
    def __init__(self, nazev):
        self.nazev = nazev
        self.id = Zanr.vytvor_id()



