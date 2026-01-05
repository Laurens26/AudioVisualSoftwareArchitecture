import os
import cv2
from glob import glob

# Input directory
input_dir = r"E:\Masterarbeit_Sillekens\Unity Projects\VisualSimulationUnity_Experiments\Scenario4\video\distorted_annotated"

# Only take RGB camera frames
pattern = os.path.join(input_dir, "RGBCamera_Distorted_Annotated_*.png")
image_paths = sorted(glob(pattern))

if not image_paths:
    raise RuntimeError("No RGBCamera_Distorted_Annotated PNG files found.")

# Read first image to get resolution
first_img = cv2.imread(image_paths[0])
height, width, _ = first_img.shape

# Extract last timestamp from filename for video length
last_filename = os.path.basename(image_paths[-1])
video_length = last_filename.replace("RGBCamera_Distorted_Annotated_", "").replace(".png", "")

# Output video path
output_path = os.path.join(
    input_dir,
    f"Video_RGBCamera_Distorted_Annotated_{video_length}.mp4"
)

# Frames per second (0.1 sec steps -> 10 FPS)
fps = 10

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Write frames to video
for img_path in image_paths:
    img = cv2.imread(img_path)
    if img is None:
        raise RuntimeError(f"Could not read image: {img_path}")
    video_writer.write(img)

video_writer.release()

print("✅ Video successfully created:")
print(output_path)
