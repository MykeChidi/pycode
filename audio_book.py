from gtts import gTTS
import os

def create_audio_book(txt_file, audio_file):
    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File {txt_file} not found.")
        return

    tts = gTTS(text=text, lang='en')
    tts.save(audio_file)
    print(f"Audiobook saved as {audio_file}")

def main():
    txt_file = 'C:\\Users\\hp\\Documents\\requirements.txt'
    audio_file = 'C:\\Users\\hp\\Documents\\audio.mp3'

    create_audio_book(txt_file, audio_file)
    os.system(f"start {audio_file}")

if __name__ == "__main__":
    main()
