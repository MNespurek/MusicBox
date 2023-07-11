class Interpret:

# statická proměnná pro ukládání posledního ID
    posledni_id = 0

# posun ID o 1
    @staticmethod
    def vytvor_id():
        Interpret.posledni_id += 1
        return Interpret.posledni_id

# volaná funkce při vytváření objektu
    def __init__(self, id_narodnost, nazev):
        self.id_narodnost = id_narodnost
        self.nazev = nazev
        self.id = Interpret.vytvor_id()


