from pydub import AudioSegment


def speed_up_audio(file_path, speed_factor=1.1):
    sound = AudioSegment.from_file(file_path, format="mp3")

    # Speed up the sound
    sound = sound.speedup(playback_speed=speed_factor)

    # Export the result
    output_path = "sped_up_" + file_path
    sound.export(output_path, format="mp3")

    return output_path
