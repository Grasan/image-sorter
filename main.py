from pathlib import Path
import argparse

from config import IMAGE_EXTENSIONS, VIDEO_EXTENSIONS, MONTH_NAMES
from file_handler import get_unique_destination, move_file
from metadata import get_video_date, get_photo_date
from sorter import get_folder_name

parser = argparse.ArgumentParser(
    description="Sort images and videos in years and months."
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Show what will happen without moving any images."
)

parser.add_argument(
    "--include-video",
    action="store_true",
    help="Include videofiles in the sorting."
)

args = parser.parse_args()


current_folder = Path.cwd()

for file in current_folder.iterdir():

    is_image = (
        file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
    )

    is_video = (
        file.is_file()
        and file.suffix.lower() in VIDEO_EXTENSIONS
    )

    if not is_image and not (is_video and args.include_video):
        continue

    if is_image:
        date = get_photo_date(file)
    else:
        date = get_video_date(file)

    if date is None:
        print(f"{file.name} -> No date found")
        continue

    folder_name = get_folder_name(date)

    destination_folder = current_folder / folder_name

    if not args.dry_run:
        destination_folder.mkdir(exist_ok=True) 

    destination = destination_folder / file.name
    destination = get_unique_destination(destination)

    print(f"{file.name} -> {destination}")

    if not args.dry_run:
        move_file(file, destination)