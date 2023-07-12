class Skladba:

# statická proměnná pro ukládání posledního ID
    posledni_id = 0

# posun ID o 1
    @staticmethod
    def vytvor_id():
        Skladba.posledni_id += 1
        return Skladba.posledni_id

# volaná funkce při vytváření objektu
    def __init__(self, nazev, delka):
        self.nazev = nazev
        self.delka = delka
        self.id = Skladba.vytvor_id()

