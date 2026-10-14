import shutil

# If a file with a similar name appears in the destination folder. 
# Edit file name.
def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem} "
            f"({counter})"
            f"{destination.suffix}"
        )

        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1

def move_file(file, destination):
    shutil.move(file, destination)