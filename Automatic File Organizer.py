import os
import shutil

# Define the source (Downloads folder) and destination (organized folders)
downloads_folder = "/path/to/your/Downloads"  # Replace with the actual path
destination_folder = "/path/to/your/OrganizedFiles"  # Replace with your desired destination

# Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Others": []  # Any files that don't match these types will go here
}

# Function to create folders if they don't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to organize files by type
def organize_files():
    # Check if the Downloads folder exists
    if not os.path.exists(downloads_folder):
        print("The specified Downloads folder doesn't exist!")
        return

    # Loop through files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Skip directories, only process files
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Determine the category based on the file extension
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                # Create the category folder if it doesn't exist
                category_folder = os.path.join(destination_folder, category)
                create_folder(category_folder)

                # Move the file to the corresponding folder
                destination_path = os.path.join(category_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {category}")
                moved = True
                break
        
        # If no category matches, move the file to 'Others'
        if not moved:
            others_folder = os.path.join(destination_folder, "Others")
            create_folder(others_folder)
            destination_path = os.path.join(others_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to Others")

# Run the organizer
organize_files()
