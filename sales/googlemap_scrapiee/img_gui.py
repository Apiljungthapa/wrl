import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import threading
import img_scrap
import subprocess

# Function to call the search function with inputs from the GUI
def start_scraping():
    shop_name = shop_name_entry.get()

    # Save the input values to a file
    with open("scrape_input.txt", "w") as f:
        f.write(f"{shop_name}\n")

    # Show the message box indicating scraping is in progress
    messagebox.showinfo("Status", "Scraping data...")

    # Start the scraping process in a separate thread
    threading.Thread(target=run_scraping_script, args=(shop_name,)).start()

    return shop_name

def run_scraping_script(shop_name):
    try:
        # Call the scrape_images function from img_scrap
        images = img_scrap.scrape_images(shop_name)
        messagebox.showinfo("Status", f"Scraping completed. {len(images)} images scraped.")
    except Exception as e:
        messagebox.showerror("Status", f"Scraping failed: {e}")

# Function to go back to the previous GUI
def go_back():
    root.destroy()  # Close the current window
    subprocess.run(["python", "inp_gui.py"])  # Run the previous GUI script

# Create the main window
root = tk.Tk()
root.title("Shop Image Scraper")
root.geometry("800x600")
root.configure(bg="lightblue")

# Load the image
image_path = 'new.jpg'
if os.path.exists(image_path):
    img = Image.open(image_path)
    img = img.resize((400, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    # Create and place the image label
    image_label = tk.Label(root, image=img)
    image_label.pack(pady=20)
else:
    tk.Label(root, text="Image not found").pack(pady=20)

# Create and place the "Google Image Scraper" label with background color
title_label = tk.Label(root, text="** Google Image Scraper **", font=("Arial", 25, "bold"), foreground="green", background="lightblue")
title_label.pack(pady=10)
    

# Create a frame for the input fields
input_frame = ttk.Frame(root, padding="20 20 20 20", style="Custom.TFrame")
input_frame.pack(fill=tk.BOTH, expand=True)

# Create and place the shop name input field
shop_name_label = ttk.Label(input_frame, text="Shop Name:", foreground="green", font=("Arial", 18, "bold"), style="Custom.TLabel")
shop_name_label.grid(column=0, row=0, columnspan=2, pady=(10, 0))  # Center the label

shop_name_entry = ttk.Entry(input_frame, width=60, font=("Arial", 14))  # Increase the width of the text field
shop_name_entry.grid(column=0, row=1, columnspan=2, pady=(0, 10))  # Center the text field

# Create and place the scrape button
scrape_button = tk.Button(input_frame, text="Scrape", command=start_scraping, bg="blue", fg="white", font=("Arial", 14), width=12, height=1)  # Increase height
scrape_button.grid(column=0, row=2, columnspan=2, pady=20)  # Center the button

# Create and place the "Go Back" button
go_back_button = tk.Button(root, text="Go Back", command=go_back, bg="red", fg="white", font=("Arial", 14), width=10, height=2)
go_back_button.pack(side=tk.LEFT, padx=10, pady=10)

# Add some padding around the widgets
for child in input_frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

# Style the widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 14), foreground="black")
style.configure("TEntry", font=("Arial", 14), foreground="black")
style.configure("TButton", font=("Arial", 14), padding=10)
style.configure("Custom.TFrame", background="lightblue")  # Set background color for the frame
style.configure("Custom.TLabel", background="lightblue")  # Set background color for the label

# Run the main event loop
root.mainloop()
