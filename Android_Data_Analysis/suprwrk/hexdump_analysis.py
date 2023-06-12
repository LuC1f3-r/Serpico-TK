# import os
# import binascii
# import magic


# # Function to perform hex dump analysis

# def hex_dump_analysis(extracted_data_path):
#     print("Performing hex dump analysis...")
#     file_list = os.listdir(extracted_data_path)
#     for file_name in file_list:
#         file_path = os.path.join(extracted_data_path, file_name)
#         if os.path.isfile(file_path):
#             with open(file_path, "rb") as file:
#                 file_content = file.read()
#                 file_type = magic.from_buffer(file_content)
#                 if "text" in file_type:
#                     hex_dump = binascii.hexlify(file_content).decode("utf-8")
#                     print(f"Hex dump of {file_name}:\n{hex_dump}")
#                 else:
#                     hex_dump = [file_content[i:i+16]
#                                 for i in range(0, len(file_content), 16)]
#                     offset = 0
#                     for line in hex_dump:
#                         hex_offset = format(offset, '08x')
#                         hex_bytes = ' '.join([format(x, '02x') for x in line])
#                         ascii_chars = ''.join(
#                             [chr(x) if 32 <= x <= 126 else '.' for x in line])
#                         print(f"{hex_offset}  {hex_bytes:<48}  {ascii_chars}")
#                         offset += 16
#     print("Hex dump analysis complete.\n")

import os
import binascii
import magic
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to perform hex dump analysis
def hex_dump_analysis(extracted_data_path):
    print("Performing hex dump analysis...")
    file_list = os.listdir(extracted_data_path)
    for file_name in file_list:
        file_path = os.path.join(extracted_data_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                file_content = file.read()
                file_type = magic.from_buffer(file_content)
                if "text" in file_type:
                    hex_dump = binascii.hexlify(file_content).decode("utf-8")
                    print(f"Hex dump of {file_name}:\n{hex_dump}")
                else:
                    hex_dump = [file_content[i:i+16]
                                for i in range(0, len(file_content), 16)]
                    offset = 0
                    for line in hex_dump:
                        hex_offset = format(offset, '08x')
                        hex_bytes = ' '.join([format(x, '02x') for x in line])
                        ascii_chars = ''.join(
                            [chr(x) if 32 <= x <= 126 else '.' for x in line])
                        print(f"{hex_offset}  {hex_bytes:<48}  {ascii_chars}")
                        offset += 16
    print("Hex dump analysis complete.\n")

# Function to handle file selection
def choose_file():
    global file_path, selected_file_label
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file_label.config(text="Selected file: "+file_path)

# Function to perform analysis on selected file
def analyze_file():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "Please select a file first.")
        return
    file_name = os.path.basename(file_path)
    extracted_data_path = os.path.join(os.getcwd(), file_name+"_extracted")
    if not os.path.exists(extracted_data_path):
        messagebox.showerror("Error", "Extracted data directory does not exist.")
        return
    hex_dump_analysis(extracted_data_path)

# Create GUI
root = tk.Tk()
root.title("Hex Dump Analysis")

# Create file selection button and label
select_file_button = tk.Button(root, text="Select File", command=choose_file)
select_file_button.pack(pady=10)
selected_file_label = tk.Label(root, text="No file selected")
selected_file_label.pack()

# Create analyze button
analyze_button = tk.Button(root, text="Analyze File", command=analyze_file)
analyze_button.pack(pady=10)

# Start GUI
root.mainloop()
