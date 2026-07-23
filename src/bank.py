class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = account_id
        self.balance = balance
        self.transaction_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_count += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_count += 1
            return True
        return False


class Ledger:
    def __init__(self):
        self.accounts = {}
        self.flagged = []

    def get_or_create(self, account_id):
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id)
        return self.accounts[account_id]

    def apply(self, account_id, transaction_type, amount):
        account = self.get_or_create(account_id)

        if transaction_type == "deposit":
            account.deposit(amount)

        elif transaction_type == "withdraw":
            success = account.withdraw(amount)

            if not success:
                self.flagged.append(
                    f"{account_id}: Declined withdrawal of {amount:.2f}"
                )

    def summary(self):
        return self.accounts
