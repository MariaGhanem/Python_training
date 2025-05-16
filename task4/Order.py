from MenuItem import MenuItem
class Order:
    def __init__(self):
        self.items = []
        
    def add_item(self,item):
        self.items.append(item)
        
    def total(self):
        total_price=0
        for item in self.items:
            total_price+= item.price
        return total_price