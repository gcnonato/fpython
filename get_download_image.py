from requests import get
from io import BytesIO
from PIL import Image
import os
import sys
from bs4 import BeautifulSoup as bs
import PySimpleGUI as sg


def verify_link(link):
    try:
        image = get(link)
        try:
            if image.status_code == 200:
                return image
        except Exception as err:
            return False
    except Exception as err:
        return False


def get_image(image_url):
    """
    Get image based on url.
    :return: Image name if everything OK, False otherwise
    """
    image_name = os.path.split(image_url)[1]
    image = verify_link(image_url)
    if image:
         # Use your own path or "" to use current working directory. Folder must exist.
        homepath = os.path.expanduser(os.getenv("USERPROFILE"))
        desktoppath = "Desktop"
        base_dir = os.path.join(homepath, desktoppath, "images")
        with open(os.path.join(base_dir, image_name), "wb") as f:
            f.write(image.content)
        return image_name
    return False


def list_folder():
    layout = [
        [sg.Frame(
                layout=[
                    [sg.T("URL")], [sg.In(key="link"), ],
                ], title="Paste link", title_color="yellow", relief=sg.RELIEF_SUNKEN,)],
        [sg.Frame(
                "Botões",
                [[sg.Button("Submit"), sg.Exit()]], background_color="lightblue", title_color="red", ) ],
    ]
    window = sg.Window("Manipule URL´s", layout, size=(430, 160))
    while True:
        event, values = window.read()
        if "Submit" in event:
            link = values['link']
            # print(link)
            link = verify_link(link)
            if link:
                return link
            else:
                sg.Print(link)
        if "viewfiles" in event:
            # change the "output" element to be the value of "input" element
            # window['-OUTPUT-'].update(values['-IN-'])
            filename = values["filename"]
        if event == sg.WIN_CLOSED or "Exit" in event:
            sg.popup_auto_close("Saindo...", auto_close_duration=0.5)
            break
    window.close()


if __name__ == '__main__':
    url = 'http://sisadm2.pjf.mg.gov.br/imagem/'
    # argv = len(sys.argv)
    # if argv < 2:
    #     print("Faltou passar a URL.")
    #     sys.exit(0)
    # url = sys.argv[1]
    list_folder()
    # response = get(url)
    # soup = bs(response.content, 'lxml')
    # for images in soup.find_all('a'):
    #     image = images.contents[0]
    #     if str(image).endswith(('jpg', 'png')):
    #         link = ''.join((url, image))
    # homepath = os.path.expanduser(os.getenv("USERPROFILE"))
    # desktoppath = "Desktop"
    # base_dir = os.path.join(homepath, desktoppath, "images")
    # for filename in os.listdir(base_dir):
    #     path = '\\'.join((base_dir, filename.strip()))
    #     try:
    #         im = Image.open(path)
    #         im.verify()
    #         im.close()
    #     except IOError as err:
    #         print(err)
