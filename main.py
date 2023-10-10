import os
import csv
import difflib

# Specified parameters
ROOT_DIR = '/path/to/your/directory'  # Root directory
FILE_NAME_SIMILARITY_RATIO = 0.2  # Filename difference ratio
FILE_SIZE_SIMILARITY_RATIO = 0.05  # File size difference ratio

def get_file_similarity(name1, name2):
    """Calculate the similarity ratio between two filenames"""
    return difflib.SequenceMatcher(None, name1, name2).ratio()

def get_all_files(path):
    """Traverse all files in the specified directory and return their relative paths and sizes"""
    file_info = []
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            size = os.path.getsize(full_path)
            relative_path = os.path.relpath(full_path, ROOT_DIR)
            file_info.append((relative_path, filename, size))
    return file_info

def compare_files(file_info):
    """Compare the file list to find potential duplicates"""
    possible_duplicates = []
    for i in range(len(file_info)):
        for j in range(i+1, len(file_info)):
            _, name1, size1 = file_info[i]
            _, name2, size2 = file_info[j]
            
            name_similarity = get_file_similarity(name1, name2)
            size_difference = abs(size1 - size2) / ((size1 + size2) / 2)
            
            if name_similarity >= 1 - FILE_NAME_SIMILARITY_RATIO and size_difference <= FILE_SIZE_SIMILARITY_RATIO:
                possible_duplicates.append((file_info[i][0], file_info[j][0]))
    return possible_duplicates

def save_to_csv(duplicates):
    """Save potential duplicates to a CSV file"""
    with open('possible_duplicates.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['File 1', 'File 2'])
        for item in duplicates:
            csvwriter.writerow(item)

def main():
    file_info = get_all_files(ROOT_DIR)
    duplicates = compare_files(file_info)
    save_to_csv(duplicates)

if __name__ == '__main__':
    main()
