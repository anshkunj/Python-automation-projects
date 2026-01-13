"""
Sort files in a folder by name
"""
import os

def sort_files(folder):
    files = sorted(os.listdir(folder))
    return files

# Example usage
# print(sort_files('my_folder'))