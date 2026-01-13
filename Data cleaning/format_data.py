"""
Format text data: trim whitespace
"""
import pandas as pd

def trim_text(file_in, file_out):
    df = pd.read_csv(file_in)
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()
    df.to_csv(file_out, index=False)

# Example usage
# trim_text('data.csv', 'data_trimmed.csv')