class ChaiOrder():
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml cup of {self.type} chai"
    
order = ChaiOrder("Masala" , 200)
print(order.summary())
        