
import csv
import json

from bibliotheque.catalogue import Bibliotheque
from bibliotheque.livre import Livre
from bibliotheque.export import exporter_csv, exporter_json


def creer_bibliotheque():
    biblio = Bibliotheque()

    biblio.ajouter(
        Livre("111", "Le Petit Prince", "Saint-Exupéry")
    )
    biblio.ajouter(
        Livre("222", "L'Étranger", "Albert Camus")
    )

    return biblio


def test_exporter_csv(tmp_path):
    biblio = creer_bibliotheque()
    chemin = tmp_path / "livres.csv"

    exporter_csv(biblio, chemin)

    with open(chemin, encoding="utf-8") as fichier:
        lignes = list(csv.reader(fichier))

    assert lignes[0] == ["isbn", "titre", "auteur", "disponible"]
    assert len(lignes) == 3
    assert lignes[1][1] == "Le Petit Prince"


def test_exporter_json(tmp_path):
    biblio = creer_bibliotheque()
    chemin = tmp_path / "livres.json"

    exporter_json(biblio, chemin)

    with open(chemin, encoding="utf-8") as fichier:
        livres = json.load(fichier)

    assert len(livres) == 2
    assert livres[0]["titre"] == "Le Petit Prince"
    assert livres[1]["auteur"] == "Albert Camus"
    assert livres[0]["disponible"] is True
