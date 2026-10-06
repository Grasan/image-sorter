from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS


# Hämta datum från bildens EXIF-information
def get_photo_date(file):
    image = Image.open(file)
    exif = image.getexif()

    # Försök hitta datum i EXIF
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)

        if tag == "DateTimeOriginal":
            return datetime.strptime(
                value,
                "%Y:%m:%d %H:%M:%S"
            )

        if tag == "DateTime":
            return datetime.strptime(
                value,
                "%Y:%m:%d %H:%M:%S"
            )

    # Försök hitta datum i XMP
    xmp = image.getxmp()

    descriptions = (
        xmp
        .get("xmpmeta", {})
        .get("RDF", {})
        .get("Description", [])
    )

    if isinstance(descriptions, dict):
        descriptions = [descriptions]

    for description in descriptions:

        date_acquired = description.get("DateAcquired")

        if date_acquired:
            return datetime.fromisoformat(
                date_acquired
            )

    return None


# Hämta datum från filens ändringsdatum
def get_video_date(file):
    timestamp = file.stat().st_mtime

    return datetime.fromtimestamp(timestamp)