
class Bibliotheque:
    """Catalogue de livres."""

    def __init__(self):
        self._livres = []

    def ajouter(self, livre):
        self._livres.append(livre)

    def rechercher_par_isbn(self, isbn):
        for livre in self._livres:
            if livre.isbn == isbn:
                return livre
        return None

    def rechercher_par_auteur(self, auteur):
        return [
            livre for livre in self._livres
            if livre.auteur.lower() == auteur.lower()
        ]

    @property
    def livres(self):
        return list(self._livres)

    def __len__(self):
        return len(self._livres)

    def rechercher_par_titre(self, mot):
        mot = mot.lower()
        return [
            l for l in self._livres
            if mot in l.titre.lower()
        ]

    def nombre_disponibles(self):
        return sum(1 for l in self._livres if l.disponible)

    def trier_par_titre(self, inverse=False):
        return sorted(
            self._livres,
            key=lambda l: l.titre,
            reverse=inverse
        )

    def supprimer(self, isbn):
        """Supprime le livre d'ISBN donné. Retourne True si un livre a été supprimé."""
        livre = self.rechercher_par_isbn(isbn)

        if livre is None:
            return False

        self._livres.remove(livre)
        return True
