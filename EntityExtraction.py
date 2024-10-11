import pytesseract
from PIL import Image
import re
import cv2
import numpy as np

# Define the path to your image
image_path = '/content/00005.jpg'

# Convert image to grayscale
img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply thresholding to preprocess the image
_, img_thresh = cv2.threshold(img_cv, 128, 255, cv2.THRESH_BINARY)

# Convert back to PIL Image for OCR
img_preprocessed = Image.fromarray(img_thresh)

# Extract text using Tesseract OCR
extracted_text = pytesseract.image_to_string(img_preprocessed)

# Print the full extracted text for debugging (optional)
print("Extracted Text After Preprocessing:")
print(extracted_text)

# Regular expression to find weights (e.g., 1400mg, 2kg)
# This pattern matches a number followed by a weight unit
weight_pattern = r'(\d+(\.\d+)?)\s*(mg|g|kg|lb|lbs|oz|pounds?|grams?|kilograms?|milligrams?)'

# Find all matches of weights in the text
weights = re.findall(weight_pattern, extracted_text, re.IGNORECASE)

# Extract the relevant weight strings (numerical part and unit)
extracted_weights = [f"{weight[0]} {weight[2]}" for weight in weights]

# Print only the combined weight strings
if extracted_weights:
    print("\nExtracted Weights:")
    for weight in extracted_weights:
        print(weight)
else:
    print("No weights found.")
