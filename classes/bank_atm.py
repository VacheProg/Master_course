class BankAccount:
    def __init__(self, owner, pin, card_numebr, balance=0):
        self.owner = owner
        self.pin = pin
        self.card_numebr = card_numebr
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def get_pin(self):
        return self.pin


global_accounts = [BankAccount("Alice", "1234", "1011 2021 1011 2021")]     # acc = BankAccount("Alice", "1234", 500)


class Bank:

    def __init__(self, name="acba", address=''):
        self.name = name
        self.address = address

    def get_account(self, card):
        acc = None
        for acc in global_accounts:
            if card == acc.card_numebr:
                return acc

        return acc



    def validate_pin(self, acc, pin):
        return acc.get_pin() == pin




class ATM:
    def __init__(self, bank):
        self.bank = bank

    def get_card_user(self, card):
        pass

    def run(self):
        print("Welcome to Python Bank ATM")
        card = input("Enter your Card: ")
        self.account = self.bank.get_account(self.get_card_user(card))


        pin = input("Enter your pin: ")
        if not self.bank.validate_pin(self.account, pin):
            print("Invalid PIN. Exiting.")
            return

        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.account.check_balance()
            elif choice == "2":
                amt = float(input("Enter amount to deposit: "))
                self.account.deposit(amt)
            elif choice == "3":
                amt = float(input("Enter amount to withdraw: "))
                self.account.withdraw(amt)
            elif choice == "4":
                print("Thank you for using Python Bank ATM!")
                break
            else:
                print("Invalid choice, try again.")


# --- Example Run ---
if __name__ == "__main__":
    bank = Bank()


    atm = ATM(bank)
    atm.run()


print(__name__)