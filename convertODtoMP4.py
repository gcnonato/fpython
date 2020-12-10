# -*- coding: utf-8 -*-
import os


def _join_vods(directory, file_paths, target):
    input_path = "/".join((f"{directory}", "files.txt"))
    print(input_path)
    with open(input_path, "w") as f:
        for path in file_paths:
            f.write(f"file {os.path.basename(path)}\n")


def path_to_desktop():
    homepath = os.path.expanduser(os.getenv("USERPROFILE"))
    desktoppath = "Desktop"
    return os.path.join(homepath, desktoppath, "vod")


if __name__ == "__main__":
    target_dir = path_to_desktop()
    target = ""
    file_paths = path_to_desktop()
    _join_vods(target_dir, file_paths, target)
