# IIITH_Summer_Internship
# Week 1 — Video Frame Extraction

---

## Task 1 — Extract Frames from Video

- Downloaded a YouTube video using yt-dlp

- Extracted multiple frames using ffmpeg

- [Source YouTube Video](https://youtu.be/_Rsonk1OCG4)

---

## Task 2 — 1800 Frames & Reconstruction

- Extracted 1800 frames at 30fps from 1 minute of video

- Reconstructed frames back into a 1 minute video using ffmpeg

- Reconstructed Video
https://drive.google.com/file/d/1mUDheiTn7wG2cQrHk0DHSMPWbo4SFZrG/view?usp=drivesdk

## Task 3 — Add Music

- Downloaded royalty-free music from Pixabay

- Clipped to 1 minute using Audacity

- Merged audio with video using ffmpeg

- Final Video with Music
  https://drive.google.com/file/d/10Aj0Yx2f4m8txclqmcgjEv1VEAMoXeGI/view?usp=drivesdk


  # Week 2 — Object Detection

---
video link:https://youtu.be/tFZWNHJPAqI?si=LYszypLowDCXm6vD
## Tasks 1, 2, 3

- Created Python virtual environment using venv

- Installed Ultralytics package

- Ran YOLOv8 pretrained object detection model

- Performed object detection on images and videos

- Generated prediction outputs with bounding boxes

- Tested detection accuracy on different objects

- Object Detection
  https://drive.google.com/file/d/10PeLHC0yEGYbgQJ6Qdb3gzbrpIshO8Ih/view?usp=drivesdk
  https://drive.google.com/file/d/1gDFjwzu0RnY0UuAsazBcVkaWfjLr78zl/view?usp=drivesdk


  # Week 3 — Segmentation

---

## Task 1 — Semantic Segmentation

- Ran YOLOv8 segmentation on animal images

- Each object segmented with unique colored pixel mask

- Stitched segmented frames back into video format

- Evaluated segmentation model performance

### Performance Metrics

- Precision: ~0.74

- Recall: ~0.60

- mAP50: ~0.68

- mAP50-95: ~0.47

- [YouTube Video](https://youtu.be/lfYYtQ1Ah04?si=SqLSZLY2y5KkHDRh)
  https://drive.google.com/drive/folders/1ifW5ELlpDTdIGXTBoyI6fbHx41hx0jWd

---

## Task 2 — Stacked Video (Raw + Detected + Segmented)

- Created 3 videos: Raw, Object Detected, Object Segmented

- Ensured all videos same dimensions (1280x720)

- Stacked all 3 vertically using ffmpeg vstack

- Removed original audio with -an option

- Final Stacked Video
https://drive.google.com/file/d/1pyG3Oo-hsyv7RC9cIwXlIMQSGhj-PBG4/view?usp=drivesdk
---

## Tools Used

- yt-dlp — YouTube video downloader

- ffmpeg — Video processing

- YOLOv8 (Ultralytics) — Object detection & segmentation

- Python, OpenCV

- Google Colab

# Week 4 — YOLO Dataset Configuration & Labeling

---

## Task 1 — YOLO Configuration Files Report

Explored the directory/file structures and meta configuration files used in YOLOv8 models.

- Full Report
https://drive.google.com/file/d/11dcuJ1GviaUQPA8tdXM1g3DAfuEUSAmt/view?usp=drivesdk
---

## Task 2 — Label Studio Setup & Custom Dataset Creation

Object detected: Bus / Car / Truck

Video source:  
https://youtu.be/JmFjluIOGJw

Task: Object Detection

Tool: Label Studio

Classes:
- Bus
- Car
- Truck

(Total classes = 3)

---

## Steps Completed:

- Created separate virtual environment for Label Studio using Python 3.11

- Installed Label Studio via pip

- Downloaded highway traffic footage using yt-dlp

- Extracted frames using ffmpeg

- Organized dataset into train, val, and test folders

- Synced images to Label Studio using Local File Storage

- Created Vehicle Detection project with bus, car, and truck classes

- Manually annotated bounding boxes on images

- Exported labels in YOLO format

- Created `data.yaml`, `train.txt`, `val.txt` metadata files

- Trained YOLOv8n on custom labeled dataset

---

## Dataset Details:

| Property | Value |
|---|---|
| Train Images | 100 |
| Validation Images | 40 |
| Test Images | 362 |
| Classes | Bus, Car, Truck |
| Label Format | YOLO (normalized bbox) |

---

## Training Run — Vehicle Detection Dataset

| Metric | Value |
|---|---|
| Precision | 0.91 |
| Recall | 0.67 |
| mAP@50 | 0.82 |
| mAP@50:95 | 0.58 |
| Epochs | 10 |
| Training Time | 0.28 hours |

---

## Metadata Files:

- `data.yaml` — dataset configuration

- `train.txt` — paths to all training images

- `val.txt` — paths to all validation images

- `labels/train/` — YOLO format annotation files

- `labels/val/` — YOLO format annotation files

---

## Tools Used:

- Label Studio — image annotation

- yt-dlp — video download

- ffmpeg — frame extraction

- YOLOv8n (Ultralytics) — object detection training

- Python 3.11 — scripting
