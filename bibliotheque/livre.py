class Livre:
    """Un livre du catalogue."""

    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if not self.disponible:
            raise ValueError(f"Livre déjà emprunté : {self.titre}")
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def __str__(self):
        statut = "disponible" if self.disponible else "emprunté"
        return f"{self.titre} ({self.auteur}) - {statut}"
