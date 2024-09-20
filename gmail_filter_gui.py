import imaplib
import email
import keyring
import tkinter as tk
from tkinter import messagebox
from email.header import decode_header

# Function to connect to Gmail's IMAP server
def connect_to_gmail(username, password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        return mail
    except imaplib.IMAP4.error:
        raise Exception("Login failed. Please check your email and App Password.")

# Function to select the inbox
def select_inbox(mail):
    mail.select("inbox")

# Function to search for job-related emails
def search_for_job_emails(mail):
    try:
        status, messages = mail.search(None, '(BODY "job" BODY "application" BODY "interview" BODY "interest" BODY "applying")')
        email_ids = messages[0].split()
        return email_ids
    except Exception as e:
        raise Exception("Failed to search emails.")

# Function to move emails to a new folder
def move_to_folder(mail, email_ids, folder_name):
    try:
        mail.create(folder_name)
        for email_id in email_ids:
            mail.copy(email_id, folder_name)
            mail.store(email_id, '+FLAGS', '\\Deleted')
        mail.expunge()
    except imaplib.IMAP4.error as e:
        raise Exception(f"Error moving emails: {e}")

# GUI to input Gmail credentials and save password
def run_gui():
    def run_script():
        user_email = email_entry.get()
        password = password_entry.get()

        # Store password in keyring if checked
        if save_password_var.get():
            keyring.set_password("gmail_app", user_email, password)

        try:
            # Connect to Gmail
            mail = connect_to_gmail(user_email, password)
            select_inbox(mail)
            job_emails = search_for_job_emails(mail)

            if job_emails:
                move_to_folder(mail, job_emails, "JobApplications")
                messagebox.showinfo("Success", f"Moved {len(job_emails)} job-related emails.")
            else:
                messagebox.showinfo("Info", "No job-related emails found.")

            mail.logout()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_saved_password():
        user_email = email_entry.get()
        stored_password = keyring.get_password("gmail_app", user_email)
        if stored_password:
            password_entry.delete(0, tk.END)
            password_entry.insert(0, stored_password)

    # GUI window
    window = tk.Tk()
    window.title("Gmail Job Email Filter")

    # Gmail email entry
    tk.Label(window, text="Gmail Address:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    email_entry = tk.Entry(window, width=40)
    email_entry.grid(row=0, column=1, padx=10, pady=10)

    # Gmail password entry
    tk.Label(window, text="App Password:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    password_entry = tk.Entry(window, show="*", width=40)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Load saved password button
    load_button = tk.Button(window, text="Load Saved Password", command=load_saved_password)
    load_button.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    # Checkbox to save password
    save_password_var = tk.BooleanVar()
    save_password_check = tk.Checkbutton(window, text="Save Password", variable=save_password_var)
    save_password_check.grid(row=3, column=1, padx=10, pady=5, sticky='w')

    # Run button
    run_button = tk.Button(window, text="Run", command=run_script)
    run_button.grid(row=4, column=1, padx=10, pady=20, sticky='w')

    window.mainloop()

# Run the GUI application
if __name__ == "__main__":
    run_gui()
