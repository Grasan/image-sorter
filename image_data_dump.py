from pathlib import Path

from PIL import Image
from PIL.ExifTags import TAGS

from config import IMAGE_EXTENSIONS

current_folder = Path.cwd()

for file in current_folder.iterdir():

    if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:
        image = Image.open(file)

        print("\n" + "=" * 60)
        print(file.name)
        print("=" * 60)

        # Visa EXIF-information
        print("\n--- EXIF ---")
        
        exif = image.getexif()

        if exif:
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)

                print(
                    f"ID: {tag_id} | "
                    f"Tagg: {tag} | "
                    f"Typ: {type(value).__name__}"
                )
                print(f"Värde: {value}")
        else:
            print("No Exif-info found.")

        # Visa XMP-information
        print("\n--- XMP ---")

        xmp = image.getxmp()

        if xmp:
            print(xmp)
        else:
            print("No XMP-info found.")

        # Visa filens ändringsdatum
        print("\n--- FILEDATE ---")
        print(f"File editdate: {file.stat().st_mtime}")