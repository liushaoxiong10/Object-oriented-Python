class BettingStrategy:
    def __init__(self):
        self.win = 0
        self.loss = 0
    def __call__(self):
        return 1

class BettingMartingale(BettingStrategy):
    def __init__(self):
        self._win = 0
        self._loss = 0
        self.stage = 1
    @property
    def win(self):
        return self._win
    @win.setter
    def win(self, value):
        self._win=value
        self.stage =1
    @property
    def loss(self):
        return self._loss
    @loss.setter
    def loss(self, value):
        self._loss = value
        self.stage *= 2
    def __call__(self):
        return self.stage
bet = BettingMartingale()
print(bet())
bet.win += 1
print(bet())
bet.loss += 1
print(bet())

class BettingMartingale2(BettingStrategy):
    def __init__(self):
        self._win = 0
        self._loss = 0
        self.stage = 1
    def __setattr__(self, key, value):
        if key == "win":
            print("win")
            self.stage = 1
        elif key == "loss":
            print("loss")
            self.stage *= 2
        super().__setattr__(key , value)
    def __call__(self):
        return self.stage

bet2=BettingMartingale2()
print(bet2())
setattr(bet2,"win",1)
print(bet2())
setattr(bet2,"loss",1)
print(bet2())