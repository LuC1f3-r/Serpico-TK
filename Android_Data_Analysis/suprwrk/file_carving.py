# import os
# import magic

# #Perfrom File Carving

# def file_carving(extracted_data_path):
#     print("Performing file carving...")
#     file_list = os.listdir(extracted_data_path)
#     file_signatures = {
#         b"\xff\xd8\xff\xe0": "JPEG Image",
#         b"\x89\x50\x4e\x47": "PNG Image",
#         b"\x47\x49\x46\x38": "GIF Image",
#         b"\x49\x49\x2a\x00": "TIFF Image",
#         b"\x42\x4d": "BMP Image",
#         b"\x25\x50\x44\x46": "PDF Document",
#         b"\x7b\x5c\x72\x74": "RTF Document",
#         b"\x50\x4b\x03\x04": "ZIP Archive",
#         b"\x7f\x45\x4c\x46": "ELF Executable",
#         b"\xca\xfe\xba\xbe": "Mach-O Executable",
#         b"\x25\x21\x50\x53": "PostScript Document",
#         b"\x66\x6f\x72\x6d\x61\x74": "Text Document"
#     }
#     for file_name in file_list:
#         file_path = os.path.join(extracted_data_path, file_name)
#         if os.path.isfile(file_path):
#             with open(file_path, "rb") as file:
#                 file_content = file.read()
#                 file_type = magic.from_buffer(file_content)
#                 for signature in file_signatures:
#                     if signature in file_content:
#                         file_extension = "." + \
#                             file_signatures[signature].lower().replace(
#                                 " ", "_")
#                         with open(file_name + file_extension, "wb") as new_file:
#                             new_file.write(file_content)
#                             print(
#                                 f"{file_name} carved as {file_name + file_extension}")
#                         break
#                 else:
#                     if "image" in file_type:
#                         file_signature = b"\xff\xd8\xff"
#                         file_offset = file_content.find(file_signature)
#                         if file_offset != -1:
#                             file_extension = magic.from_buffer(
#                                 file_content[file_offset:]).split(",")[0].split()[1]
#                             new_file_name = file_name + "." + file_extension
#                             with open(new_file_name, "wb") as new_file:
#                                 new_file.write(file_content[file_offset:])
#                                 print(f"{file_name} carved as {new_file_name}")
#                     elif "Microsoft Excel" in file_type:
#                         file_signature = b"\x50\x4b\x03\x04"
#                         file_offset = file_content.find(file_signature)
#                         if file_offset != -1:
#                             with open(file_name + ".xlsx", "wb") as new_file:
#                                 new_file.write(file_content[file_offset:])
#                                 print(
#                                     f"{file_name} carved as {file_name + '.xlsx'}")
#                     elif "Text" in file_type:
#                         with open(file_name + ".txt", "wb") as new_file:
#                             new_file.write(file_content)
#                             print(f"{file_name} carved as {file_name + '.txt'}")
#     print("File carving complete.\n")

import os
import magic
import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.title("File Carving")

# Create a function to handle the "Browse" button click event
def browse_files():
    file_path = filedialog.askdirectory()
    extract_button.config(state=tk.NORMAL)
    file_path_label.config(text=file_path)

# Create a function to handle the "Extract" button click event
def extract_files():
    extracted_data_path = file_path_label.cget("text")
    file_carving(extracted_data_path)
    extract_button.config(state=tk.DISABLED)
    file_path_label.config(text="Extraction complete.")

# Create a function to perform file carving
def file_carving(extracted_data_path):
    print("Performing file carving...")
    file_list = os.listdir(extracted_data_path)
    file_signatures = {
        b"\xff\xd8\xff\xe0": "JPEG Image",
        b"\x89\x50\x4e\x47": "PNG Image",
        b"\x47\x49\x46\x38": "GIF Image",
        b"\x49\x49\x2a\x00": "TIFF Image",
        b"\x42\x4d": "BMP Image",
        b"\x25\x50\x44\x46": "PDF Document",
        b"\x7b\x5c\x72\x74": "RTF Document",
        b"\x50\x4b\x03\x04": "ZIP Archive",
        b"\x7f\x45\x4c\x46": "ELF Executable",
        b"\xca\xfe\xba\xbe": "Mach-O Executable",
        b"\x25\x21\x50\x53": "PostScript Document",
        b"\x66\x6f\x72\x6d\x61\x74": "Text Document"
    }
    for file_name in file_list:
        file_path = os.path.join(extracted_data_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                file_content = file.read()
                file_type = magic.from_buffer(file_content)
                for signature in file_signatures:
                    if signature in file_content:
                        file_extension = "." + \
                            file_signatures[signature].lower().replace(
                                " ", "_")
                        with open(file_name + file_extension, "wb") as new_file:
                            new_file.write(file_content)
                            print(
                                f"{file_name} carved as {file_name + file_extension}")
                        break
                else:
                    if "image" in file_type:
                        file_signature = b"\xff\xd8\xff"
                        file_offset = file_content.find(file_signature)
                        if file_offset != -1:
                            file_extension = magic.from_buffer(
                                file_content[file_offset:]).split(",")[0].split()[1]
                            new_file_name = file_name + "." + file_extension
                            with open(new_file_name, "wb") as new_file:
                                new_file.write(file_content[file_offset:])
                                print(f"{file_name} carved as {new_file_name}")
                    elif "Microsoft Excel" in file_type:
                        file_signature = b"\x50\x4b\x03\x04"
                        file_offset = file_content.find(file_signature)
                        if file_offset != -1:
                            with open(file_name + ".xlsx", "wb") as new_file:
                                new_file.write(file_content[file_offset:])
                                print(
                                    f"{file_name} carved as {file_name + '.xlsx'}")
                    elif "Text" in file_type:
                        with open(file_name + ".txt", "wb") as new_file:
                            new_file.write(file_content)
                            print(f"{file_name} carved as {file_name + '.txt'}")
    print("File carving complete.\n")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.extracted_data_path = ""
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_dir_button = tk.Button(self)
        self.select_dir_button["text"] = "Select Extracted Data Directory"
        self.select_dir_button["command"] = self.select_extracted_data_path
        self.select_dir_button.pack(side="top")

        self.carve_button = tk.Button(self)
        self.carve_button["text"] = "Carve Files"
        self.carve_button["state"] = "disabled"
        self.carve_button["command"] = self.perform_carving
        self.carve_button.pack(side="top")

        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def select_extracted_data_path(self):
        self.extracted_data_path = filedialog.askdirectory()
        if self.extracted_data_path:
            self.carve_button["state"] = "normal"

    def perform_carving(self):
        file_carving(self.extracted_data_path)
        self.carve_button["state"] = "disabled"
        self.extracted_data_path = ""
        tk.messagebox.showinfo(
            title="File Carving Complete", message="File carving complete.")

        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
