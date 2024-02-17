class Bankaccount :
    def __init__(self,name,accountnumber,balance=50000000) -> None:
        self.accountnumber=accountnumber
        self.name=name
        self.balance=50000000

    def deposite(self,d_amount):
        self.d_amount=d_amount
        self.balance+=self.d_amount
        print(f"deposite amount is credit in your bank account :{self.accountnumber}")
        print(f" Your current balance is {self.balance}")

    def withdrawal(self,w_amount):
        self.w_amount=w_amount
        self.balance-=self.w_amount
        print(f"Amount is Withdrawal from your accont is {self.w_amount}")
        print(f"After Withdrawal Current Balance is now {self.balance}")

    def display_account_details(self,accountnumber,name,balance):
        self.accountnumber=accountnumber
        self.name=name
        self.balance=balance

        print(f"Account Holder name : {self.name}")
        print(f"Account Holder name : {self.accountnumber}")
        print(f"Account Holder name : {self.balance}")





# MAIN FUCNTION----------------------------


def main():
    name = input("Enter name of account holder: ")
    account_number = input("Enter 10-digit account number: ")

    if len(account_number) != 10:
        print("Error: Account number must be 10 digits long.")
        return

    try:
        account_number = int(account_number)
    except ValueError:
        print("Error: Account number must be a valid integer.")
        return

    bank_account = Bankaccount(name, account_number)

    withdrawal_of_amount = float(input("Enter the amount you want to withdraw = "))
    bank_account.withdrawal(withdrawal_of_amount)

if __name__ == "__main__":
    main()