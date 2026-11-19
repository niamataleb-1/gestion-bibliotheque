
from bibliotheque.catalogue import Bibliotheque
from bibliotheque.livre import Livre
from bibliotheque.persistance import sauvegarder_json, charger_json


def test_sauvegarder_et_charger_json(tmp_path):
    biblio = Bibliotheque()
    livre = Livre("123456", "Python debutant", "Ali")
    biblio.ajouter(livre)

    chemin = tmp_path / "catalogue.json"

    sauvegarder_json(biblio, chemin)
    biblio_chargee = charger_json(chemin)

    assert len(biblio_chargee) == 1
    assert biblio_chargee.livres[0].isbn == "123456"
    assert biblio_chargee.livres[0].titre == "Python debutant"


def test_conserver_disponibilite(tmp_path):
    biblio = Bibliotheque()
    livre = Livre("789456", "Python avance", "Sara")
    biblio.ajouter(livre)
    livre.emprunter()

    chemin = tmp_path / "catalogue.json"

    sauvegarder_json(biblio, chemin)
    biblio_chargee = charger_json(chemin)

    assert biblio_chargee.livres[0].disponible is False
