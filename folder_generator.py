import os
import shutil


def generate_folders_under_dir(folders, directory):
    for folder in folders:
        path = os.path.join(directory, folder)
        os.makedirs(path, exist_ok=True)


def copy_file_to_dirs(src_file, dirs):
    for directory in dirs:
        shutil.copy2(src_file, directory)