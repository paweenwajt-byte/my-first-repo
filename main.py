from bank import BankAccount

def main():
    acc = BankAccount("A101", "Alice", 100.0)
    print(f"Initial balance: {acc.get_balance()}")
    acc.deposit(50.0)
    print(f"After deposit 50: {acc.get_balance()}")
    acc.withdraw(30.0)
    print(f"After withdraw 30: {acc.get_balance()}")

if __name__ == "__main__":
    main()