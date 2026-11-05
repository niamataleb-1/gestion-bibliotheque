import csv


def exporter_csv(biblio, chemin):
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["isbn", "titre", "auteur", "disponible"])

        for livre in biblio.livres:
            writer.writerow([
                livre.isbn,
                livre.titre,
                livre.auteur,
                livre.disponible
            ])