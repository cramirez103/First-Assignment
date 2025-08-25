class Transaction:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        type_ = "Income" if self.amount >= 0 else "Expense"
        return f"{type_}: ${abs(self.amount):.2f} - {self.category} - {self.description}"


class Budget:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, category="General", description=""):
        self.transactions.append(Transaction(amount, category, description))

    def add_expense(self, amount, category="General", description=""):
        self.transactions.append(Transaction(-amount, category, description))

    def show_summary(self):
        total_income = sum(t.amount for t in self.transactions if t.amount > 0)
        total_expense = -sum(t.amount for t in self.transactions if t.amount < 0)
        balance = total_income - total_expense

        print("\n--- Budget Summary ---")
        print(f"Total Income:  ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Balance:       ${balance:.2f}")

    def show_transactions_by_category(self):
        category_dict = {}
        for t in self.transactions:
            if t.category not in category_dict:
                category_dict[t.category] = []
            category_dict[t.category].append(t)

        print("\n--- Transactions by Category ---")
        for category, trans_list in category_dict.items():
            print(f"\nCategory: {category}")
            for t in trans_list:
                print(f" - {t}")


def main():
    budget = Budget()

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Transactions by Category")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Amount of income: "))
                category = input("Category (e.g., Salary, Freelance): ")
                description = input("Description (optional): ")
                budget.add_income(amount, category, description)
                print("Income added!")
            except ValueError:
                print("Invalid amount.")

        elif choice == '2':
            try:
                amount = float(input("Amount of expense: "))
                category = input("Category (e.g., Food, Rent): ")
                description = input("Description (optional): ")
                budget.add_expense(amount, category, description)
                print("Expense added!")
            except ValueError:
                print("Invalid amount.")

        elif choice == '3':
            budget.show_summary()

        elif choice == '4':
            budget.show_transactions_by_category()

        elif choice == '5':
            print("Exiting. Take control of your finances! ")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()