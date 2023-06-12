from tkinter import *
from tkinter import filedialog
import os
import keyword_analysis
import timeline_analysis
import file_carving
import hexdump_analysis


# Function to open a file dialog box and select the extracted android data
def open_file():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=[("All files", "*.*")])
    # Display the selected file path on the main screen
    selected_file_label.config(text=f"Selected file: {filename}")
    print(f"Opening file: {filename}")


# Create the main window
root = Tk()
root.title("Android Data Analysis")


# Create a label to display the selected file path
selected_file_label = Label(root, text="No file selected", font=("Arial", 12))
selected_file_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


# Create labels for the analysis methods
Label(root, text="Select an analysis method:").grid(row=1, column=0, padx=10, pady=10)
Label(root, text="Keyword analysis").grid(row=2, column=0, padx=10, pady=5, sticky=W)
Label(root, text="Timeline analysis").grid(row=3, column=0, padx=10, pady=5, sticky=W)
Label(root, text="Hex dump analysis").grid(row=4, column=0, padx=10, pady=5, sticky=W)
Label(root, text="File carving").grid(row=5, column=0, padx=10, pady=5, sticky=W)


# Create buttons for the analysis methods
Button(root, text="Select file", command=open_file).grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Perform keyword analysis", command=lambda: keyword_analysis.keyword_search(filename)).grid(row=2, column=1, padx=10, pady=5, sticky=W)
Button(root, text="Perform timeline analysis", command=lambda: timeline_analysis.timeline_analysis(filename)).grid(row=3, column=1, padx=10, pady=5, sticky=W)
Button(root, text="Perform hex dump analysis", command=lambda: hexdump_analysis.hex_dump_analysis(filename)).grid(row=4, column=1, padx=10, pady=5, sticky=W)
Button(root, text="Perform file carving", command=lambda: file_carving.file_carving(filename)).grid(row=5, column=1, padx=10, pady=5, sticky=W)


# Run the main loop
root.mainloop()
