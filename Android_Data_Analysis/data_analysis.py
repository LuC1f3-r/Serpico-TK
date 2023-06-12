import os
import datetime
import re
import binascii
import magic
import pandas as pd

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

# Function to perform keyword search


def keyword_search(extracted_data_path):
    print("Performing keyword search...")
    search_term = input("Enter a keyword to search for: ")
    print(extracted_data_path)
    if os.path.isfile(extracted_data_path):
            csvFile = pd.DataFrame()
    print("Keyword search complete.\n")


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

# Main function to call the other functions based on user input


def main():
    extracted_data_path = input("Enter the path to the extracted data: ")
    while True:
        print("\nPlease select an option:")
        print("1. Timeline Analysis")
        print("2. Keyword Search")
        print("3. File Carving")
        print("4. Hex Dump Analysis")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            timeline_analysis(extracted_data_path)
        elif choice == "2":
            keyword_search(extracted_data_path)
        elif choice == "3":
            file_carving(extracted_data_path)
        elif choice == "4":
            hex_dump_analysis(extracted_data_path)
        elif choice == "5":
            break
        else:
            print("Invalid Choice!! Enter the Right Choice:")


if __name__ == "__main__":
    main()
