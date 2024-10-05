import os
import shutil
import sys

UNKNOWN_EXTENSION = 'none_extension'
ds = os.sep


def copy_files(dir_from: str, destination_dir: str):
    for item in os.listdir(dir_from):
        if os.path.isdir(os.path.join(dir_from, item)):
            copy_files("".join([dir_from, os.sep, item]), destination_dir)
        else:
            file_name, extension_real = os.path.splitext(item)
            extension = UNKNOWN_EXTENSION if len(extension_real) in [0, 1] else extension_real[1:]

            copy_from = "".join([dir_from, ds, item])
            dir_copy_to = "".join([destination_dir, ds, extension])

            if not os.path.exists(dir_copy_to):
                os.makedirs(dir_copy_to)

            file_copy_to = "".join([dir_copy_to, ds, file_name, '.', extension])

            if os.path.exists(file_copy_to):
                # TODO: need to cover this case by business logic
                print(f"File '{item}' already exists and will be replaced")

            try:
                shutil.copy(copy_from, file_copy_to)
            except PermissionError:
                print(f"Failed to copy file {item}. Permission denied")


if __name__ == '__main__':
    arguments = sys.argv
    path_from = arguments[1] if len(arguments) > 1 else "directory_copy_from"
    path_to = arguments[2] if len(arguments) > 2 else "dist"

    copy_files(path_from, path_to)
