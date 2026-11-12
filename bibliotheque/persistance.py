import json
from bibliotheque.catalogue import Bibliotheque
from bibliotheque.livre import Livre


def sauvegarder_json(biblio, chemin):
    """Écrit le catalogue dans un fichier JSON."""
    donnees = [
        {
            "isbn": l.isbn,
            "titre": l.titre,
            "auteur": l.auteur,
            "disponible": l.disponible
        }
        for l in biblio.livres
    ]

    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)


def charger_json(chemin):
    """Relit un catalogue depuis un fichier JSON."""
    biblio = Bibliotheque()

    with open(chemin, encoding="utf-8") as f:
        for d in json.load(f):
            livre = Livre(d["isbn"], d["titre"], d["auteur"])
            livre.disponible = d["disponible"]
            biblio.ajouter(livre)

    return biblio