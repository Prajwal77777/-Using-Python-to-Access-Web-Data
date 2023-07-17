class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def get_withdrawals(self):
        withdrawals = 0
        for transaction in self.ledger:
            if transaction["amount"] < 0:
                withdrawals -= transaction["amount"]
        return withdrawals

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for transaction in self.ledger:
            items += f"{transaction['description'][:23]:23}" + \
                f"{transaction['amount']:>7.2f}\n"
            total += transaction['amount']
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    total_withdrawals = sum(category.get_withdrawals()
                            for category in categories)
    spent_percentages = [(category.get_withdrawals() /
                          total_withdrawals) * 100 for category in categories]

    chart = "Percentage spent by category\n"
    for percentage in range(100, -10, -10):
        chart += f"{percentage:3}| "
        for spent_percentage in spent_percentages:
            if spent_percentage >= percentage:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart = chart.rstrip() + "\n"  # Remove trailing whitespace from each line
        if i < max_name_length - 1:
            chart += "\n"

    return chart
