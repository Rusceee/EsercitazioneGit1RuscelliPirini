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


class Artista:
    def __init__(self, nome, genere):
        self.nome = nome
        self.genere = genere
        self.album_pubblicati = []

    def pubblica_cd(self, cd):
        if not isinstance(cd, CD):
            raise TypeError("Si possono associare solo oggetti di tipo CD.")
        self.album_pubblicati.append(cd)

    def numero_album(self):
        return len(self.album_pubblicati)

    def __str__(self):
        return f"Artista: {self.nome} | Genere: {self.genere} | Album pubblicati: {self.numero_album()}"


class EtichettaDiscografica:
    def __init__(self, nome_etichetta):
        self.nome_etichetta = nome_etichetta
        self.artisti = []

    def meggia_artista(self, artista):
        """Mette sotto contratto / aggiunge un artista all'etichetta."""
        if not isinstance(artista, Artista):
            raise TypeError("È possibile aggiungere solo oggetti Artista.")
        if artista not in self.artisti:
            self.artisti.append(artista)

    def elenco_artisti(self):
        if not self.artisti:
            return "Nessun artista sotto contratto."
        return "\n".join(f"  - {art.nome} ({art.genere})" for art in self.artisti)

    def __str__(self):
        return f"Etichetta: {self.nome_etichetta}\nArtisti sotto contratto:\n{self.elenco_artisti()}"


if __name__ == "__main__":
    print("=== TEST CLASSE BRANO ===")
    b1 = Brano("La sera", "Ada Rossi", 172)[cite: 1]
    b2 = Brano("Strade", "Luca Bianchi", 215)[cite: 1]
    b3 = Brano("Notte Stellata", "Ada Rossi", 150)
    
    print(b1)
    print(f"'{b1.titolo}' è breve (<= 3 min)? {b1.shortSong()}")  # True[cite: 1]
    print(f"'{b2.titolo}' è breve (<= 3 min)? {b2.shortSong()}")  # False
    print()

    print("=== TEST CLASSE CD ===")
    cd1 = CD("Due canzoni", "Ada Rossi")[cite: 1]
    cd1.aggiungi_brano(b1)[cite: 1]
    cd1.aggiungi_brano(b3)
    print(cd1)[cite: 1]
    
    # Test rimozione brano
    cd1.rimuovi_brano("La sera")[cite: 1]
    print("\nDopo la rimozione di 'La sera':")
    print(cd1)
    print()

    print("=== TEST CLASSE PLAYLIST ===")
    playlist = Playlist("Preferiti")[cite: 1]
    playlist.aggiungi_brano(b1)[cite: 1]
    playlist.aggiungi_brano(b2)
    print(playlist)[cite: 1]
    
    # Test ricerca nella playlist
    risultati_p = playlist.cerca_brano("Strade")[cite: 1]
    print(f"Brani trovati con il termine 'Strade': {len(risultati_p)}")
    print()

    print("=== TEST CLASSE ARCHIVIOMUSICALE ===")
    cd2 = CD("Viaggio", "Luca Bianchi")
    cd2.aggiungi_brano(b2)
    
    archivio = ArchivioMusicale()[cite: 1]
    archivio.aggiungi_cd(cd1)[cite: 1]
    archivio.aggiungi_cd(cd2)
    print(archivio)[cite: 1]
    
    # Test cerca CD nell'archivio
    trovati = archivio.cerca_cd("Due")[cite: 1]
    print(f"CD trovati con 'Due': {[cd.titolo for cd in trovati]}")
    print()

    print("=== TEST NUOVA CLASSE ARTISTA ===")
    artista1 = Artista("Ada Rossi", "Pop")
    artista1.pubblica_cd(cd1)
    print(artista1)
    print()

    print("=== TEST NUOVA CLASSE ETICHETTA DISCOGRAFICA ===")
    etichetta = EtichettaDiscografica("Sony Music")
    etichetta.meggia_artista(artista1)
    
    artista2 = Artista("Luca Bianchi", "Rock")
    etichetta.meggia_artista(artista2)
    
    print(etichetta)