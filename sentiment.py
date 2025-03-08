import cv2
from deepface import DeepFace
import os

# Correct image path
image_path = "C:\\22701A3330\\e.jpg"

# Check if file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at {image_path}")

# Load image with OpenCV
img = cv2.imread(image_path)

# Check if image loaded correctly
if img is None:
    raise ValueError("Error: Image could not be loaded. Check file format and path.")

# Perform sentiment analysis
result = DeepFace.analyze(img, actions=['emotion'])

# Extract dominant emotion
dominant_emotion = result[0]['dominant_emotion'].capitalize()

# Display the emotion as a simple message
print(f"Detected Emotion: {dominant_emotion}")