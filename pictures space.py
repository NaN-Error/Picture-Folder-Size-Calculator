import os
from tkinter import Tk, filedialog

def select_folder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def calculate_pictures_size(folder):
    total_size = 0
    for root, dirs, files in os.walk(folder):
        # Exclude directories starting with '-'
        dirs[:] = [d for d in dirs if not d.startswith('-')]
        
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
    
    # Convert bytes to gigabytes
    total_size_gb = total_size / (1024 ** 3)
    return total_size_gb

def main():
    folder = select_folder()
    if folder:
        size_in_gb = calculate_pictures_size(folder)
        print(f"Total size of pictures in '{folder}' is {size_in_gb:.2f} GB")

if __name__ == "__main__":
    main()
