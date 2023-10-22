import moviepy.editor as mp
from customtkinter import filedialog


def convert_mp4_to_gif():
    # Allow the user to select a .mp4 file
    video_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select .mp4 file",
        filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*"))
    )
    
    if video_path:
        # Allow the user to select a save location and name for the .gif file
        gif_path = filedialog.asksaveasfilename(
            confirmoverwrite=True,
            defaultextension=".gif",
            filetypes=(("GIF files", "*.gif"), ("All files", "*.*")),
            initialdir="/",
            title="Save .gif file",
        )
        
        if gif_path:
            clip = mp.VideoFileClip(video_path)  # Read the mp4 file.
            clip.write_gif(gif_path)  # Convert the mp4 file to a gif.