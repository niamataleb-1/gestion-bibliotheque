from bibliotheque.catalogue import Bibliotheque
from bibliotheque.livre import Livre


def main():
    biblio = Bibliotheque()

    biblio.ajouter(
        Livre(
            "978-2-07-040850-4",
            "Le Petit Prince",
            "Antoine de Saint-Exupéry"
        )
    )

    biblio.ajouter(
        Livre("978-2-07-036002-4", "L'Étranger", "Albert Camus")
    )
    biblio.ajouter(
        Livre("978-2-07-036822-8", "La Peste", "Albert Camus")
    )

    print("=== Bibliothèque ===")
    for livre in biblio.livres:
        print(f" - {livre}")

    livre = biblio.rechercher_par_isbn("978-2-07-036822-8")
    if livre is not None:
        livre.emprunter()

    print("Livres d'Albert Camus :")
    for livre in biblio.rechercher_par_auteur("Albert Camus"):
        print(f" - {livre}")


if __name__ == "__main__":
    main()
    print("Recherche « peste » :")
    for livre in biblio.rechercher_par_titre("peste"):
        print(f" - {livre}")