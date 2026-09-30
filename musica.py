class Brano:
    def __init__(self, titolo, autore, durata):
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    def get_titolo(self):
        return self.titolo

    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_autore(self):
        return self.autore

    def set_autore(self, autore):
        self.autore = autore

    def get_durata(self):
        return self.durata

    def set_durata(self, durata):
        if not isinstance(durata, (int, float)) or isinstance(durata, bool) or durata < 0:
            raise ValueError("La durata deve essere un numero non negativo di secondi.")
        self.durata = durata

    def shortSong(self):
        """Restituisce True se il brano dura al massimo tre minuti."""
        return self.durata <= 180

    def __str__(self):
        minuti, secondi = divmod(int(self.durata), 60)
        return f"{self.titolo} - {self.autore} ({minuti}:{secondi:02d})"


class CD:
    def __init__(self, titolo, autore, brani=None):
        self.titolo = titolo
        self.autore = autore
        self.brani = list(brani) if brani is not None else []

    def aggiungi_brano(self, brano):
        if not isinstance(brano, Brano):
            raise TypeError("È possibile aggiungere solo oggetti Brano.")
        self.brani.append(brano)

    def rimuovi_brano(self, titolo):
        for brano in self.brani:
            if brano.titolo == titolo:
                self.brani.remove(brano)
                return True
        return False

    def durata_complessiva(self):
        return sum(brano.durata for brano in self.brani)

    def __str__(self):
        durata = int(self.durata_complessiva())
        minuti, secondi = divmod(durata, 60)
        elenco = "\n".join(
            f"  {indice}. {brano}" for indice, brano in enumerate(self.brani, start=1)
        )
        if not elenco:
            elenco = "  (nessun brano)"
        return (
            f"CD: {self.titolo}\nAutore: {self.autore}\n"
            f"Durata complessiva: {minuti}:{secondi:02d}\nBrani:\n{elenco}"
        )


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.brani = []

    def aggiungi_brano(self, brano):
        if not isinstance(brano, Brano):
            raise TypeError("È possibile aggiungere solo oggetti Brano.")
        self.brani.append(brano)

    def durata_complessiva(self):
        return sum(brano.durata for brano in self.brani)

    def cerca_brano(self, titolo):
        return [brano for brano in self.brani if titolo.lower() in brano.titolo.lower()]

    def __str__(self):
        elenco = "\n".join(f"  - {brano}" for brano in self.brani)
        if not elenco:
            elenco = "  (playlist vuota)"
        return f"Playlist: {self.nome}\n{elenco}"


class ArchivioMusicale:
    def __init__(self):
        self.cd = []

    def aggiungi_cd(self, cd):
        if not isinstance(cd, CD):
            raise TypeError("È possibile archiviare solo oggetti CD.")
        self.cd.append(cd)

    def cerca_cd(self, titolo):
        return [cd for cd in self.cd if titolo.lower() in cd.titolo.lower()]

    def __str__(self):
        if not self.cd:
            return "Archivio musicale vuoto."
        return "Archivio musicale:\n" + "\n".join(
            f"  - {cd.titolo} ({cd.autore})" for cd in self.cd
        )


if __name__ == "__main__":
    primo = Brano("La sera", "Ada Rossi", 172)
    secondo = Brano("Strade", "Luca Bianchi", 215)

    cd = CD("Due canzoni", "Ada Rossi")
    cd.aggiungi_brano(primo)
    cd.aggiungi_brano(secondo)
    print(cd)
    print(f"\n'{primo.titolo}' è un brano breve: {primo.shortSong()}")

    playlist = Playlist("Preferiti")
    playlist.aggiungi_brano(primo)
    print(f"\n{playlist}")

    archivio = ArchivioMusicale()
    archivio.aggiungi_cd(cd)
    print(f"\n{archivio}")