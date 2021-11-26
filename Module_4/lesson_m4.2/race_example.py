import time
import concurrent.futures


class BankAccount:
    def __init__(self):
        self.balance = 100  # concurrent resource

    def update(self, transaction: str, amount) -> None:
        print(f'transaction {transaction} started')
        cash_amount = self.balance
        cash_amount += amount
        time.sleep(2)
        self.balance = cash_amount
        print(f'transaction ended: {transaction}')


if __name__ == "__main__":
    acc = BankAccount()
    print(f'Process started, balance = {acc.balance}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f"end of main, Balance = {acc.balance}")
