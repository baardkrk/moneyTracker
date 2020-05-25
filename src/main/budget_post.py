class BudgetPost:
    def __init__(self, name, amount=0.00):
        self.name = name
        self.amount = amount
        self.active = True
        self.category = None

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def is_active(self):
        return self.active
