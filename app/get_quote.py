import csv
import os

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Define the path to the quotes CSV file
file_path = os.path.join(BASE_DIR, "data", "quotes.csv")

def get_quote():
    quotes = []
    # Open the CSV file containing quotes
    with open(file_path, 'r', newline='', encoding='utf-8') as quotes_file:
        reader = csv.reader(quotes_file)
        # Read each row in the CSV file
        for row in reader:
            # Ensure the row has exactly 2 elements (author and quote)
            if len(row) == 2:
                author, quote = row
                # Append the quote to the list as a dictionary
                quotes.append({'author': author, 'quote': quote})
    # Return the list of quotes
    return quotes