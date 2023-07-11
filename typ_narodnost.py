class Narodnost:

# statická proměnná pro ukládání posledního ID    
    posledni_id = 0

# posun ID o 1
    @staticmethod
    def vytvor_id():
        Narodnost.posledni_id =+ 1
        return Narodnost.posledni_id

# volaná funkce při vytváření objektu
    def __init__(self, nazev):
        self.nazev = nazev
        self.id = Narodnost.vytvor_id()

