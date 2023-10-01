import elevenlabs
from config import ELEVENLABS_API_KEY

elevenlabs.set_api_key(ELEVENLABS_API_KEY)


def text_to_speech(i, title, body):
    title_audio = elevenlabs.generate(text=title, voice="Adam")
    elevenlabs.save(title_audio, f"title_audio/audio-{i}.mp3")

    body_audio = elevenlabs.generate(text=body, voice="Adam")
    elevenlabs.save(body_audio, f"body_audio/audio-{i}.mp3")

    return (f"title_audio/audio-{i}.mp3", f"body_audio/audio-{i}.mp3")
