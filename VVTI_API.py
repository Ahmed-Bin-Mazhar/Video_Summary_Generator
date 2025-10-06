from fastapi import FastAPI, UploadFile, Form
import shutil
import tempfile
import os

app = FastAPI()

@app.post("/process_video/")
async def process_video(video: UploadFile = None, url: str = Form(None)):
    # Save uploaded file or download from URL
    if video:
        temp_video_path = f"temp_{video.filename}"
        with open(temp_video_path, "wb") as f:
            shutil.copyfileobj(video.file, f)
    elif url:
        import requests
        temp_video_path = "temp_video.mp4"
        r = requests.get(url, stream=True)
        with open(temp_video_path, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    else:
        return {"error": "Provide either a video file or URL"}

    # Extract frames
    frames = extract_frames(temp_video_path, interval=2)

    # OCR
    image_texts = extract_text_from_images(frames)

    # Speech-to-text
    audio_text = extract_audio_to_text(temp_video_path)

    # Clean up
    os.remove(temp_video_path)

    return {
        "audio_text": audio_text,
        "frames_with_text": image_texts
    }
