import os
import glob

def count_images_in_folder(folder_path, extensions=['*.jpg', '*.jpeg', '*.png', '*.gif']):
    # Initialize the image count
    image_count = 0

    # Count images for each extension
    for ext in extensions:
        image_count += len(glob.glob(os.path.join(folder_path, ext)))

    return image_count

# Specify the folder path where the images are saved
folder_path = '/content/drive/MyDrive/Amazon ML Challenge/dataset/train_images'

# Call the function to count the number of images in the folder
num_images = count_images_in_folder(folder_path)

# Print the number of images
print(f"Number of images in folder '{folder_path}': {num_images}")
