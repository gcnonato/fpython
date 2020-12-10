# -*- coding: utf-8 -*-
import subprocess
import os

location_script = os.getcwd()
homepath = os.path.expanduser(os.getenv("USERPROFILE"))
desktoppath = "Desktop"

streamers = ["rennerocha", "dunossauro", "marinaul"]


def run(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    return proc.returncode, stdout, stderr


options = " videos"
code, out, err = run(["twitch-dl", "videos", "marinaul"])
os.chdir(os.path.join(homepath, desktoppath))
output = os.fsdecode(subprocess.check_output(["twitch-dl", "videos", streamers[2]]))

with open("videos_streamers.txt", "w") as _file:
    _file.write(output)

with open("videos_streamers.txt", "r") as _file:
    tex_nv = _file.readlines()
not_words_in_the_list = [
    "marinaul",
    "There are more",
    "Increase",
    "Published",
    "--------------------------------------------------------------------------------",
]
for palavra in tex_nv:
    # if not not_words_in_the_list.intersection(' '.join(palavra))\
    if palavra not in not_words_in_the_list and palavra not in "\n":
        print(palavra.split())

# for palavra in tex_nv:
#     if 'marinaul' not in palavra and 'There are more' not in palavra\
#             and 'Loading' not in palavra and '-----' not in palavra\
#             and palavra not in '\n':
#         print(palavra.split())

# nro_video_para_baixar = 821404850
# print(os.getcwd())
# code, out, err = run(["twitch-dl", "download", f"{nro_video_para_baixar}"])
# print(code, out, err)
# f'twitch-dl download {nro_video_para_baixar}'
# subprocess.check_output(
#         [
#             "twitch-dl",
#             "download",
#             f"{nro_video_para_baixar}"]
#     )
