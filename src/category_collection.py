from src.utils import input_loop


class CategoryCollection:
    CANCEL_COMMAND = "exit"
    CREATE_COMMAND = "create"

    def __init__(self, category_dict: dict):
        self.category_dict = category_dict

    def __contains__(self, category: str):
        return any(category == category_name
                   for category_name in self.category_dict.keys())

    def __str__(self):
        return_string = ""
        for category, substring_list in self.category_dict.items():
            return_string += category + ":\t" + ",".join(substring_list) + "\n"
        return return_string

    def get_matching_category(self, text: str):
        for category, substring_list in self.category_dict.items():
            if any(substring in text or text in substring or substring == text for substring in substring_list):
                return category
        return None

    def add_substring(self, category: str, text: str):
        existing = self.get_matching_category(text)
        if existing:
            print("Substring already in category: {}".format(existing))
            return

        if not (category in self):
            self.category_dict[category] = []
        self.category_dict[category].append(text)
        print("Added '" + text + "' to '" + category + "'")

    def add_substrings(self, category: str, substrings: list = None):
        # create the category with and empty list if it didn't exist
        if substrings is None and not (category in self):
            self.category_dict[category] = []
            return

        for substring in substrings:
            self.add_substring(category, substring)

    def add_category(self):
        input_text = input_loop("Please enter the name for the category, or '" + self.CANCEL_COMMAND + "' to cancel",
                                lambda text: not (text in self) or text == self.CANCEL_COMMAND,
                                input_hint="Please enter a category name: ",
                                error_msg="Category was in the collection already\n")
        if input_text == self.CANCEL_COMMAND:
            print("Canceled adding category.")
            return
        self.category_dict[input_text] = []
        print("Added category {}!".format(input_text))

    def choose_category(self, text):
        hint_text = "Please enter the category you want to choose for '" + text + "':\n" + \
                    self.list_categories() + \
                    "\n(Type '" + self.CREATE_COMMAND + "' to create a new category, or '" + \
                    self.CANCEL_COMMAND + "' to cancel)"
        input_text = input_loop(hint_text,
                                lambda
                                    category: category in self or category == self.CANCEL_COMMAND or category == self.CREATE_COMMAND,
                                input_hint="Enter a category: ",
                                error_msg="Category didn't exist.\n")
        if input_text == self.CANCEL_COMMAND:
            print("Canceled picking a category")
            return
        if input_text == "create":
            self.add_category()
            self.choose_category(text)
            return

        substring = self.choose_substring(text)
        if substring:
            self.add_substring(input_text, substring)

    def list_categories(self):
        return ", ".join(self.category_dict.keys())

    def choose_substring(self, text):
        input_text = input_loop("Please choose a substring from\n'" + text + "'\n(Type '" + \
                                self.CANCEL_COMMAND + "' to cancel.)",
                                lambda substring: ((substring in text or substring == text) and (self.get_matching_category(substring) is None) and substring.strip()) or substring == self.CANCEL_COMMAND,
                                input_hint="Enter a substring: ",
                                error_msg="Substring can't exist in the collection, and can not be empty.\n")
        if input_text == self.CANCEL_COMMAND:
            print("Canceled choosing substring.")
            return None
        return input_text
