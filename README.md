# image-sorter

A CLI tool for organizing large photo collections by sorting images into folders based on the year and month found in their metadata.

## Features

- Sorts images into folders named after their year and month.
- Supports multiple image formats.
- Uses EXIF and XMP metadata to determine image dates.
- Handles files with identical names by generating unique filenames.
- Supports optional video sorting.
- Includes a dry-run mode to preview changes before moving files.

## Dependencies

This tool requires Python 3 and the following packages:

- [Pillow](https://pypi.org/project/Pillow/)
- [defusedxml](https://pypi.org/project/defusedxml/) (required for reading XMP metadata through Pillow)

### Installation

Install the required packages using:

```bash
python3 -m pip install Pillow defusedxml
```

To verify that Pillow was installed correctly, run:

```bash
python3 -c "from PIL import Image; print('Pillow works!')"
```

## Usage

First, navigate to the folder containing the images you want to organize.

An easy way to do this is to open the folder using your operating system's file explorer, right-click inside the folder, and select **Open in Terminal**.

Run the script using:

```bash
python3 /path/to/image-sorter/main.py
```

The program will scan the files in the current directory and attempt to determine their dates using available metadata.

Files with a recognized date will be moved into folders named after their year and month. Files without a usable date will be skipped.

### Example output

```text
2012-12 December/
    image001.jpg
    image002.jpg

2013-01 January/
    image003.jpg
```

## Optional flags

The program supports two optional flags.

### `--dry-run`

Preview what the program would do without moving any files or creating folders.

This is recommended before running the program for the first time.

```bash
python3 /path/to/image-sorter/main.py --dry-run
```

### `--include-video`

Include supported video files in the sorting process.

Videos are not included by default. Their dates are determined using the file's last modified timestamp.

```bash
python3 /path/to/image-sorter/main.py --include-video
```

You can also combine both flags:

```bash
python3 /path/to/image-sorter/main.py --include-video --dry-run
```

## Data dump

The project includes a separate script called `data_dump.py`.

This script prints metadata information from supported image files. It can be useful for troubleshooting images that are skipped during sorting or for investigating which metadata fields are available.

The output is printed directly in the terminal.

### Optional flag

The data dump script also supports an optional flag to save the output to a file instead of printing it in the terminal.

```bash
python3 /path/to/image-sorter/data_dump.py --log-file
```

Check the script's available arguments if you need additional information about its options.