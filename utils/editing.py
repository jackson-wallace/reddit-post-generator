import random
from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    vfx,
    ImageClip,
    CompositeVideoClip,
    CompositeAudioClip,
    concatenate_audioclips,
)
from moviepy.video.fx.resize import resize
from moviepy.audio.fx.volumex import volumex
from datetime import date
from config import ORIGINAL_OUTPUT_PATH


def overlay_on_video(
    i, background_video_path, title_audio_path, body_audio_path, screenshot_path
):
    # moad the main video
    background_clip = VideoFileClip(background_video_path)

    # load .mp3 files as clips
    body_audio_clip = AudioFileClip(body_audio_path)
    title_audio_clip = AudioFileClip(title_audio_path)
    full_audio_clip = concatenate_audioclips([title_audio_clip, body_audio_clip])
    music_clip = AudioFileClip(background_video_path)

    # get duration of background video
    background_duration = background_clip.duration
    speech_duration = full_audio_clip.duration

    # randomize when the background clip starts
    background_start = random.randint(0, int(background_duration - speech_duration))
    background_clip_section = background_clip.subclip(
        t_start=(0, 0, background_start),
        t_end=(0, 0, background_start + speech_duration),
    )  # insert duration

    # Desired size for mobile aspect ratio (9:16)
    width, height = (
        background_clip_section.size[1] * (9 / 16),
        background_clip_section.size[1],
    )
    x_center = background_clip_section.size[0] / 2
    y_center = background_clip_section.size[1] / 2

    # x1, y1 indicates the top left
    x1 = x_center - (width / 2)
    y1 = y_center - (height / 2)
    x2 = x_center + (width / 2)
    y2 = y_center + (height / 2)

    # Crop the clip centered in the middle
    cropped_clip = vfx.crop(background_clip_section, x1=x1, y1=y1, x2=x2, y2=y2)

    # Load the image as a clip
    img_clip = (
        ImageClip(screenshot_path)
        .set_start(0)  # which second to start displaying image
        .set_duration(title_audio_clip.duration)  # how long to display image
        .set_pos(("center", "center"))
        .resize(width=width * 0.65)
    )

    # Overlay image on the video
    final_clip = CompositeVideoClip([cropped_clip, img_clip])

    music_subclip = music_clip.subclip(
        t_end=(0, 0, speech_duration),
    )

    music_subclip_leveled = music_subclip.fx(volumex, 0.2)

    final_audio = CompositeAudioClip([full_audio_clip, music_subclip_leveled])

    final_clip.audio = final_audio

    # Write the cropped clip with the overlayed image to an output MP4 file
    final_clip.write_videofile(ORIGINAL_OUTPUT_PATH + f"{date.today()}_{i}.mp4")
