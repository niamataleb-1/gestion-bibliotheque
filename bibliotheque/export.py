
import csv
import json


def exporter_csv(biblio, chemin):
    with open(chemin, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["isbn", "titre", "auteur", "disponible"])

        for livre in biblio.livres:
            writer.writerow([
                livre.isbn,
                livre.titre,
                livre.auteur,
                livre.disponible
            ])


def exporter_json(biblio, chemin):
    livres = []

    for livre in biblio.livres:
        livres.append({
            "isbn": livre.isbn,
            "titre": livre.titre,
            "auteur": livre.auteur,
            "disponible": livre.disponible
        })

    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(livres, fichier, ensure_ascii=False, indent=4)
