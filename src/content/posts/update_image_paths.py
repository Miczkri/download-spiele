import os
import re

# Ścieżka do folderu z Twoimi postami .mdx
DIRECTORY = '.' 

# Regex szuka ciągu: image: "nazwa-pliku.jpg"
# Grupa (.*?) wyłapuje samą nazwę pliku wewnątrz cudzysłowu
IMAGE_REGEX = r'image:\s*"([^"]+)"'

def update_image_urls():
    if not os.path.exists(DIRECTORY):
        print(f"Błąd: Katalog {DIRECTORY} nie istnieje.")
        return

    count = 0
    prefix = "https://img.download-spiele.com/"

    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".mdx"):
            filepath = os.path.join(DIRECTORY, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Sprawdzamy, czy link nie jest już zaktualizowany (żeby nie doklejać prefiksu dwa razy)
            # Zamieniamy na: image: "https://img.download-spiele.com/\1"
            # \1 to nazwa pliku przechwycona przez regex
            new_content = re.sub(IMAGE_REGEX, f'image: "{prefix}\\1"', content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Zaktualizowano obrazek w: {filename}")
                count += 1

    print(f"\nGotowe! Zaktualizowano ścieżki w {count} plikach.")

if __name__ == "__main__":
    update_image_urls()