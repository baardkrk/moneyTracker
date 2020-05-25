class Transaction:
    inn = 0.00
    out = 0.00
    date = None
    tr_type = None
    text = None
    category = None

    def __init__(self, inn, out, date, tr_type, text):
        self.inn = inn
        self.out = out
        self.date = date
        self.tr_type = tr_type
        self.text = text
