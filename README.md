# Python-Automations
I create Python scripts to benifit myself and others as well as learn on the process.

## Set up and Installation 

### Installation

1. Make sure you have Python installed on your system. You can download it from the official Python website: [python.org](https://www.python.org/downloads/).

2. Clone or download the repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory where you have cloned or downloaded the repository.

4. Install the required dependencies by running the following command:
    `pip install requirments.txt`


## Automations 

### File Organizer

This script allows you to sort files on your desktop based on their file type. It can be used on macOS, Windows, and Linux with minor changes.

### Running the program
+ To run the program cd into the directory `/python-scripts/automation/folder-management/`
  + run the following command: `python3 organize.py [file_type] [file_destination] [source_file] [auto_sort]`
  + `file_type` is the file extension such as ".png" and is of type string.
  + `file_destination` is the file destination folder that the user specifies
  + `source_file` is the source folder that the user wants to put in such as ~`Downloads
  + `auto_sort` is a boolean setting that when set to `True` automatically sorts through any file within the source_file folder and determines the new folder that needs to be created sorting the file accordingly.
+ Examples:
  + run `python3 organize.py .png png Downloads False` when specifying which type of file, where to place it etc.
  + run `python3 organize.py none none Downloads True` when using the auto sort feature.


