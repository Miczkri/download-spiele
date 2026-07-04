import os
import re

# Ścieżka do folderu z Twoimi postami .mdx
DIRECTORY = '.' 

# Regex szukający konkretnych linków z tej domeny
# Wyłapuje linki zaczynające się od https://games-download.top/ i bierze wszystko do końca linii/spacji
GAMES_REGEX = r'(https://games-download\.top/[\w\-/]+)'

def transform_button_links():
    if not os.path.exists(DIRECTORY):
        print(f"Błąd: Katalog {DIRECTORY} nie istnieje.")
        return

    count = 0
    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".mdx"):
            filepath = os.path.join(DIRECTORY, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Zamiana linku na komponent Button
            # \1 wstawia cały dopasowany link w miejsce atrybutu link=""
            replacement = r'<Button label="Herunterladen" link="\1" style="outline" />'
            new_content = re.sub(GAMES_REGEX, replacement, content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Zaktualizowano: {filename}")
                count += 1

    print(f"\nGotowe! Zmieniono linki w {count} plikach.")

if __name__ == "__main__":
    transform_button_links()