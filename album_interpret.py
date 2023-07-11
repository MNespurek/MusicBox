class AlbumInterpret:

# statická proměnná pro ukládání posledního ID
    posledni_id = 0

# posun ID o 1
    @staticmethod
    def vytvor_id():
        AlbumInterpret.posledni_id += 1
        return AlbumInterpret.posledni_id

# volaná funkce při vytváření objektu
    def __init__(self, id_album, id_interpret):
        self.id_album = id_album
        self.id_interpret = id_interpret
        self.id = AlbumInterpret.vytvor_id()
