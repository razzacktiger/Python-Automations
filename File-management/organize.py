import os
import argparse
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

""" 
    Author: Razzacktiger
    With the help of this script, you can sort your files on your desktop based on their file type. 
    Originally coded for MAC OS, but can be used on Windows and Linux as well with minor changes.
    Thanks to Cursor AI for help on this script.
    Enjoy!
"""

class FileHandler(FileSystemEventHandler):
    def __init__(self, file_type, source_destination, source_file, auto_sort):
        self.file_type = file_type
        self.source_destination = source_destination
        self.source_file = source_file
        self.auto_sort = auto_sort
        self.processed_files = set()
        super().__init__()
        
    def on_created(self, event):
        if event.is_directory:
            return None
        elif event.src_path in self.processed_files:
            return None
        else:
            self.processed_files.add(event.src_path)
            self.reorganize_files()
            
    def reorganize_files(self):
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
        source_path = os.path.expanduser(f"~/{self.source_file}")
        
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
                if item.endswith(self.file_type):
                    # Move the file to the specified source destination folder
                    if self.source_destination is not None:
                        if not os.path.exists(os.path.expanduser(f"~/{self.source_file}/{self.source_destination}")):
                            os.makedirs(os.path.expanduser(f"~/{self.source_file}/{self.source_destination}"))
                        os.rename(item_path, os.path.join(
                            os.path.expanduser(f"~/{self.source_file}/{self.source_destination}"), item))
                        print(f"Moved: {item} to {self.source_destination} folder on desktop path \"~/{self.source_file}/{self.source_destination}\" \n")
                    # Move the file to the default folder associated with the file type
                    else:
                        if not os.path.exists(os.path.expanduser(f"~/{self.source_file}/{self.file_type}")):
                            os.makedirs(os.path.expanduser(f"~/{self.source_file}/{self.file_type}"))
                        os.rename(item_path, os.path.join(
                            os.path.expanduser(f"~/{self.source_file}/{self.file_type}"), item))
                        print(f"Moved: {item} to {self.file_type} folder on desktop path \"~/{self.source_file}/{self.file_type}\" \n")
                else:
                    # Auto sort the file based on their extension
                    if self.auto_sort:
                        file_extension = item.split(".")[-1]
                        if not os.path.exists(os.path.expanduser(f"~/{self.source_file}/{file_extension}")):
                            os.makedirs(os.path.expanduser(f"~/{self.source_file}/{file_extension}"))
                        os.rename(item_path, os.path.join(
                            os.path.expanduser(f"~/{self.source_file}/{file_extension}"), item))    
                        print(f"Moved: {item} to {file_extension} folder on desktop path \"~/{self.source_file}/{file_extension}\" \n")
                    # Move remaining files to new folder called "misc"
                    else:
                        if not os.path.exists(os.path.expanduser(f"~/{self.source_file}/misc")):
                            os.makedirs(os.path.expanduser(f"~/{self.source_file}/misc"))
                        os.rename(item_path, os.path.join(
                            os.path.expanduser(f"~/{self.source_file}/misc"), item))    
                        print(f"Moved: {item} to misc folder on desktop path \"~/{self.source_file}/misc\" \n")

def main():
    # Parse the arguments
    parser = argparse.ArgumentParser(description='Sort files on desktop based on their file type.')
    parser.add_argument('file_type', type=str, help='file type to sort')
    parser.add_argument('source_destination', type=str, help='destination folder to move the files to')
    parser.add_argument('source_file', nargs='?', default='Downloads', type=str, help='source folder to sort the files from')
    parser.add_argument('auto_sort', nargs='?', default=True, type=bool, help='whether to automatically sort files based on their extension')
    args = parser.parse_args()
    
    # Create an event handler and an observer to monitor the specified folder
    event_handler = FileHandler(args.file_type, args.source_destination, args.source_file, args.auto_sort)
    observer = Observer()
    observer.schedule(event_handler, os.path.expanduser(f"~/{args.source_file}"), recursive=True)
    observer.start()
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    # Stop the script if the user presses Ctrl+C
    except KeyboardInterrupt:
        observer.stop()
    observer.join() # Wait until the thread terminates

# Run the script
if __name__ == "__main__":
    main()
    

print("Desktop cleanup complete.")


