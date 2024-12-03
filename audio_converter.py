from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os


def convert_to_mp3(input_file, output_dir="output_audio"):
    """
    Converts an audio or video file to an MP3 file.

    Args:
        input_file (str): Path to the input file (audio or video).
        output_dir (str): Directory to save the MP3 file.

    Returns:
        str: Path to the converted MP3 file.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract file name and extension
    file_name = os.path.basename(input_file)
    base_name, _ = os.path.splitext(file_name)

    # Define the output MP3 file path
    output_file = os.path.join(output_dir, f"{base_name}.mp3")

    try:
        # Check if input is a video or audio file
        if os.path.splitext(input_file)[1].lower() in ['.mp4', '.avi', '.mov', '.webm', '.movpkg']:
            # For video files
            media = VideoFileClip(input_file)
        else:
            # For audio files
            media = AudioFileClip(input_file)

        # Write the MP3 file
        media.write_audiofile(output_file)
        print(f"File successfully converted to MP3: {output_file}")
        return output_file
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    input_path = "record_out.ogg"  # Replace with your audio or video file path
    output_mp3 = convert_to_mp3(input_path)
