# Reddit Post Generator

This script is designed to automatically process posts from the Reddit subreddit "AITAH" (or any subreddit you define). It takes posts, converts their content to speech, takes a screenshot of the post title, and overlays these elements on a background video.

## Modules:

1. `utils.posts`: This module is used to fetch posts from the specified subreddit.
2. `utils.screenshot`: Allows for taking screenshots of individual Reddit posts.
3. `utils.tts`: Contains the `text_to_speech` function which converts post content to audio.
4. `utils.editing`: The module that handles video overlay.
5. `utils.accelerate_audio`: Speeds up the generated audio to fit the video duration.

## Workflow:

1. Fetches posts from the specified subreddit.
2. Loads posts that have already been processed to avoid duplicates.
3. For each unused post:
   1. Takes a screenshot of the post.
   2. Converts the post title and content into speech (audio).
   3. Speeds up the audio.
   4. Overlays the audio and screenshot on a background video.
   5. Logs the processed post to avoid re-processing in future runs.

## Usage:

Simply run the script:

```
python <script_name>.py
```

## Note:

- The script uses a file named `processed_posts.txt` to keep track of posts that have already been processed.
- If a post fails at any stage in the pipeline, it is logged to the `processed_posts.txt` file to skip it in future runs. This ensures the script is resilient to occasional post-specific issues.
- The background video path is hardcoded as `background_video/background_video.webm`. You may need to update this path if your background video is located elsewhere or has a different name.

**Please ensure you have the necessary modules installed and the Reddit API credentials set up before running the script.**
