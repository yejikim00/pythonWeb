class item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"{self.name}을 {self.price}에 팝니다.")
    
    def discard(self):
        print(f"{self.name}을 버립니다.")

class WearableItem(item):
    def __init__(self)