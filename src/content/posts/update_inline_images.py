import os
import re

# Ścieżka do folderu z Twoimi postami .mdx
DIRECTORY = '.' 

# Nowy regex: 
# Szuka: ![](https://download-spiele.com/wp-content/uploads/ROK/MIESIAC/nazwa-pliku.rozszerzenie)
# \d{4}/\d{2}/ radzi sobie z dowolną datą (np. 2024/12, 2025/01 itd.)
INLINE_IMAGE_REGEX = r'!\[(.*?)\]\(https://download-spiele\.com/wp-content/uploads/\d{4}/\d{2}/([^)]+)\)'

def update_inline_images():
    if not os.path.exists(DIRECTORY):
        print(f"Błąd: Katalog {DIRECTORY} nie istnieje.")
        return

    count = 0
    new_base_url = "https://img.download-spiele.com/"

    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".mdx"):
            filepath = os.path.join(DIRECTORY, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Zamieniamy stary URL na nowy
            # \1 to alt text (tekst w kwadratowych nawiasach)
            # \2 to sama nazwa pliku (np. Builders-of-Egypt1.webp)
            replacement = f'![\\1]({new_base_url}\\2)'
            new_content = re.sub(INLINE_IMAGE_REGEX, replacement, content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Zaktualizowano obrazki w treści: {filename}")
                count += 1

    print(f"\nGotowe! Zaktualizowano obrazki w {count} plikach.")

if __name__ == "__main__":
    update_inline_images()