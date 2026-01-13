"""
Simple error handling example
"""
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Example usage
# print(safe_divide(10, 0))