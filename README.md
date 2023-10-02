# Reddit Story Video Generator

---

## Introduction

This project automates the process of creating "Reddit Story" style videos for platforms like TikTok, YouTube Shorts, and Instagram Reels. It combines text-to-speech, background videos, and title screenshots into a single video. Users can then add subtitles using CapCut.

## Setup

### Prerequisites

- Python installed on your system.
- [CapCut](https://www.capcut.net/) installed for adding subtitles. [Tutorial Link](https://www.youtube.com/watch?v=soZRgP28O2g).
- Necessary authentication for PRAW. [Tutorial Link](https://www.youtube.com/watch?v=NRgfgtzIhBQ&t=441s) (Skip to 0:40).
- Create an [Elevenlabs](https://elevenlabs.io/speech-synthesis) account and generate an API key.

### Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```shell
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```shell
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```shell
     source venv/bin/activate
     ```
5. Install the required packages:
   ```shell
   pip install -r requirements.txt
   ```

### Configuration

Create a `config.py` file in the project directory with the following variables:

```python
SUBREDDIT_NAME = ""  # Name of the subreddit to fetch posts from
PRAW_CLIENT_ID = ""  # Your PRAW client ID
PRAW_CLIENT_SECRET = ""  # Your PRAW client secret
PRAW_USER_AGENT = ""  # User agent for PRAW (can be anything)
ELEVENLABS_API_KEY = ""  # Your ElevenLabs API key
ORIGINAL_OUTPUT_PATH = ""  # Path to save videos without captions
SPLICED_VIDEO_READ_PATH = ""  # Path to read videos with captions from CapCut
SPLICED_VIDEO_WRITE_PATH = ""  # Path to save spliced videos
```

## Usage

### Generate Video

Run `main.py` to generate a video combining text-to-speech, background video, and title screenshot:

```shell
python main.py
```

### Splice Videos

Run `splice_videos.py` to cut each video into segments of 59 seconds or less:

```shell
python splice_videos.py
```

## File Descriptions

- `main.py`: Main script to generate videos.
- `accelerate_audio.py`: Speeds up audio files.
- `content_moderation.py`: Replaces trigger words in content.
- `editing.py`: Handles video editing tasks.
- `posts.py`: Retrieves posts from a specified subreddit using PRAW.
- `screenshot_post.py`: Takes screenshots of post titles.
- `tts.py`: Converts text to speech using ElevenLabs API.
- `splice_videos.py`: Slices videos into segments.

## Purpose

This project aims to simplify the creation of "Reddit Story" style videos by automating various tasks, making content creation faster and more efficient for content creators.

---
