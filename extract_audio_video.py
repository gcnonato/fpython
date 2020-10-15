import json
import os
import subprocess
import PySimpleGUI as sg

class ManagerVideo:

  def extract_audio(self, video, output):
    # command = f"ffmpeg -i {video} -ac 1  -f flac -vn {output}"
    command = f"ffmpeg -i {video} {output}"
    print(command)
    subprocess.call(command, shell=True)


  def spawn_child(self, cmds=[]):
    subprocess.Popen(cmds)


  def extract_audio_stream(self, video_input, audio_output):
    cmds = ['ffmpeg', '-i', video_input, '-vn', '-acodec', 'copy', audio_output]
    spawn_child(cmds)


  def cut_video(self, video_input, start_cut, end_cut, video_output):
    cmds = ['ffmoeg', '-i', video_input, '-ss', start_cut, '-to', end_cut, '-c', 'copy', video_output]
    spawn_child(cmds)


  def convert_avi_to_mp4(self, avi_file_path, output_name):
    # cmds = f"ffmpeg -i input = {avi_file_path} -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 output = {output_name}"
    cmds = f"ffmpeg -i {avi_file_path} -y {output_name}"
    print(cmds)
    try:
      spawn_child(cmds)
    except Exception as err:
      print(f'Error..: {err}')
    return True


  def cut_video_duration(self, video_input, start_time, video_output, duration):
    filters = "fps=15,scale=320:-1:flags=lanczos"
    msg = ''
    if (video_input.endswith(".mp4")):  # or .avi, .mpeg, whatever.
      os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(video_input))
    try:
      cmds = f'ffmpeg -v warning -ss {start_time} -t {duration} -i {video_input} -vf {filters} {video_output}'
      print(cmds)
      spawn_child(cmds)
      msg = 'Tudo OK'
    except Exception as err:
      print(f'Error...: {err}')
      msg = f'Deu ruim... {err}'
    return msg

class Tela:
  def __init__(self):
    ...

  def layout_inicial(self, list_films):
    print(type(list_films))
    opcoes_films = [fimes[1] for fimes in list_films.items()]
    layout = [
      [sg.T("Escolha o filme")],
      [sg.Listbox(list(opcoes_films),
                size=(45,len(opcoes_films)+1),
                font=('Arial', 18),
                key='-LISTBOX-',
                enable_events=True,
            )
      ],
      [
        sg.Frame(
          layout=[
            [
              sg.InputText(key='name_film')
            ]
          ],
          title="Digite o Nome do Filme",
          title_color="yellow",
          relief=sg.RELIEF_SUNKEN,
          tooltip="Use these to set flags",
        )
      ],
      [sg.Exit(), sg.OK()],
    ]
    window = sg.Window("Extract Audio from Video", layout)
    while True:
      event, values = window.read()
      print(event, values)
      if event is None or event == 'Exit':
        sg.popup_auto_close("Saindo...", auto_close_duration=0.5)
        film = ''
        break
      if event == "OK":
        # print(window['-IN-'].update(values['_LISTBOX_']))
        # window.FindElement('-LISTBOX-').Update(scroll_to_index=3)
        # window.FindElement('-LISTBOX-').Update(set_to_index=4)
        film = values['-LISTBOX-'][0]
        # print(film)
        break
    return film
    window.close()


if __name__ == '__main__':
  tela = Tela()
  mv = ManagerVideo()
  # choice_films = 'predador'
  archive_json = "films.json"
  with open(archive_json, "rb") as text:
    infos_archive_to_extract = json.loads(text.read())
  print(infos_archive_to_extract)
  choice_films = tela.layout_inicial(infos_archive_to_extract)
  # os.chdir('../')
  # print(os.getcwd())

  file = choice_films[0]
  path = 'E:/Filmes/'
  filedirlist = os.listdir(path)
  for f in filedirlist:
    print(f)
  dirlist  = [os.path.abspath(d) for d in filedirlist if os.path.isdir(d)]
  file_video = f"{path}{file}"
  if file_video.endswith('.avi'):
    avi_file_path = file_video
    output_name = f'{path}{choice_films}.mp4'
    mv.convert_avi_to_mp4(avi_file_path, output_name)
    file_video = f"{path}{file}"
  new_file = file.split('.')[0]
  path_video = f'{os.path.abspath(os.path.dirname("../"))}/{new_file}.mp3'
  print(path_video)
  # cont = 1
  # while os.path.isfile(path_video):
  #   path_video = f'{os.path.abspath(os.path.dirname("../"))}/{new_file}_00{cont}.mp3'
  #   cont += 1
  # start_time = infos_archive_to_extract[choice_films][1]
  # end_time = infos_archive_to_extract[choice_films][2]
  # # start_time='01:37:10'
  # # end_time='01:39:40'
  # if (start_time.split(':')[2]):
  #   start = td(
  #     hours=int(start_time.split(':')[0]),
  #     minutes=int(start_time.split(':')[1]),
  #     seconds=int(start_time.split(':')[2])
  #   )
  #   end = td(
  #     hours=int(end_time.split(':')[0]),
  #     minutes=int(end_time.split(':')[1]),
  #     seconds=int(end_time.split(':')[2])
  #   )
  # else:
  #   start = td(minutes=int(start_time.split(':')[0]), seconds=int(start_time.split(':')[1]))
  #   end = td(minutes=int(end_time.split(':')[0]), seconds=int(end_time.split(':')[1]))
  # duration = (end - start).seconds
  # print(cut_video_duration(file_video, start_time, path_video, duration))
