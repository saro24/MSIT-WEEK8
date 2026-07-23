import sys
from bank import Ledger


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 process.py <input_csv> <output_report>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    ledger = Ledger()

    total_transactions = 0
    total_deposits = 0
    deposit_count = 0

    with open(input_file, "r") as file:
        next(file)  # Skip header

        for line in file:
            account_id, transaction_type, amount = line.strip().split(",")

            amount = float(amount)

            ledger.apply(account_id, transaction_type, amount)

            total_transactions += 1

            if transaction_type == "deposit":
                total_deposits += amount
                deposit_count += 1

    average_deposit = 0

    if deposit_count > 0:
        average_deposit = total_deposits / deposit_count

    with open(output_file, "w") as report:

        report.write("TartanBank Daily Report\n")
        report.write("========================\n\n")

        report.write("Final Account Balances\n")

        for account in ledger.accounts.values():
            report.write(
                f"{account.account_id}: "
                f"Balance = {account.balance:.2f}, "
                f"Transactions = {account.transaction_count}\n"
            )

        report.write(f"\nTotal transactions processed: {total_transactions}\n")

        report.write(f"Total value of deposits: {total_deposits:.2f}\n")

        report.write(f"Average deposit amount: {average_deposit:.2f}\n")

        report.write("\nFlagged Withdrawals\n")

        if ledger.flagged:
            for item in ledger.flagged:
                report.write(item + "\n")
        else:
            report.write("None\n")


if __name__ == "__main__":
    main()
