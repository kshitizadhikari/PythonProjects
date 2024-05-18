class Vault:
    def __init__(self, coin, cash):
        self.coin = coin
        self.cash = cash

    def __str__(self) -> str:
        return f"Coin: {self.coin}\tCash: {self.cash}"
    
    def __add__(self, other):
        totalCoin = self.coin + other.coin
        totalCash = self.cash + other.cash
        return Vault(totalCoin, totalCash)


    ...

ramVault = Vault(10, 20)
samVault = Vault(20, 45)


#get total coin
totalVault = ramVault + samVault

print(totalVault)