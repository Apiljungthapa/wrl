import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os
import threading
import sale

# Function to call the search function with inputs from the GUI
def start_scraping():
    location = location_entry.get()
    store_type = store_type_entry.get()

    # Save the input values to a file
    with open("scrape_input.txt", "w") as f:
        f.write(f"{location}\n")
        f.write(f"{store_type}\n")

    # Show the message box indicating scraping is in progress
    messagebox.showinfo("Status", "Scraping data...")

    # Start the scraping process in a separate thread
    threading.Thread(target=run_scraping_script, args=(location, store_type)).start()
    return location, store_type


def run_scraping_script(location, store_type):
    try:
        sale.scrape(location, store_type)
        # subprocess.run(["python", "sale.py"], check=True)
        messagebox.showinfo("Status", "Scraping completed.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Status", f"Scraping failed: {e}")


# Create the main window
root = tk.Tk()
root.title("Web Scraping GUI")
root.geometry("800x600")

# Load the image
image_path = 'scraping_type.png'
if os.path.exists(image_path):
    img = Image.open(image_path)
    img = img.resize((400, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    # Create and place the image label
    image_label = tk.Label(root, image=img)
    image_label.pack(pady=20)
else:
    tk.Label(root, text="Image not found").pack(pady=20)

# Create a frame for the input fields
input_frame = ttk.Frame(root, padding="20 20 20 20")
input_frame.pack(fill=tk.BOTH, expand=True)

# Create and place the location input field
location_label = ttk.Label(input_frame, text="Location:", foreground="green", font=("Arial", 14, "bold"))
location_label.grid(column=0, row=0, sticky=tk.W, pady=10)
location_entry = ttk.Entry(input_frame, width=50, font=("Arial", 14))
location_entry.grid(column=1, row=0, pady=10)

# Create and place the store type input field
store_type_label = ttk.Label(input_frame, text="Search Keyword:", foreground="blue", font=("Arial", 14, "bold"))
store_type_label.grid(column=0, row=1, sticky=tk.W, pady=10)
store_type_entry = ttk.Entry(input_frame, width=50, font=("Arial", 14))
store_type_entry.grid(column=1, row=1, pady=10)

# Create and place the scrape button
scrape_button = tk.Button(input_frame, text="Scrape", command=start_scraping, bg="blue", fg="white", font=("Arial", 14), width=15, height=2)
scrape_button.grid(column=0, row=2, columnspan=2, pady=20)  # Center the button

# Add some padding around the widgets
for child in input_frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

# Style the widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 14), foreground="black")
style.configure("TEntry", font=("Arial", 14), foreground="black")
style.configure("TButton", font=("Arial", 14), padding=10)

# Run the main event loop
root.mainloop()
