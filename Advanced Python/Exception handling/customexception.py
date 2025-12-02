######## Custom Error ##############

# def brew_chai(flavor):
#     if flavor not in ["masala","elaichi",'mint']:
#         raise ValueError("Unsupported chai Flavor")
#     print(f"Brewing {flavor} chai....")

# brew_chai("masala")
# brew_chai("ginger")

##############33 Custom Exception ##############
class OutOfIngredients(Exception):
    pass

def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredients("Missing milk or sugar")
    print("Chai is ready...")

make_chai(0,1)