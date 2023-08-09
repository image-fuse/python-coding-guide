class Account:
    def __init__(self, balance: float):
        """
        Initialize an Account object.

        Parameters:
        balance (float): The initial account balance.

        Returns:
        None
        """
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a specified amount from the account.

        Parameters:
        amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    """
    Subtype of Account representing a savings account.
    """
    pass

class CheckingAccount(Account):
    def __init__(self, balance: float, overdraft_limit: float):
        """
        Initialize a CheckingAccount object.

        Parameters:
        balance (float): The initial account balance.
        overdraft_limit (float): The overdraft limit for the checking account.

        Returns:
        None
        """
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a specified amount from the checking account.

        Parameters:
        amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account: Account) -> None:
    """
    Perform a series of bank actions on an account.

    Parameters:
    account (Account): The account on which actions will be performed.

    Returns:
    None
    """
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)
