import json

# Dictionnaire des dossiers et plages de fichiers
data = {
    "english": {"folder": "/hymne/hymne-english/xml-hymne-english", "prefix": "E", "range": 698},
    "francais": {"folder": "/hymne/hymne-francais/xml-hymne-francais", "prefix": "H", "range": 654},
    "spanish": {"folder": "/hymne/hymne-spanish/xml-hymne-spanish", "prefix": "S", "range": 613},
}

# Liste pour stocker les chemins
xml_paths = []

# Génération des chemins
for lang, info in data.items():
    folder = info["folder"]
    prefix = info["prefix"]
    for i in range(1, info["range"] + 1):
        filename = f"{prefix}{str(i).zfill(3)}.xml"
        xml_paths.append(f"{folder}/{filename}")

# Écriture dans un fichier JSON
with open("xml-files.json", "w", encoding="utf-8") as json_file:
    json.dump(xml_paths, json_file, indent=2)

print("Fichier xml-files.json généré avec succès !")
