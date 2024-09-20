# Gmail Job Email Filter Script with GUI

This Python script allows you to filter job-related emails from your Gmail inbox and move them to a specified folder using a simple GUI. It uses `Tkinter` for the graphical interface and securely stores your Gmail App Password using `keyring`.

## Prerequisites

Before running this script, ensure you have the following:

1. **Python 3.** Ensure Python 3.x is installed.
2. **Tcl-Tk 8.6 or higher.** This is required for the GUI to work properly.
3. **Gmail App Password.** You must have 2-Step Verification enabled on your Gmail account and generate an App Password to use with this script.

### Steps to Enable Gmail App Password:

1. Enable **2-Step Verification** on your Gmail account.
2. Generate an **App Password** for accessing your Gmail through this script:
   - Go to your Google Account -> Security -> App Passwords.
   - Generate a password for "Mail" on a "Custom device" (e.g., name it "Python Script").

## Installation

1. **Clone or Download the Repository.**
2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Intsall Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Script**
To start the GUI and run the script, execute the following command:

    ```bash
    python gmail_filter_gui.py
    ```


GUI Instructions:
Enter Gmail Address: Enter the Gmail address you want to filter.
Enter Gmail App Password: Enter the Gmail App Password you generated.
Save Password: You can check this option to securely save the password in your system’s keyring.
Load Saved Password: This will load any previously saved passwords from your system keyring.
Run: This will search your inbox for job-related emails and move them to a folder called "JobApplications."
