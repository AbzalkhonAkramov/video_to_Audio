from moviepy.video.io.VideoFileClip import VideoFileClip


# pip install mediapy

# Function to convert video file to MP3
def video_to_mp3(video_path, output_path):
    try:
        # Load the video file
        video = VideoFileClip(video_path)

        # Extract the audio from the video
        audio = video.audio

        # Write the audio as an MP3 file
        audio.write_audiofile(output_path, codec='mp3')
        print(f"Video audio saved as {output_path}")
    except Exception as e:
        print(f"Error while converting video to MP3: {e}")



# Example usage for converting video to MP3
video_to_mp3("exa.mp4", "resultOfMP4.mp3")  # Replace with your video file path
