# -*- coding: utf-8 -*-
import tkinter as tk

bg_color = "#202020"
# Design padrão das Entry
entry_design = {
    "highlightbackground": "#ccc",
    "insertbackground": "#ccc",
    "font": ("Helvetica", 11),
    "highlightcolor": "#ccc",
    "relief": "flat",
    "bg": "white",
    "fg": "#333",
    "width": 30,
    "bd": 3,
}
label_design = {
    "font": ("Helvetica", 11),
    "bg": "#202020",
    "fg": "green",
}
label_design_Titulo = {
    "font": ("Helvetica", 21),
    "bg": "#202020",
    "fg": "green",
}
label_design2 = {
    "font": ("Helvetica", 11),
    "bg": "#202020",
    "fg": "white",
}
# Design do botão de login.
login_button_design = {
    "highlightbackground": "#00ff00",
    "activebackground": "#00ff00",
    "activeforeground": "#202020",
    "relief": "flat",
    "bg": "#00ff00",
    "fg": "white",
    "bd": 0,
}
text_design = {
    "font": ("Georgia", 11),
    "bg": "#202020",
    "fg": "orange",
}

root = tk.Tk()
# login_screen = tk.PhotoImage(file="img/logo.png")


root.title("Login")

root.resizable(width=False, height=False)
root.geometry("400x450+350+20")

# logo_l = Label(root,width=98, height=100, #image=login_screen)
# logo_l.place(x=150, y=80)


campuser = tk.Entry(root, **entry_design)
campuser.configure(**entry_design)
campuser.place(x=80, y=250)

camppass = tk.Entry(root, show="*", **entry_design)
camppass.bind("<FocusOut>")
camppass.bind("<FocusIn>")
camppass.place(x=80, y=290)

button_start = tk.Button(root, text="Login", width=15)
button_start.configure(**login_button_design)
button_start.place(x=130, y=330)

# cor da tela
root["bg"] = "#202020"
root.mainloop()
