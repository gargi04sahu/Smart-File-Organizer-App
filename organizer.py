import os
import shutil
from datetime import datetime

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Documents/PDFs": [".pdf"],
    "Documents/Word Files": [".doc", ".docx"],
    "Documents/Excel Files": [".xls", ".xlsx"],
    "Documents/PPT Files": [".ppt", ".pptx"],
    "Text Files": [".txt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Apps & Installers": [".exe", ".msi"]
}

last_moved_files = []  # stores tuples of (src, dest)


def get_file_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def get_preview_list():
    files = os.listdir(DOWNLOADS_FOLDER)
    preview = {}

    for file in files:
        file_path = os.path.join(DOWNLOADS_FOLDER, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            category = get_file_category(ext)
            preview.setdefault(category, []).append(file)

    return preview


def organize_downloads(folder_path):
    global last_moved_files
    last_moved_files = []
    moved_count = 0
    folder_count = set()

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            category = get_file_category(ext)

            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            new_file_path = os.path.join(category_folder, file)

            try:
                shutil.move(file_path, new_file_path)
                last_moved_files.append((new_file_path, file_path))
                moved_count += 1
                folder_count.add(category)
            except Exception as e:
                print(f"Error moving {file}: {e}")

    return moved_count, len(folder_count)
