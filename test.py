import tkinter as tk

def run_gui():
    # Create the GUI window
    window = tk.Tk()
    window.title("Test Gmail Input")

    # Gmail email entry
    tk.Label(window, text="Gmail Address:").grid(row=0, column=0, padx=10, pady=10)
    email_entry = tk.Entry(window, width=40)
    email_entry.grid(row=0, column=1, padx=10, pady=10)

    # Gmail password entry
    tk.Label(window, text="App Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(window, show="*", width=40)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Run button
    run_button = tk.Button(window, text="Run")
    run_button.grid(row=2, column=1, padx=10, pady=20)

    window.mainloop()

if __name__ == "__main__":
    run_gui()
