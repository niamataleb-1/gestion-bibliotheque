class Livre:
    """Un livre du catalogue."""

    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre} ({self.auteur})"
