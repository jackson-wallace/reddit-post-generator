import os
from moviepy.editor import VideoFileClip
from datetime import date
import shutil
from config import SPLICED_VIDEO_READ_PATH, SPLICED_VIDEO_WRITE_PATH


def splice_video_into_segments(video_path, output_directory):
    clip = VideoFileClip(video_path)
    segment_duration = 59  # seconds, must be <= 59 seconds to be a YouTube Short

    if clip.duration <= segment_duration:
        # Ensure the output directory exists
        segment_output_directory = os.path.join(
            output_directory, os.path.basename(video_path).split(".")[0]
        )
        if not os.path.exists(segment_output_directory):
            os.makedirs(segment_output_directory)

        # Determine the output path for this segment
        output_path = os.path.join(segment_output_directory, f"segment_0.mp4")

        # Copy the original file to the output path instead of writing a new one
        shutil.copy(video_path, output_path)  # Use shutil.copy to copy the file

    else:
        num_segments = int(clip.duration // segment_duration)
        leftover_time = (
            clip.duration % segment_duration
        )  # Remaining time after dividing by segment_duration

        for i in range(
            num_segments + 1
        ):  # +1 to account for the possible leftover segment
            start_time = i * segment_duration

            if (
                i == num_segments and leftover_time > 0
            ):  # This is the last iteration and there's leftover time
                end_time = start_time + leftover_time
            else:
                end_time = (i + 1) * segment_duration

            # Extract the segment
            segment = clip.subclip(start_time, end_time)

            # Ensure the output directory exists
            segment_output_directory = os.path.join(
                output_directory, os.path.basename(video_path).split(".")[0]
            )
            if not os.path.exists(segment_output_directory):
                os.makedirs(segment_output_directory)

            # Determine the output path for this segment
            output_path = os.path.join(segment_output_directory, f"segment_{i}.mp4")

            # Write the segment to the output path
            segment.write_videofile(output_path, codec="libx264", audio_codec="aac")


if __name__ == "__main__":
    # Get the number of videos to process
    num_videos = int(
        input("How many videos am I splicin' today boss? (Italian accent): ")
    )

    output_directory = SPLICED_VIDEO_WRITE_PATH

    # Loop through each video and process
    for i in range(num_videos):
        video_path = SPLICED_VIDEO_READ_PATH + f"{date.today()}_{i}.mp4"
        splice_video_into_segments(video_path, output_directory)
