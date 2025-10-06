import cv2
import os

def extract_frames(video_path, output_dir="frames", interval=2):
    os.makedirs(output_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval)
    count, saved = 0, 0

    while True:
        success, frame = vidcap.read()
        if not success:
            break
        if count % frame_interval == 0:
            frame_path = os.path.join(output_dir, f"frame_{saved}.jpg")
            cv2.imwrite(frame_path, frame)
            saved += 1
        count += 1
    vidcap.release()
    return [os.path.join(output_dir, f) for f in os.listdir(output_dir)]
