# CODEALPHA-TASK-3---FILE-ORGANIZER


#### Overview
The File Organization Automation tool is a Python script designed to automate the process of organizing files within a system. It categorizes files based on their type (e.g., images, documents, videos) and moves them to predefined folders. This project demonstrates the power of Python scripting in automating repetitive tasks, saving time, and improving system organization.

#### Features
1. File Categorization: Automatically sorts files into folders like Images, Documents, Videos, Audio, etc., based on file extensions.  
2. User-Friendly Interface: The tool uses Streamlit for a simple, intuitive web interface where users can select the directory to organize.  
3. Batch Processing: Handles multiple files at once, efficiently organizing large directories.  
4. Logging: Keeps a log of organized files, making it easier to track the actions taken by the script.  
5. Customizable: Users can modify the folder structure and file categorization criteria as per their needs.



#### How It Works  
1. Directory Selection: The user inputs the directory where the files are located.  
2. File Categorization: The script identifies file extensions and moves them to the appropriate folder (e.g., `.jpg` and `.png` files go to the "Images" folder).  
3. Log Generation: A log is created for each run, showing which files were organized and where they were moved.  
4. Output: Once executed, the files are neatly categorized into the designated folders, making file management simpler.  



#### Educational Benefits
This project helps learners:  
- Python Scripting: Learn how to automate file management tasks using Python.  
- Streamlit Framework: Implement a user interface for interacting with scripts, even without prior web development knowledge.  
- File Handling: Gain practical experience with Python's `os` and `shutil` libraries for file manipulation.  
- System Automation: Understand the concept of automating repetitive tasks to improve productivity.  



#### Future Enhancements
- Add advanced file filtering based on file metadata (e.g., file size, date modified).  
- Integrate with cloud storage platforms like Google Drive or Dropbox for remote file organization.  
- Add a preview feature to allow users to see the files that will be moved before the action is performed.  
- Implement error handling for unsupported file types or files with no extension.  



#### How to Run the Program  
1. Clone or download this repository.  
2. Launch the application with:  
   ```bash
   streamlit run file_org.py
   ```  
3. Follow the user-friendly prompts to start organizing your files.
<br>
S JAIGANESH
<br>
LINKEDIN PROFILE: https://www.linkedin.com/in/jaiganeshs539/

