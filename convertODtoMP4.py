import os
import subprocess


def _join_vods(directory, file_paths, target):
    # input_path = f"{directory}/files.txt"
    input_path = '/'.join((f"{directory}", 'files.txt'))
    print(input_path)

    # with open(input_path, encoding='utf8') as f:
    #     read_file = f.read()
    # print(read_file)
    with open(input_path, 'w') as f:
        for path in file_paths:
            f.write(f'file {os.path.basename(path)}\n')
    #
    # result = subprocess.run([
    #     "ffmpeg",
    #     "-f", "concat",
    #     "-i", input_path,
    #     "-c", "copy",
    #     target,
    #     "-stats",
    #     "-loglevel", "warning",
    # ])
    #
    # result.check_returncode()

def path_to_desktop():
    homepath = os.path.expanduser(os.getenv("USERPROFILE"))
    desktoppath = "Desktop"
    return os.path.join(homepath, desktoppath, 'vod')


if __name__ == '__main__':
    target_dir = path_to_desktop()
    target = ''
    file_paths = path_to_desktop()
    # print(file_paths)
    # target = _video_target_filename(video, args.format)
    _join_vods(target_dir, file_paths, target)
    # _join_vods()
