import tkinter as tk
from tkinter import filedialog, messagebox
import moviepy.editor as mp

def convert_to_gif():
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
            defaultextension='.gif',
            filetypes=(("GIF files", "*.gif"), ("All files", "*.*")),
            initialdir="/",
            title="Save .gif file",
        )
        
        if gif_path:
            # Read the mp4 file
            clip = mp.VideoFileClip(video_path)

            # Convert the mp4 file to a gif
            clip.write_gif(gif_path)

            # Show a message when file conversion is complete.
            messagebox.showinfo('Conversion Complete!', 'DONE!')
            app.destroy()  # Close the tkinter app.

# Create the Tkinter app
app = tk.Tk()
app.title("Video to GIF Converter")

# Create a button that triggers the conversion function
convert_btn = tk.Button(app, text="Select .mp4 file and Convert to .gif", command=convert_to_gif)
convert_btn.pack(pady=20)

# Run the Tkinter event loop
app.mainloop()