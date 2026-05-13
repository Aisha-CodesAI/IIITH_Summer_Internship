import cv2
import os

# video path
video_path = "video.mp4"

# folder to save frames
output_folder = "frames"

# create folder if not exists
os.makedirs(output_folder, exist_ok=True)

# open video
cap = cv2.VideoCapture(video_path)

frame_count = 0
saved_count = 0

# how many frames to skip (for 10 FPS approx)
skip_frames = 3   # adjust if needed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % skip_frames == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()

print(f"Total frames saved: {saved_count}")