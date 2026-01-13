"""
Read Excel, remove empty rows
"""
import pandas as pd

def clean_excel(file_in, file_out):
    df = pd.read_excel(file_in)
    df.dropna(how='all', inplace=True)
    df.to_excel(file_out, index=False)

# Example usage
# clean_excel('data.xlsx', 'data_clean.xlsx')
