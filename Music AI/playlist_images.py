import openai
import requests
from moviepy.editor import *

openai.api_key = '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'

def transcribe_audio(audio_file):
    with open(audio_file, 'rb') as file:
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=file,
            response_format="text"
        )
    return response

# Example usage
audio_files = [
    r'C:\Users\dell\OneDrive\Bureau\Project3\WhispersintheForest.mp3',
    r'C:\Users\dell\OneDrive\Bureau\Project3\ForestCanvas.mp3',
    r'C:\Users\dell\OneDrive\Bureau\Project3\ChasingtheDawn.mp3',
    r'C:\Users\dell\OneDrive\Bureau\Project3\RiseandShine.mp3'
]

lyrics_list = [transcribe_audio(audio) for audio in audio_files]


def generate_image(prompt, image_path):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    # Download image
    image_data = requests.get(image_url).content
    with open(image_path, 'wb') as handler:
        handler.write(image_data)

# Example usage
for i, lyrics in enumerate(lyrics_list):
    prompt = lyrics  # Using the lyrics as the prompt
    image_path = f'C:\\Users\\dell\\OneDrive\\Bureau\\Project3\\image_{i + 1}.png'
    generate_image(prompt, image_path)

def create_video_with_audio(audio_file, image_files, output_file):
    clips = []
    for image_file in image_files:
        img_clip = ImageClip(image_file).set_duration(10)  # Duration for each image
        clips.append(img_clip)

    video = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(audio_file)
    video = video.set_audio(audio)
    video.write_videofile(output_file, fps=24)

# Example usage
audio_file = r'C:\Users\dell\OneDrive\Bureau\Project3\playlist.mp3'
image_files = [
    r'C:\Users\dell\OneDrive\Bureau\Project3\image_1.png',
    r'C:\Users\dell\OneDrive\Bureau\Project3\image_2.png',
    r'C:\Users\dell\OneDrive\Bureau\Project3\image_3.png',
    r'C:\Users\dell\OneDrive\Bureau\Project3\image_4.png'
]
output_file = r'C:\Users\dell\OneDrive\Bureau\Project3\output_video.mp4'

create_video_with_audio(audio_file, image_files, output_file)

