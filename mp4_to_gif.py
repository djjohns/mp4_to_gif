from moviepy.editor import VideoFileClip

def convert_to_gif(video_path, gif_path):
    # Load the video clip
    video = VideoFileClip(video_path)
    # Set the output file path and name
    gif_output = gif_path
    # Convert the video clip to a gif
    video.write_gif(gif_output)



if __name__=='__main__':
    # Specify the .mp4 file path
    mp4_path = "path/to/input.mp4"
    # Specify the .gif file path
    gif_path = "path/to/output.gif"
    # Call the conversion function
    convert_to_gif(mp4_path, gif_path)