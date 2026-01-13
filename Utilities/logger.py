"""
Log messages to a file
"""
def log_message(msg, file='log.txt'):
    with open(file, 'a') as f:
        f.write(msg + '\n')

# Example usage
# log_message("Task completed")