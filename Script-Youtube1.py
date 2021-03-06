# -*- coding: utf-8 -*-
import os
from os.path import expanduser
from time import sleep

os.path.expanduser("~")

# ---------------------------------------------------
# Criado por: Wolfterro
# Versão: 1.8.0 - Python 3.x
# Data: 07/01/2016
# ---------------------------------------------------

# ---------------------------------------------------
# Localização do script
# ---------------------------------------------------
location_script = os.getcwd()

# ---------------------------------------------------
# Função Principal: O script
# ---------------------------------------------------


def youtube_dl_script():
    # ---------------------------------------------------
    # Função de repetição do script
    # ---------------------------------------------------
    def repeat_script():
        print("")
        print("Deseja realizar outra operação com o script? [S/N]")
        REPEAT = input("Digite 'S' para sim ou 'N' para não: ")
        REPEAT = REPEAT.upper()
        if REPEAT == "S":
            os.system("clear")
            youtube_dl_script()
        else:
            print("")
            print("Saindo...")
            print("")
            # os.system("sleep 3")
            sleep(0.3)  # Time in seconds.

    # ---------------------------------------------------

    # ---------------------------------------------------
    # Função de caminho alternativo
    # ---------------------------------------------------
    def alt_path():
        print("")
        print(
            "Por favor, especifique o caminho desejado (Exemplo: /home/user/playlist):"
        )
        print(
            "========================================================================="
        )
        global ALT_PATH_SAVE
        ALT_PATH_SAVE = input("Insira o caminho desejado: ")
        print("")

    # ---------------------------------------------------

    # ---------------------------------------------------
    # Apresentação inicial do script
    # ---------------------------------------------------
    print("")
    print(
        "Script para Youtube-Dl: Baixar Vídeos e Músicas em Diversos Formatos (1.8.0 - Python 3.x)"
    )
    print(
        "========================================================================================="
    )
    print("")
    print(
        "* Este script requer o Youtube-Dl instalado e configurado para ser reconhecido como comando do shell"
    )
    print(
        "* O pacote 'libav' deverá estar instalado para converter os arquivos baixados se assim for necessário"
    )
    print(
        "* Caso não tenha o Youtube-Dl ou o pacote libav instalado, feche este script usando o comando Ctrl + C"
    )
    print(
        "* Caso queira baixar o Youtube-Dl, visite o seguinte endereço: https://github.com/rg3/youtube-dl"
    )
    print(
        "* Caso queira baixar o pacote libav, utilize o comando 'sudo apt-get install libav-tools', sem aspas"
    )
    print(
        "* Utilize os formatos de conversão de vídeo caso o formato nativo escolhido não estiver disponível"
    )
    print("")
    # ---------------------------------------------------

    # ---------------------------------------------------
    # Leitura da ID do vídeo desejado
    # ---------------------------------------------------
    def main_function_get_id():
        print(
            "Por favor, digite APENAS a ID do vídeo desejado (Exemplo: https://www.youtube.com/watch?v=ID_DO_VÍDEO):"
        )
        print(
            "======================================================================================================="
        )
        global ID
        ID = input("Insira a ID do vídeo: ")
        print("")

    # ---------------------------------------------------

    # ---------------------------------------------------
    # Função comum para vídeos: caminho
    # ---------------------------------------------------
    def video_function_path():
        print("Qual pasta deseja armazenar o arquivo de vídeo?")
        print("===============================================")
        print("")
        print("(1) Pasta 'home' do usuário atual (padrão)")
        print("(2) Pasta 'Vídeos' do usuário atual")
        print("(3) Pasta atual do script")
        print("(4) Especificar o caminho desejado")
        print("")
        LOCATIONV = input("Selecione uma das opções acima: ")
        # ---------------------------------------------------
        if LOCATIONV == "2":
            print("")
            print("Verificando a existência da pasta 'Vídeos'...")
            VIDEOEXIST = os.path.exists(expanduser("~/Vídeos"))
            # ------------------------------------------------
            if VIDEOEXIST is True:
                EXISTV = True
            else:
                EXISTV = False
            # ------------------------------------------------
            if EXISTV is True:
                os.chdir(expanduser("~/Vídeos"))
                print("")
                print("A pasta 'Vídeos' foi selecionada!")
                print("")
            else:
                print("")
                print("A pasta 'Vídeos' não existe! Deseja criá-la? [S/N]")
                CREATEV = input("Digite 'S' para sim ou 'N' para não: ")
                CREATEV = CREATEV.upper()
                # ---------------------------------------------
                if CREATEV == "S":
                    os.chdir(expanduser("~/"))
                    os.system(expanduser("mkdir Vídeos"))
                    os.chdir(expanduser("~/Vídeos"))
                    print("")
                    print("A pasta 'Vídeos' foi criada e selecionada!")
                    print("")
                else:
                    os.chdir(expanduser(location_script))
                    print("")
                    print("Neste caso, a pasta atual do script será selecionada!")
                    print("")
                # ----------------------------------------------
            # --------------------------------------------------
        elif LOCATIONV == "3":
            os.chdir(expanduser(location_script))
            print("")
            print("A pasta atual do script foi selecionada!")
            print("")
        elif LOCATIONV == "4":
            alt_path()
            print("Verificando a existência do caminho '" + ALT_PATH_SAVE + "' ...")
            ALT_PATH_EXIST = os.path.exists(expanduser(ALT_PATH_SAVE))

            if ALT_PATH_EXIST is False:
                print("")
                print(
                    "O caminho especificado não existe! A pasta 'home' do usuário atual será selecionada!"
                )
                os.chdir(expanduser("~/"))
                print("")
            else:
                os.chdir(expanduser(ALT_PATH_SAVE))
                print("")
                print("O caminho '" + ALT_PATH_SAVE + "' foi selecionado!")
                print("")
        else:
            os.chdir(expanduser("~/"))
            print("")
            print("A pasta 'home' do usuário atual foi selecionada!")
            print("")

    # ---------------------------------------------------

    # ---------------------------------------------------
    # Função comum para músicas: caminho
    # ---------------------------------------------------
    def audio_function_path():
        print("Qual pasta deseja armazenar o arquivo de áudio?")
        print("===============================================")
        print("")
        print("(1) Pasta 'home' do usuário atual (padrão)")
        print("(2) Pasta 'Música' do usuário atual")
        print("(3) Pasta atual do script")
        print("(4) Especificar o caminho desejado")
        print("")
        LOCATIONM = input("Selecione uma das opções acima: ")
        # ---------------------------------------------------
        if LOCATIONM == "2":
            print("")
            print("Verificando a existência da pasta 'Música'...")
            MUSICEXIST = os.path.exists(expanduser("~/Música"))
            # ------------------------------------------------
            if MUSICEXIST is True:
                EXISTM = True
            else:
                EXISTM = False
            # ------------------------------------------------
            if EXISTM is True:
                os.chdir(expanduser("~/Música"))
                print("")
                print("A pasta 'Música' foi selecionada!")
                print("")
            else:
                print("")
                print("A pasta 'Música' não existe! Deseja criá-la? [S/N]")
                CREATEM = input("Digite 'S' para sim ou 'N' para não: ")
                CREATEM = CREATEM.upper()
                # ---------------------------------------------
                if CREATEM == "S":
                    os.chdir(expanduser("~/"))
                    os.system(expanduser("mkdir Música"))
                    os.chdir(expanduser("~/Música"))
                    print("")
                    print("A pasta 'Música' foi criada e selecionada!")
                    print("")
                else:
                    os.chdir(expanduser(location_script))
                    print("")
                    print("Neste caso, a pasta atual do script será selecionada!")
                    print("")
                # ----------------------------------------------
            # --------------------------------------------------
        elif LOCATIONM == "3":
            os.chdir(expanduser(location_script))
            print("")
            print("A pasta atual do script foi selecionada!")
            print("")
        elif LOCATIONM == "4":
            alt_path()
            print("Verificando a existência do caminho '" + ALT_PATH_SAVE + "' ...")
            ALT_PATH_EXIST = os.path.exists(expanduser(ALT_PATH_SAVE))

            if ALT_PATH_EXIST is False:
                print("")
                print(
                    "O caminho especificado não existe! A pasta 'home' do usuário atual será selecionada!"
                )
                os.chdir(expanduser("~/"))
                print("")
            else:
                os.chdir(expanduser(ALT_PATH_SAVE))
                print("")
                print("O caminho '" + ALT_PATH_SAVE + "' foi selecionado!")
                print("")
        else:
            os.chdir(expanduser("~/"))
            print("")
            print("A pasta 'home' do usuário atual foi selecionada!")
            print("")

    # ---------------------------------------------------

    # ---------------------------------------------------
    # Função principal para o download de vídeos (nativos)
    # ---------------------------------------------------
    def video_function_default_mp4():
        # ---------------------------------------------------
        os.system("youtube-dl --format mp4 https://www.youtube.com/watch?v=" + ID)
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    def video_function_mkv():
        # ---------------------------------------------------
        os.system("youtube-dl --format mkv https://www.youtube.com/watch?v=" + ID)
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    def video_function_webm():
        # ---------------------------------------------------
        os.system("youtube-dl --format webm https://www.youtube.com/watch?v=" + ID)
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    def video_function_avi():
        # ---------------------------------------------------
        os.system("youtube-dl --format avi https://www.youtube.com/watch?v=" + ID)
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    # -----------------------------------------------------------

    # ---------------------------------------------------
    # Função principal para o download de vídeos (conversão)
    # ---------------------------------------------------
    def video_function_default_mp4_conversion():
        # ---------------------------------------------------
        os.system("youtube-dl --recode-video mp4 https://www.youtube.com/watch?v=" + ID)
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    def video_function_mkv_conversion():
        # ---------------------------------------------------
        os.system("youtube-dl --recode-video mkv https://www.youtube.com/watch?v=" + ID)
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    def video_function_webm_conversion():
        # ---------------------------------------------------
        os.system(
            "youtube-dl --recode-video webm https://www.youtube.com/watch?v=" + ID
        )
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    def video_function_avi_conversion():
        # ---------------------------------------------------
        os.system("youtube-dl --recode-video avi https://www.youtube.com/watch?v=" + ID)
        # ---------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    # -----------------------------------------------------------

    # -----------------------------------------------------------
    # Função principal para o download de músicas
    # -----------------------------------------------------------
    def audio_function_default_mp3():
        # ----------------------------------------------------
        os.system(
            "youtube-dl --extract-audio --prefer-avconv --audio-format mp3 https://www.youtube.com/watch?v="
            + ID
        )
        # ----------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    def audio_function_wav():
        # ----------------------------------------------------
        os.system(
            "youtube-dl --extract-audio --prefer-avconv --audio-format wav https://www.youtube.com/watch?v="
            + ID
        )
        # ----------------------------------------------------
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        # ---------------------------------------------------

    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # Funções opcionais do script
    # ------------------------------------------------------------
    def option_function_update():
        os.system("youtube-dl --update")
        sleep(0.5)  # Time in seconds.
        # os.system("sleep 5")

    # ------------------------------------------------------------
    def option_function_install():
        os.chdir(expanduser("~/"))
        print("Baixando youtube-dl usando 'wget'...")
        print("")
        os.system("wget -O youtube-dl 'https://yt-dl.org/downloads/latest/youtube-dl'")
        print("Aplicando permissões de execução...")
        print("")
        os.system("chmod a+rx youtube-dl")
        print("Movendo para a pasta '/usr/bin'...")
        print("")

        if os.geteuid() != 0:
            print(
                "É necessário privilégios de root para mover o arquivo para a pasta selecionada!"
            )
            print(
                "Deseja utilizar o comando 'sudo' para mover 'youtube-dl' para '/usr/bin'? [S/N]"
            )
            MOVEFILE = input("Digite 'S' para sim ou 'N' para não: ")
            MOVEFILE = MOVEFILE.upper()

            if MOVEFILE == "S":
                os.system("sudo mv youtube-dl /usr/bin")
                print("")
                print("Youtube-Dl está instalado!")
                # os.system("sleep 5")
                sleep(0.5)  # Time in seconds.
            else:
                print("")
                print(
                    "O arquivo não pôde ser movido por falta de permissão! Saindo da Instalação..."
                )
                os.system("rm youtube-dl")
                # os.system("sleep 5")
                sleep(0.5)  # Time in seconds.
        else:
            os.system("mv youtube-dl /usr/bin")
            print("Youtube-Dl está instalado!")
            # os.system("sleep 5")
            sleep(0.5)  # Time in seconds.

    # ------------------------------------------------------------
    def option_conversion_formats():
        print("Qual formato deseja que o vídeo seja convertido?")
        print("================================================")
        print("")
        print("Formatos de vídeo (conversão):")
        print("(1) Arquivo de vídeo em formato .MP4")
        print("(2) Arquivo de vídeo em formato .MKV")
        print("(3) Arquivo de vídeo em formato .WEBM")
        print("(4) Arquivo de vídeo em formato .AVI")
        print("")
        ESCOLHACONVERSAO = input("Escolha uma das opções acima: ")
        print("")
        if ESCOLHACONVERSAO == "1":
            main_function_get_id()
            video_function_path()
            video_function_default_mp4_conversion()
        elif ESCOLHACONVERSAO == "2":
            main_function_get_id()
            video_function_path()
            video_function_mkv_conversion()
        elif ESCOLHACONVERSAO == "3":
            main_function_get_id()
            video_function_path()
            video_function_webm_conversion()
        elif ESCOLHACONVERSAO == "4":
            main_function_get_id()
            video_function_path()
            video_function_avi_conversion()
        else:
            print("Esta não é uma opção válida!")
            sleep(0.5)  # Time in seconds.
            # os.system("sleep 5")

    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # Opções para o salvamento do vídeo selecionado
    # ------------------------------------------------------------
    print("Como deseja salvar o vídeo?")
    print("===========================")
    print("")
    print("Instalação:")
    print("(0) Instalar Youtube-Dl")
    print("")
    print("Formatos de vídeo (nativos):")
    print("(1) Arquivo de vídeo em formato .MP4")
    print("(2) Arquivo de vídeo em formato .MKV")
    print("(3) Arquivo de vídeo em formato .WEBM")
    print("(4) Arquivo de vídeo em formato .AVI")
    print("")
    print("Formatos de áudio:")
    print("(5) Arquivo de música em formato .MP3")
    print("(6) Arquivo de música em formato .WAV")
    print("")
    print("Opções do script:")
    print("(7) Formatos de Conversão de Vídeo")
    print("(8) Atualizar Youtube-Dl")
    print("(9) Sair do Youtube-Dl Script")
    print("")
    ESCOLHA = input("Escolha uma das opções acima: ")
    print("")
    if ESCOLHA == "0":
        option_function_install()
        repeat_script()
    elif ESCOLHA == "1":
        main_function_get_id()
        video_function_path()
        video_function_default_mp4()
        repeat_script()
    elif ESCOLHA == "2":
        main_function_get_id()
        video_function_path()
        video_function_mkv()
        repeat_script()
    elif ESCOLHA == "3":
        main_function_get_id()
        video_function_path()
        video_function_webm()
        repeat_script()
    elif ESCOLHA == "4":
        main_function_get_id()
        video_function_path()
        video_function_avi()
        repeat_script()
    elif ESCOLHA == "5":
        main_function_get_id()
        audio_function_path()
        audio_function_default_mp3()
        repeat_script()
    elif ESCOLHA == "6":
        main_function_get_id()
        audio_function_path()
        audio_function_wav()
        repeat_script()
    elif ESCOLHA == "7":
        option_conversion_formats()
        repeat_script()
    elif ESCOLHA == "8":
        option_function_update()
        repeat_script()
    elif ESCOLHA == "9":
        print("Saindo...")
        print("")
        # os.system("sleep 3")
        sleep(0.3)  # Time in seconds.
    else:
        print("Esta não é uma opção válida!")
        # os.system("sleep 5")
        sleep(0.5)  # Time in seconds.
        repeat_script()


# ------------------------------------------------------------
youtube_dl_script()
