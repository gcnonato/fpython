import os

import PySimpleGUI as sg

form = sg.FlexForm("Everything bagel", default_element_size=(80, 1))  # config form

layout = [
    [sg.T("Source Folder")],  # folder choice
    [sg.In(key="input")],  # key of path to be followed
    [sg.FolderBrowse(target="input")],  # target of folder browser
    [sg.T("Enter the word you want: ", font=("Helvetica", 16))],  # text  asking input
    [sg.Input(key="5")],  # place to type the input and key to use in search_str
    [sg.Multiline(key="TEXT", size=(60, 10), enter_submits=True)],
    [sg.Button("Submit"), sg.Button("Exit")],
]

window = sg.Window("Find word in file.txt in folders", layout)
event, values = window.read()
window.close()
search_path = values["input"]  # directory to read files from
file_type = ".txt"  # extension selected to be read
search_str = values["5"]  # word to be searched


def my_word():
    strings = []
    # Repeat for each file in the directory
    for folder, dirs, files in os.walk(search_path):

        for file in files:
            # open file for reading
            if file.endswith(file_type):  # file type filter
                fullpath = os.path.join(folder, file)
                with open(fullpath, "r", encoding="ascii", errors="ignore") as f:
                    # sg.PopupScrolled do not accept str.(my_word()) - it returns []
                    # so I had to create the  my_list_of_files
                    # to append the lines
                    my_list_of_files = []
                    # for line in f:  crashes the app then I must use for line in f.readlines():
                    #                        if search_str in line: ******I want this line but if I use it
                    # sg.PopupScrolled prints  []
                    #                            print('\n', fullpath, '\n', line)
                    for line in f.readlines():  # Read line from the file:
                        # if search_str in line: ** I want this but results[]
                        a = ("\n", fullpath, line)  # **just this works but
                        my_list_of_files.append(a)  # **results directory list
                    return my_list_of_files  # open sg.PopupScrolled  but returns all files from directory
                    break

    else:
        print("Did not find another or a match")
