import os

comando_do_video = 'twitch-dl videos'
comando_do_download_do_video = 'twitch-dl download -q source' #best quality

user_twitch = 'italojs_'
# os.system(' '.join((comando_do_video,user_twitch)) )

# twitch-dl download -q source


nro_do_video_a_baixar = '760910544'
os.system(
    ' '.join(
        (
            comando_do_download_do_video,
            nro_do_video_a_baixar
        )
    )
)






