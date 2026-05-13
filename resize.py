from PIL import Image
import os

folders = [
    "dataset/images/train",
    "dataset/images/val"
]

for folder in folders:
    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        # Skip folders
        if not os.path.isfile(path):
            continue

        # Open image
        img = Image.open(path)

        width = 384
        ratio = width / img.width
        height = int(img.height * ratio)

        resized = img.resize((width, height))

        resized.save(path)

print("All images resized!")