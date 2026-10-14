from pathlib import Path
import argparse

from PIL import Image
from PIL.ExifTags import TAGS

from config import IMAGE_EXTENSIONS

parser = argparse.ArgumentParser(
    description="Inspect metadata from images."
)

parser.add_argument(
    "--log-file",
    type=Path,
    help="Save all image data in a log text file."
)

args = parser.parse_args()

current_folder = Path.cwd()

def output(message):
    if args.log_file:
        with args.log_file.open("a", encoding="utf-8") as log:
            log.write(str(message) + "\n")
    else:
        print(message)


for file in current_folder.iterdir():
    if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:
        image = Image.open(file)

        output("\n" + "=" * 60)
        output(file.name)
        output("=" * 60)

        # Visa EXIF-information
        output("\n--- EXIF ---")
        
        exif = image.getexif()

        if exif:
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)

                output(
                    f"ID: {tag_id} | "
                    f"Tagg: {tag} | "
                    f"Typ: {type(value).__name__}"
                )
                output(f"Value: {value}")
        else:
            output("No Exif-info found.")

        # Visa XMP-information
        output("\n--- XMP ---")

        xmp = image.getxmp()


        
        if xmp:
            output(xmp)
        else:
            output("No XMP-info found.")

        # Visa filens ändringsdatum
        output("\n--- FILEDATE ---")
        output(f"File editdate: {file.stat().st_mtime}")