# import os
# import re

# # Function to perform keyword search


# def keyword_search(extracted_data_path):
#     print("Performing keyword search...")
#     search_term = input("Enter a keyword to search for: ")
#     directory_path = os.path.dirname(filename)
#     file_list = os.listdir(directory_path)
#     for file_name in file_list:
#         filename = os.path.join(extracted_data_path, file_name)
#         if os.path.isfile(filename):
#             with open(filename, "r", encoding='utf8', errors='ignore') as file:
#                 line_num = 0
#                 for line in file:
#                     line_num += 1
#                     if re.search(search_term, line, re.IGNORECASE):
#                         print(
#                             f"{search_term} found in {file_name} at line {line_num}")
#     print("Keyword search complete.\n")

import os
import re
import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import filedialog

# Function to perform keyword search
def keyword_search():
    # Get the path of the file to search
    filename = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
    if not filename:
        return
    selected_file_label.config(text=f"Selected file: {filename}")

    # Get the search terms from the user
    # search_term_label.config(text="Enter the keywords to search for separated by commas:")
    search_term_entry.delete(0, tk.END)
    search_term_entry.focus()

    def search():
        search_terms_str = search_term_entry.get().strip()
        if not search_terms_str:
            return
        search_terms = [term.strip() for term in search_terms_str.split(',')]
        if not search_terms:
            return
        count = 0
        index = 0

        search_counts = {term: 0 for term in search_terms}
        if os.path.isfile(filename):
                csvFile = pd.read_excel(filename)
                arrayValues = csvFile.values
                for line in arrayValues:
                    line = np.array_str(line)
                    result = line.find(search_terms_str)
                    index = index+1
                    if result != -1:
                        count = count+1
                        csvFileName = os.path.basename(filename).split('/')[-1]
                        output_text.insert(tk.END, f"{search_terms_str} found {count} time(s) in {csvFileName} at index {index}\n")
        output_text.insert(tk.END, f"Total {search_terms_str} count: {count}\n")
        output_text.insert(tk.END, "Keyword search complete.\n")

    # Clear previous search results
    output_text.delete("1.0", tk.END)

    # Create search button
    search_button = tk.Button(root, text="Search", command=search)
    output_text.window_create("end", window=search_button)
    output_text.insert(tk.END, "\n")


# Create GUI
root = tk.Tk()
root.title("Keyword Analysis")

# Create widgets
select_file_button = tk.Button(root, text="Select file", command=keyword_search)
selected_file_label = tk.Label(root, text="")
search_term_label = tk.Label(root, text="Enter the keywords to search for:")
search_term_entry = tk.Entry(root)
output_text = tk.Text(root)

# Pack widgets
select_file_button.pack(pady=10)
selected_file_label.pack(pady=5)
search_term_label.pack()
search_term_entry.pack(pady=5)
output_text.pack(pady=10)

root.mainloop()
