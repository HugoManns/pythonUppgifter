class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

edvin_account = Bank('Edvin', 60000)
hugo_account = Bank('Hugo', 5000)
print(hugo_account.name)
print(hugo_account.balance)

print(edvin_account.balance)