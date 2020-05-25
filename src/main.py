# from src.category import Category, CategoryCollection
from src.transaction import Transaction
from src.category_collection import CategoryCollection
from src.file_managment import load_transactions, load_category_file, save_categories


def set_transaction_categories(transaction_list, category_list):
    for transaction in transaction_list:
        category = category_list.get_matching_category(transaction.text)

        if category is None:
            category = category_list.choose_category()

        transaction.set_category(category)


def define_substring(text: str):
    input_ok = False
    substring = None

    while not input_ok:
        print("Please enter a substring from the text below")
        print(text)
        substring = input("Your substring:")
        input_ok = substring in text
    return substring


def update_category_list(category_list: CategoryCollection):
    pass


transaction_filepaths = [
    "data/visa/97224534721_2020_01_01-2020_01_31.csv"
]

january_transactions = load_transactions(transaction_filepaths[0])
print("loaded!")
# for transaction in january_transactions:
#     # category = category_list.get_matching_category(transaction.text)
#     # transaction.set_category()
#     print("{}: {}".format(transaction.text, transaction.out))

json_dict = load_category_file("data/saved_categories.json")
collection = CategoryCollection(json_dict)

for transaction in january_transactions:
    if not(collection.get_matching_category(transaction.text)):
        collection.choose_category(transaction.text)

save_categories("data/saved_categories.json", collection)
# BUG! if a substring is a substring of an existing entry it will be saved, and
