class Category:
    def __init__(self, name):
        self.name = name
        self.substrings = []

    def __contains__(self, text: str):
        # Possible preformance boost: Aho–Corasick algorithm
        return any(substring in text for substring in self.substrings)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def add_substring(self, substring: str):
        if not(substring in self.substrings):
            self.substrings.append(substring)

    def add_substrings(self, substring_list):
        for substring in substring_list:
            self.add_substring(substring)

    def remove_substring(self, substring: str):
        self.substrings.remove(substring)
