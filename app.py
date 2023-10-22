from customtkinter import *
from modules import convert_mp4_to_gif



app = CTk()
app.geometry("500x400")

set_appearance_mode("system")
set_default_color_theme("blue")

btn = CTkButton(
    master=app,
    text="Select .mp4 to convert to .gif",
    corner_radius=6,
    command=convert_mp4_to_gif
)

btn.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

app.mainloop()