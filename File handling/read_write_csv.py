"""
Read a CSV and print content
"""
import csv

def read_csv(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Example usage
# read_csv('data.csv')
