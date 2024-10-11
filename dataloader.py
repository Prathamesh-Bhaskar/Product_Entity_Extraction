import cv2
import pytesseract
from PIL import Image
import os
from google.colab import files

# Configure pytesseract (No need for tesseract path in Colab as it's pre-installed)
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def upload_and_extract_text():
    # Upload image
    uploaded = files.upload()

    for filename in uploaded.keys():
        # Save uploaded file
        file_path = os.path.join('/content', filename)

        # OCR to extract text
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        extracted_text = pytesseract.image_to_string(img)

        # Print extracted text
        print("Extracted Text:")
        print("-------------------------")
        print(extracted_text)

        # Optionally, remove the uploaded image after processing
        os.remove(file_path)

# Call the function to upload image and extract text
upload_and_extract_text()
