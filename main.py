from utils.posts import get_posts
from utils.screenshot import screenshot_post
from utils.tts import text_to_speech
from utils.editing import overlay_on_video
from utils.accelerate_audio import speed_up_audio
from utils.content_moderation import replace_trigger_words
from config import SUBREDDIT_NAME


if __name__ == "__main__":
    # Define your subreddit here
    posts = get_posts(SUBREDDIT_NAME)

    # Load already-selected posts from the file into a set
    try:
        with open("processed_posts.txt", "r") as file:
            already_selected = set([line.strip() for line in file])
    except:
        already_selected = set()

    unused_posts = []
    for post in posts:
        # Replace trigger words
        title = replace_trigger_words(post.title)
        body = replace_trigger_words(post.selftext)

        # Print post title and body
        print(
            "---------------------------------------------------------------------------------------"
        )
        print("TITLE: " + title)
        print("BODY: " + body)
        print(
            "---------------------------------------------------------------------------------------"
        )
        decision = input("Add to unused posts? (y/n): ").strip().lower()

        if decision in ["no", "n"]:
            continue  # Skip to the next iteration

        if decision in ["yes", "y"] and str(post) not in already_selected:
            unused_posts.append(post)

    for i, post in enumerate(unused_posts[1:]):
        print(
            "---------------------------------------------------------------------------------------"
        )
        print(
            "---------------------------------------------------------------------------------------"
        )
        print(f"Working on post {i + 1} out of {len(unused_posts)}")
        print(
            "---------------------------------------------------------------------------------------"
        )

        # Taking Screenshot
        screenshot_post(i, post)

        # Replace trigger words
        title = replace_trigger_words(post.title)
        body = replace_trigger_words(post.selftext)

        # Text to speech
        title_audio_path, body_audio_path = text_to_speech(i, title, body)

        sped_up_title_audio = speed_up_audio(title_audio_path)
        speed_up_body_audio = speed_up_audio(body_audio_path)

        # Overlay on video
        overlay_on_video(
            i,
            "background_video/background_video.webm",
            sped_up_title_audio,
            speed_up_body_audio,
            f"title_screenshots/screenshot-{i}.png",
        )

        # Add the new song to the file and the set
        with open("processed_posts.txt", "a") as file:
            file.write(str(post) + "\n")
