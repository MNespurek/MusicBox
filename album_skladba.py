class AlbumSkladba:

# statická proměnná pro ukládání posledního ID    
    posledni_id = 0

# posun ID o 1
    @staticmethod
    def vytvor_id():
        AlbumSkladba.posledni_id += 1
        return AlbumSkladba.posledni_id


# volaná funkce při vytváření objektu    
    def __init__(self, id_album, id_skladba, cislo_stopy):
        self.id_album = id_album
        self.id_skladba = id_skladba        
        self.cislo_stopy = cislo_stopy
        self.id = AlbumSkladba.vytvor_id()


