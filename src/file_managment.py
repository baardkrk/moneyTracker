from src.transaction import Transaction
from src.category import Category
from src.category_collection import CategoryCollection
import csv
import datetime
import json


def load_transactions(filepath):
    leading_rows = 3

    with open(filepath, newline='', encoding='latin-1') as csvfile:
        transaction_reader = csv.reader(csvfile, delimiter=";")
        transactions = []

        for i in range(leading_rows):
            next(transaction_reader)  # skip header

        for row in transaction_reader:
            if len(row) < 8:
                break  # no more data to be loaded
            transactions.append(translate_row(row))

    return transactions


def translate_row(row):
    idx_out = 7
    idx_inn = 6
    idx_text = 5
    idx_tr_type = 4
    idx_date = 0
    date_format = "%Y-%m-%d"

    out = convert_comma_float(row[idx_out])
    inn = convert_comma_float(row[idx_inn])
    text = row[idx_text]
    tr_type = row[idx_tr_type]
    date = datetime.datetime.strptime(row[idx_date], date_format)

    return Transaction(out, inn, date, tr_type, text)


def convert_comma_float(number_string):
    try:
        return float(number_string.replace(",", "."))
    except ValueError:
        return None


def load_category_file(filepath):
    with open(filepath, 'r') as jsonfile:
        json_data = json.load(jsonfile)

        if not isinstance(json_data, dict):
            raise SyntaxError("invalid json format")
        return json_data


def save_categories(filepath, category_list: CategoryCollection):
    with open(filepath, 'w') as outfile:
        json.dump(category_list.category_dict, outfile)
