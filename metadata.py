import re

from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS

def get_photo_date(file):
    image = Image.open(file)
    exif = image.getexif()

    exif_ifd = exif.get_ifd(34665)

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

    for tag_id, value in exif_ifd.items():
        tag = TAGS.get(tag_id, tag_id)

        if tag == "DateTimeOriginal":
            return datetime.strptime(
                value,
                "%Y:%m:%d %H:%M:%S"
            )

        if tag == "DateTimeDigitized":
            return datetime.strptime(
                value,
                "%Y:%m:%d %H:%M:%S"
            )

    match = re.search(r"(\d{13})(?=\.[^.]+$)", file.name)

    # If the file name and last modify date are the same 
    if match:
        timestamp = int(match.group(1)) / 1000

        modified_timestamp = file.stat().st_mtime

        difference = abs(timestamp - modified_timestamp)

        # Allow a maximum of two seconds differens
        # Or a one hour and two seconds for summer/winter time differense.
        if (
            difference <= 2
            or abs(difference - 3600) <= 2
        ):
            return datetime.fromtimestamp(timestamp)

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


# get date from the file's edit date.
def get_video_date(file):
    timestamp = file.stat().st_mtime

    return datetime.fromtimestamp(timestamp)