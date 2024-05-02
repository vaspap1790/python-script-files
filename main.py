import os

from config import DIRECTORIES, PROJECT_DIR, FILES_TO_COPY_DIR
from folder_generator import generate_folders_under_dir, copy_file_to_dirs


def main():
    generate_folders_under_dir(DIRECTORIES, PROJECT_DIR)

    src_file = FILES_TO_COPY_DIR + "/alertmanager.yml"
    dirs = [os.path.join(PROJECT_DIR, dir) for dir in DIRECTORIES]
    copy_file_to_dirs(src_file, dirs)


if __name__ == "__main__":
    main()