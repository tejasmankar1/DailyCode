class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding spices ginger, cardomom, cloves.")

#Composition

class Chaishop:
    chai_cls = BaseChai    # reference of class

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(Chaishop):
    chai_cls = MasalaChai


shop = Chaishop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()

    
