import os
import argparse

""" 
    Author: Razzacktiger
    With the help of this script, you can sort your files on your desktop based on their file type. 
    Originally coded for MAC OS, but can be used on Windows and Linux as well with minor changes.
    Thanks to Cursor AI for help on this script.
    Enjoy!
"""

def SortDesktop(file_type, source_destination, source_file, auto_sort):
    """
    Sorts files on the desktop based on their file type.
    If a source destination is specified, the file will be placed there.
    Otherwise, it will be placed in the default folder associated with the file type.
    
    param: file_type: file type to sort
    param: source_destination: destination folder to move the files to
    param: source_file: source folder to sort the files from
    return: None
    """
    # Specify the path to your desktop folder
    source_path = os.path.expanduser(f"~/{source_file}")
    
    # List all files and folders on the desktop
    desktop_contents = os.listdir(source_path)
    
    # Iterate through the files and folders
    for item in desktop_contents:
        item_path = os.path.join(source_path, item)

        # Check if it's a file (not a folder) and not a hidden file
        if os.path.isfile(item_path) and not item.startswith("."):
            # Print the file name
            print(f"File found: {item}")
            # filter the files ending with file_type
            if item.endswith(file_type):
                # Move the file to the specified source destination folder
                if source_destination is not None:
                    if not os.path.exists(os.path.expanduser(f"~/{source_file}/{source_destination}")):
                        os.makedirs(os.path.expanduser(f"~/{source_file}/{source_destination}"))
                    os.rename(item_path, os.path.join(
                        os.path.expanduser(f"~/{source_file}/{source_destination}"), item))
                    print(f"Moved: {item} to {source_destination} folder on desktop path \"~/{source_file}/{source_destination}\" \n")
                # Move the file to the default folder associated with the file type
                else:
                    if not os.path.exists(os.path.expanduser(f"~/{source_file}/{file_type}")):
                        os.makedirs(os.path.expanduser(f"~/{source_file}/{file_type}"))
                    os.rename(item_path, os.path.join(
                        os.path.expanduser(f"~/{source_file}/{file_type}"), item))
                    print(f"Moved: {item} to {file_type} folder on desktop path \"~/{source_file}/{file_type}\" \n")
            else:
                # Auto sort the file based on their extension
                if auto_sort:
                    file_extension = item.split(".")[-1]
                    if not os.path.exists(os.path.expanduser(f"~/{source_file}/{file_extension}")):
                        os.makedirs(os.path.expanduser(f"~/{source_file}/{file_extension}"))
                    os.rename(item_path, os.path.join(
                        os.path.expanduser(f"~/{source_file}/{file_extension}"), item))    
                    print(f"Moved: {item} to {file_extension} folder on desktop path \"~/{source_file}/{file_extension}\" \n")
                # Move remaining files to new folder called "misc"
                else:
                    if not os.path.exists(os.path.expanduser(f"~/{source_file}/misc")):
                        os.makedirs(os.path.expanduser(f"~/{source_file}/misc"))
                    os.rename(item_path, os.path.join(
                        os.path.expanduser(f"~/{source_file}/misc"), item))    
                    print(f"Moved: {item} to misc folder on desktop path \"~/{source_file}/misc\" \n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort files on desktop based on their file type.')
    parser.add_argument('file_type', type=str, help='file type to sort')
    parser.add_argument('source_destination', type=str, help='destination folder to move the files to')
    parser.add_argument('source_file', type=str, help='source folder to sort the files from')
    parser.add_argument('auto_sort', type=bool, help='whether to automatically sort files based on their extension')
    args = parser.parse_args()

    SortDesktop(args.file_type, args.source_destination, args.source_file, args.auto_sort)
    

print("Desktop cleanup complete.")

