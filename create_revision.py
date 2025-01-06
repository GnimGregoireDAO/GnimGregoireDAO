import csv

# Définir les données de révision
revision_plan = [
    {"Sujet": "Web 1", "Date": "2025-01-06", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-07", "Remarques": "9h00 - 12h00 : Méthodes de Conception (3h)"},
    {"Sujet": "Native 1", "Date": "2025-01-07", "Remarques": "14h00 - 16h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-08", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-09", "Remarques": "9h00 - 11h00 : Méthodes de Conception (2h)"},
    {"Sujet": "Native 1", "Date": "2025-01-09", "Remarques": "14h00 - 16h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-10", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-10", "Remarques": "14h00 - 16h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-11", "Remarques": "9h00 - 12h00 : Méthodes de Conception (3h)"},
    {"Sujet": "Native 1", "Date": "2025-01-11", "Remarques": "14h00 - 16h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-12", "Remarques": "13h00 - 15h00 : Web 1 (2h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-12", "Remarques": "15h00 - 17h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-13", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-13", "Remarques": "14h00 - 16h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-14", "Remarques": "9h00 - 12h00 : Méthodes de Conception (3h)"},
    {"Sujet": "Native 1", "Date": "2025-01-14", "Remarques": "14h00 - 16h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-15", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-15", "Remarques": "14h00 - 16h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-16", "Remarques": "9h00 - 12h00 : Méthodes de Conception (3h)"},
    {"Sujet": "Native 1", "Date": "2025-01-16", "Remarques": "14h00 - 16h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-17", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-17", "Remarques": "14h00 - 16h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-18", "Remarques": "9h00 - 11h00 : Méthodes de Conception (2h)"},
    {"Sujet": "Native 1", "Date": "2025-01-19", "Remarques": "9h00 - 11h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-20", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-20", "Remarques": "14h00 - 16h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-21", "Remarques": "9h00 - 12h00 : Méthodes de Conception (3h)"},
    {"Sujet": "Native 1", "Date": "2025-01-21", "Remarques": "14h00 - 16h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-22", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-22", "Remarques": "14h00 - 16h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-23", "Remarques": "9h00 - 12h00 : Méthodes de Conception (3h)"},
    {"Sujet": "Native 1", "Date": "2025-01-23", "Remarques": "14h00 - 16h00 : Native 1 (2h)"},
    {"Sujet": "Web 1", "Date": "2025-01-24", "Remarques": "9h00 - 12h00 : Web 1 (3h)"},
    {"Sujet": "Sécurité Informatique", "Date": "2025-01-24", "Remarques": "14h00 - 16h00 : Sécurité Informatique (2h)"},
    {"Sujet": "Méthodes de Conception", "Date": "2025-01-25", "Remarques": "9h00 - 11h00 : Méthodes de Conception (2h)"},
    {"Sujet": "Native 1", "Date": "2025-01-26", "Remarques": "13h00 - 16h00 : Native 1 (3h)"},
]

# Nom du fichier CSV
filename = "planning_revision.csv"

# Créer et écrire dans le fichier CSV
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ["Sujet", "Date", "Remarques"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in revision_plan:
        writer.writerow(row)

print(f"Planning de révision créé avec succès dans le fichier {filename}")