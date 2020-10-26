import json
import os
import subprocess
import PySimpleGUI as sg
from datetime import timedelta as td

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
    self.spawn_child(cmds)


  def cut_video(self, video_input, start_cut, end_cut, video_output):
    cmds = ['ffmoeg', '-i', video_input, '-ss', start_cut, '-to', end_cut, '-c', 'copy', video_output]
    self.spawn_child(cmds)


  def convert_avi_to_mp4(self, avi_file_path, output_name):
    # cmds = f"ffmpeg -i input = {avi_file_path} -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 output = {output_name}"
    cmds = f"ffmpeg -i {avi_file_path} -y {output_name}"
    print(cmds)
    try:
      self.spawn_child(cmds)
    except Exception as err:
      print(f'Error..: {err}')
    return True


  def cut_video_duration(self, video_input, start_time, video_output, duration):
    filters = "fps=15,scale=320:-1:flags=lanczos"
    msg = ''
    if (video_input.endswith(".mp4")):  # or .avi, .mpeg, whatever.
      os.system(f"ffmpeg -i {video_input} -f image2 -vf fps=fps=1 output%d.png")
    try:
      cmds = f'ffmpeg -v warning -ss {start_time} -t {duration} -i {video_input} -vf {filters} {video_output}'
      print(cmds)
      self.spawn_child(cmds)
      msg = 'Tudo OK'
    except Exception as err:
      print(f'Error...: {err}')
      msg = f'Deu ruim... {err}'
    return msg

  def transform_in_file_audio(self):
    if not choice_films:
      print('Não foi selecionado nenhum filme!!!!!')
      exit(0)
    file_video = f"{''.join((path, choice_films))}"
    new_file = choice_films.split('.')[0]
    path_video = f'{os.path.abspath(os.path.dirname("../"))}/{new_file}.mp3'
    cont = 1
    while os.path.isfile(path_video):
      path_video = f'{os.path.abspath(os.path.dirname("../"))}/{new_file}_00{cont}.mp3'
      cont += 1
    print(path_video)
    inicio = td(
      hours=int(start.split(':')[0]),
      minutes=int(start.split(':')[1]),
      seconds=int(start.split(':')[2])
    )
    fim = td(
      hours=int(end.split(':')[0]),
      minutes=int(end.split(':')[1]),
      seconds=int(end.split(':')[2])
    )
    duration = (fim - inicio).seconds
    print(duration)
    print(mv.cut_video_duration(file_video, start, path_video, duration))

class Tela:

  def layout_inicial(self, list_films):
    layout = [
      [sg.T("Escolha o filme")],
      [sg.Listbox(list_films,
                size=(45,len(list_films)+1),
                font=('Arial', 18),
                key='-LISTBOX-',
                enable_events=True,
            )
      ],
      [
        sg.Frame(
          layout=[
            [ sg.T("Inicial"),
              sg.InputText(key='hours_inicial', size='30'),
              sg.T(":"),
              sg.InputText(key='minutes_inicial', size='30'),
              sg.T(":"),
              sg.InputText(key='seconds_inicial', size='30'),
            ],
            [ sg.T("Final "),
              sg.InputText(key='hours_final', size='30'),
              sg.T(":"),
              sg.InputText(key='minutes_final', size='30'),
              sg.T(":"),
              sg.InputText(key='seconds_final', size='30'),
            ]
          ],
          title="Horas, Minutos, Segundos",
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
      # print(event, values)
      if event is None or event == 'Exit':
        sg.popup_auto_close("Saindo...", auto_close_duration=0.5)
        film = ''
        start = ''
        end = ''
        break
      if event == "OK":
        # print(window['-IN-'].update(values['_LISTBOX_']))
        # window.FindElement('-LISTBOX-').Update(scroll_to_index=3)
        # window.FindElement('-LISTBOX-').Update(set_to_index=4)
        film = values['-LISTBOX-'][0]
        start = ':'.join((
          values['hours_inicial'],
          values['minutes_inicial'],
          values['seconds_inicial'])
        )
        end = ':'.join((
          values['hours_final'],
          values['minutes_final'],
          values['seconds_final'])
        )
        break
    return film, start, end
    window.close()


if __name__ == '__main__':
  tela = Tela()
  mv = ManagerVideo()
  archive_json = "films.json"
  list_files_dir_current = []
  path = 'E:/Filmes/'
  list_files_and_dirs = os.listdir(path)
  for files_or_dir in list_files_and_dirs:
    if os.path.isfile(''.join((path,files_or_dir))):
      list_files_dir_current.append(files_or_dir)
  choice_films, start, end = tela.layout_inicial(list_files_dir_current)
  print(choice_films, start, end)

  # file_video = f"{path}{file}"
  # if file_video.endswith('.avi'):
  #   avi_file_path = file_video
  #   output_name = f'{path}{choice_films}.mp4'
  #   mv.convert_avi_to_mp4(avi_file_path, output_name)
  #   file_video = f"{path}{file}"
  # new_file = file.split('.')[0]
  # path_video = f'{os.path.abspath(os.path.dirname("../"))}/{new_file}.mp3'
  # print(path_video)
  # cont = 1
  # while os.path.isfile(path_video):
  #   path_video = f'{os.path.abspath(os.path.dirname("../"))}/{new_file}_00{cont}.mp3'
  #   cont += 1
  # start_time = infos_archive_to_extract[choice_films][1]
  # end_time = infos_archive_to_extract[choice_films][2]
  # # start_time='01:37:10'
  # # end_time='01:39:40'
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
