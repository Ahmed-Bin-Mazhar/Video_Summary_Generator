import moviepy.editor as mp
import speech_recognition as sr

def extract_audio_to_text(video_path):
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile("temp.wav", verbose=False, logger=None)

    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
