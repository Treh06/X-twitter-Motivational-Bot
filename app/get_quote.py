import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "quotes.csv")


def get_quote():
    quotes = []
    with open(file_path, 'r', newline='', encoding='utf-8') as quotes_file:
        reader = csv.reader(quotes_file)
        for row in reader:
            if len(row) == 2:
                author, quote = row
                quotes.append({'author': author, 'quote': quote})
    return quotes