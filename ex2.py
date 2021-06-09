from abc import ABC, abstractmethod


class Request(ABC):
    @abstractmethod
    def execute(self):
        pass


class CheckBalance(Request):
    def __init__(self, bank, ag, cc):
        self.bank = bank
        self.acc = (ag, cc)

    def execute(self):
        self.bank.check_balance(self.acc)


class GetBankStatement(Request):
    def __init__(self, bank, ag, cc):
        self.bank = bank
        self.acc = (ag, cc)

    def execute(self):
        self.bank.get_statement(self.acc)


class Transfer(Request):
    def __init__(self, bank, ag1, cc1, ag2, cc2, value):
        self.bank = bank
        self.acc1 = (ag1, cc1)
        self.acc2 = (ag2, cc2)
        self.value = value

    def execute(self):
        self.bank.transfer(self.acc1, self.acc2, self.value)


class Bank:
    def check_balance(self, acc):
        if acc:
            print(f'Checking balance for (ag,cc): {acc}\n')

    def get_statement(self, acc):
        if acc:
            print(f'Getting bank statement for (ag,cc): {acc}\n')

    def transfer(self, acc1, acc2, value):
        if value > 0 and acc1 != acc2:
            print(f'Transferring ${value} from {acc1} to {acc2}\n')


class Manager:
    def __init__(self):
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def run_order(self):
        self.orders.pop(0).execute()


if __name__ == '__main__':
    bankX = Bank()
    manager = Manager()
    my_ag = '0001'
    my_cc = '1234-1'
    other_ag = '0002'
    other_cc = '6789-0'
    qty = 500.00
    requests = [CheckBalance(bankX, my_ag, my_cc), Transfer(bankX, my_ag, my_cc, other_ag, other_cc, qty),
                GetBankStatement(bankX, my_ag, my_cc)]
    for r in requests:
        manager.place_order(r)
    while True:
        try:
            manager.run_order()
            print('Running next order...\n')
        except IndexError:
            break
    print('Oh, no more orders! :)')    
         
