# import os
# import datetime

# # Function to perform timeline analysis and plot results in a graph

# def timeline_analysis(extracted_data_path):
#     print("Performing timeline analysis...")
#     file_list = os.listdir(extracted_data_path)
#     mod_times = []
#     for file_name in file_list:
#         file_path = os.path.join(extracted_data_path, file_name)
#         mod_time = os.path.getmtime(file_path)
#         mod_times.append(mod_time)
#     mod_times.sort()
#     timestamps = [datetime.datetime.fromtimestamp(
#         mod_time) for mod_time in mod_times]
#     plot_timeline(timestamps)
#     print("Timeline analysis complete.\n")

# # Function to plot timeline graph

# def plot_timeline(timestamps):
#     import matplotlib.pyplot as plt
#     plt.plot(timestamps, [1]*len(timestamps), "|", color='blue', markersize=15)
#     plt.ylim(0, 2)
#     plt.title("Timeline Analysis")
#     plt.xlabel("Timestamps")
#     plt.yticks([])
#     plt.show()

import os
import datetime
import tkinter as tk
from tkinter import filedialog

# Function to perform timeline analysis and plot results in a graph

def timeline_analysis(extracted_data_path):
    print("Performing timeline analysis...")
    file_list = os.listdir(extracted_data_path)
    mod_times = []
    for file_name in file_list:
        file_path = os.path.join(extracted_data_path, file_name)
        mod_time = os.path.getmtime(file_path)
        mod_times.append(mod_time)
    mod_times.sort()
    timestamps = [datetime.datetime.fromtimestamp(
        mod_time) for mod_time in mod_times]
    plot_timeline(timestamps)
    print("Timeline analysis complete.\n")

# Function to plot timeline graph

def plot_timeline(timestamps):
    import matplotlib.pyplot as plt
    plt.plot(timestamps, [1]*len(timestamps), "|", color='blue', markersize=15)
    plt.ylim(0, 2)
    plt.title("Timeline Analysis")
    plt.xlabel("Timestamps")
    plt.yticks([])
    plt.show()

# Function to choose a file

def choose_file():
    global selected_file_label
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file_label.config(text="Selected file: "+file_path)
        timeline_analysis(file_path)
    else:
        selected_file_label.config(text="No file selected")

# Create GUI

root = tk.Tk()
root.title("Timeline Analysis Tool")

select_file_button = tk.Button(root, text="Select File", command=choose_file)
select_file_button.pack(pady=10)

selected_file_label = tk.Label(root, text="No file selected")
selected_file_label.pack()

root.mainloop()
