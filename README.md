
# Amazon ML Challenge OCR and Data Extraction Project

This project aims to extract relevant information, particularly weight and other entities like dimensions and voltage, from product images using Optical Character Recognition (OCR) techniques. It leverages Google Colaboratory for its ease of use and access to powerful libraries for image processing and OCR.

## Project Structure

The project is structured as follows:

1. **Google Drive Integration:** Mounts Google Drive to store and access the dataset and processed data.
2. **Image Download:** Downloads images from the provided dataset using multiprocessing for efficient download.
3. **Image Preprocessing:** Utilizes OpenCV for image preprocessing techniques like resizing, thresholding, and skew correction to enhance OCR accuracy.
4. **OCR Extraction:** Leverages Tesseract OCR to extract text from the preprocessed images.
5. **Entity Extraction:** Implements regular expressions to identify and extract specific entities like weights, dimensions, voltage, and wattage.

## Dependencies

- OpenCV (cv2)
- PyTesseract
- PIL (Pillow)
- Pandas
- Multiprocessing
- TQDM
- NumPy
- Pathlib
- urllib

## How to Use

1. **Mount Google Drive:** Execute the initial cell for mounting your Google Drive to store the dataset.
2. **Dataset Download:** Configure the dataset path and execute the cell to download images.
3. **Image Preprocessing:** The provided code already contains a preprocessing function. Modify and enhance it according to your needs.
4. **OCR & Entity Extraction:** Execute the relevant code to perform OCR and extract the desired entities.
5. **Analysis and Further Development:** Explore the extracted data, analyze the results, and further develop the project by adding more powerful OCR models or improving entity extraction methods.

## Future Work

- Investigate techniques to improve OCR accuracy, including fine-tuning Tesseract or using advanced OCR models.
- Develop more robust entity extraction techniques that can handle variations in text format and units.
- Explore techniques to detect and extract object boundaries or other visual cues to refine the overall data extraction process.
- Apply machine learning or deep learning models to automatically classify product types or extract specific product attributes.
- Create a user-friendly interface to allow for easy uploading of images and automatic information extraction.

## Acknowledgements

- Tesseract OCR engine
- Google Colaboratory platform
- Pandas for data manipulation

##Project is open for PRs and open source contributions
