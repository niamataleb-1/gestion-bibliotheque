
from bibliotheque.catalogue import Bibliotheque
from bibliotheque.livre import Livre


def creer_bibliotheque():
    biblio = Bibliotheque()

    biblio.ajouter(Livre("111", "Le Petit Prince", "Saint-Exupéry"))
    biblio.ajouter(Livre("222", "L'Étranger", "Albert Camus"))
    biblio.ajouter(Livre("333", "La Peste", "Albert Camus"))

    return biblio


def test_ajouter_livre():
    biblio = creer_bibliotheque()
    assert len(biblio.livres) == 3


def test_rechercher_par_isbn():
    biblio = creer_bibliotheque()
    livre = biblio.rechercher_par_isbn("222")

    assert livre is not None
    assert livre.titre == "L'Étranger"


def test_rechercher_par_auteur():
    biblio = creer_bibliotheque()
    livres = biblio.rechercher_par_auteur("Albert Camus")

    assert len(livres) == 2


def test_rechercher_par_titre():
    biblio = creer_bibliotheque()
    livres = biblio.rechercher_par_titre("peste")

    assert len(livres) == 1
    assert livres[0].titre == "La Peste"
