import os 
import shutil

def main():
    # Source and destination paths
    source_path = r"C:\Users\adhik\Downloads"
    dest_path = r"C:\Users\adhik\Downloads"

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # Create directories to store files
    new_dirs = ['images', 'documents', 'pdfs', 'others']
    for dir_name in new_dirs:
        dir_path = os.path.join(dest_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Iterate over files in the source directory
    for file in os.listdir(source_path):
        file_path = os.path.join(source_path, file)
        # Check the file extension and move it to the appropriate directory
        if os.path.isfile(file_path):
            file_extension = file.split(".")[-1].lower()
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                shutil.move(file_path, os.path.join(dest_path, "images", file))
            elif file_extension in ['txt', 'docx']:
                shutil.move(file_path, os.path.join(dest_path, "documents", file))
            elif file_extension in ['pdf']:
                shutil.move(file_path, os.path.join(dest_path, "pdfs", file))
            else:
                shutil.move(file_path, os.path.join(dest_path, "others", file))
            print(f"Moved {file} to the appropriate directory.")

    print("Files sorted successfully.")

if __name__ == '__main__':
    main()