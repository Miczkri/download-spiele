import os
import re

# Ścieżka do folderu z Twoimi postami .mdx
# Jeśli skrypt jest w tym samym folderze, zostaw '.'
DIRECTORY = '.' 

# Wyrażenie regularne do znalezienia linku YouTube i wyciągnięcia ID
# Obsługuje formaty: youtube.com/watch?v=ID oraz youtu.be/ID
YT_REGEX = r'https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)(?:&\S*)?'

def transform_mdx_files():
    if not os.path.exists(DIRECTORY):
        print(f"Błąd: Katalog {DIRECTORY} nie istnieje.")
        return

    count = 0
    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".mdx"):
            filepath = os.path.join(DIRECTORY, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Szukamy linków i zamieniamy na tag Astro
            # \1 odnosi się do pierwszej grupy w regex (czyli video_id)
            new_content = re.sub(YT_REGEX, r'<Youtube id="\1" client:visible/>', content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Zaktualizowano: {filename}")
                count += 1

    print(f"\nGotowe! Zaktualizowano plików: {count}")

if __name__ == "__main__":
    transform_mdx_files()