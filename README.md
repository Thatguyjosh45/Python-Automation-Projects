# Python-Automation-Projects

# To-Do List
To-Do List Management:

You can view tasks, add new tasks, or mark tasks as done.
Each task is added with a number, making it easy to identify them.
Reminder Feature:

The script can send you an email reminder every day at a set time (e.g., 9:00 AM).
This will list your tasks or remind you if you don't have any tasks.
Email Sending:

This uses Python’s smtplib to send emails.
Make sure you replace the your_email@example.com, your_password, and smtp.example.com with actual values. You can use services like Gmail or others that support SMTP.

# Automatic File Organizer

File Type Categories:

The file_types dictionary holds different categories like "Images", "Documents", etc. Each category has a list of file extensions associated with it. For example, the "Images" category has .jpg, .png, .gif, and so on.
Organizing Files:

The script checks each file in the downloads_folder.
It checks the file extension and matches it to the appropriate category in the file_types dictionary.
If a match is found, the file is moved to the corresponding folder (e.g., "Images", "Documents").
Folder Creation:

If the folder for a specific category doesn't exist, the script will create it using os.makedirs().
Handling Files without Matching Categories:

If a file doesn't match any of the specified file types, it will be moved to an "Others" folder.
