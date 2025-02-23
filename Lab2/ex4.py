import re

regex_client = r"^Client:\s+[A-Z][a-z]+(\s[A-Z][a-z]+)+$"
regex_cnp = r"^CNP:\s+\d{13}$"
regex_produs = r"^Produs:\s+[\w\s]+,\s+Pret:\s+\d+\.\d{2},\s+Cantitate:\s+\d+,\s+TVA:\s+\d+%$"

def verifica_factura(nume_fisier):
    try:
        with open(nume_fisier, "r", encoding="utf-8") as file:
            linii = file.readlines()

        erori = []

        if not re.match(regex_client, linii[0].strip()):
            erori.append(f"Eroare format client: {linii[0].strip()}")

        if not re.match(regex_cnp, linii[1].strip()):
            erori.append(f"Eroare format CNP: {linii[1].strip()}")

        for i in range(2, len(linii)):
            if not re.match(regex_produs, linii[i].strip()):
                erori.append(f"Eroare format produs: {linii[i].strip()}")

        if erori:
            print("Factura nu respectă formatul. Erori găsite:")
            for eroare in erori:
                print(" -", eroare)
        else:
            print("Factura respectă formatul!")

    except FileNotFoundError:
        print("Fișierul nu a fost găsit!")

nume_fisier = "factura.txt"
verifica_factura(nume_fisier)
