# Assuming you have already imported the required libraries and functions

# Read the CSV file
train_df = pd.read_csv('/content/drive/MyDrive/dataset/train.csv')

# Generate the filename mapping (image links and filenames)
image_links, filenames = generate_filename_mapping(train_df)

# Download all images from the dataset
download_images(image_links, filenames, '/content/drive/MyDrive/Amazon ML Challenge/dataset/train_images', allow_multiprocessing=True)
