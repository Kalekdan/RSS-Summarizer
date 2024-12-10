from pathlib import Path
import openai
from datetime import datetime

instructions = ('Summarize the following RSS into a daily digest in conversational prose. Output without any markdown '
                'or formatting. Keep it brief and relevant and do not exceed 700 words. You don\'t need to mention '
                'which feed each bit of content is from.')


def today():
    # Get today's date in YYYY-MM-DD format
    return datetime.now().strftime('%Y-%m-%d')  # Format as "2024-12-09"


def summarize(text):
    # Format the messages for OpenAI API
    messages = [{'role': 'system', 'content': instructions + '\n Content: ' + text}]
    # Call the OpenAI API
    response = openai.chat.completions.create(
        # model="gpt-3.5-turbo",
        # model="gpt-4o",
        model="gpt-4o-mini",
        messages=messages,
    )
    summary = response.choices[0].message.content.strip()
    # Create the text file path at the root of the project
    text_file_path = Path("/mnt/media-nfs-rss/Podcasts") / f"{today()}_summary.txt"
    # Save the text summary to the text file
    with open(text_file_path, 'w') as file:
        file.write(summary)

    return summary


def tts(text):
    speech_file_path = Path("/mnt/media-nfs-rss/Podcasts") / f"{today()}_tts.mp3"
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    # Write the audio file locally
    response.stream_to_file(speech_file_path)
