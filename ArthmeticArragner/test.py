class Category:
    def __init__(self, name):
        self.name = name
        self.details = []

    def deposit(self, amount, description=""):
        self.details.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if (self.check_fund(amount)):
            self.details.append(
                {"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.details:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_fund(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from{self.name}")
            return True
        return False

    def check_fund(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0

        for transaction in self.details:
            items += f"{transaction['description'][:23]:23}" + \
                f"{transaction['amount']:>7.2f}\n"
            total += transaction["amount"]
            output = title + items + f"Total:{total:.2f}"
            return output


def create_spend_chart(categories):
    total_withdrawals = 0
    category_names = []
    spent_percentages = []

    for category in categories:
        total_withdrawals += category.get_withdrawals()
        category_names.append(category.name)

    for category in categories:
        spent_percentage = category.get_withdrawals() / total_withdrawals * 100
        spent_percentages.append(spent_percentage)

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

    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length):
        chart += "    "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart
