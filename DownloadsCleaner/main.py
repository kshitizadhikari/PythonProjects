# This program automatically sorts the items in your downloads directory and puts them in appropriate directories

import os 
import shutil

def main():
    current_dir = os.getcwd()
    
    source_dir = "test"
    dest_dir = "sortedData"

    # get paths of the directories
    source_path = os.path.join(current_dir, source_dir)
    dest_path = os.path.join(current_dir, dest_dir)

    # create directories if they don't already exist
    if not os.path.exists(source_path):
        os.makedirs(source_dir)

    if not os.path.exists(dest_path):
        os.makedirs(dest_dir)

    # create directories to store files
    new_dirs = ['images', 'documents', 'pdfs', 'others']
    for dir in new_dirs:
        dir_path = os.path.join(dest_path, dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


    for file in os.listdir(source_path):
        if file.split(".")[1] in ['jpg', 'jpeg', 'png', 'gif']:
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_path, "images"))

        elif file.split(".")[1] in ['txt', 'docx',]:
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_path, "documents"))

        elif file.split(".")[1] in ['pdf']:
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_path, "pdfs"))

        else:
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, "others"))

    print("Files moved successfully")

    
if __name__ == '__main__':
    main()