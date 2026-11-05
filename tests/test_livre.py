
import pytest

from bibliotheque.livre import Livre


def test_creation_livre():
    livre = Livre(
        "978-2-07-040850-4",
        "Le Petit Prince",
        "Antoine de Saint-Exupéry"
    )

    assert livre.titre == "Le Petit Prince"
    assert livre.auteur == "Antoine de Saint-Exupéry"
    assert livre.disponible is True


def test_emprunter_livre():
    livre = Livre("123", "Test", "Auteur")

    livre.emprunter()

    assert livre.disponible is False


def test_emprunter_livre_deja_emprunte():
    livre = Livre("123", "Test", "Auteur")

    livre.emprunter()

    with pytest.raises(ValueError):
        livre.emprunter()


def test_rendre_livre():
    livre = Livre("123", "Test", "Auteur")

    livre.emprunter()
    livre.rendre()

    assert livre.disponible is True
