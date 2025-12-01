#Duplication-----------------------------------------------------------------


# def print_order(name, chai_type):
#     print(f"{name}  ordered {chai_type} chai")


# print_order("Tejas" , "masala")
# print_order("Abhishek" , "ginger")



# #Complex task spliting--------------------------------------------------------------

# def fetch_sales():
#     print("Fectching the sales data")

# def filter_valid_sales():
#     print("Filtering valid sales data")

# def summarize_data():
#     print("Summarizing sales data")

# def generate_report():
#     fetch_sales()
#     filter_valid_sales()
#     summarize_data()
#     print("Report is ready")


# generate_report()

#----------------------------------------------------------------------------------

#hiding

# def get_input():
#     print('Getting User input')

# def valid_input():
#     print('Validating the user Info')

# def save_to_db():
#     print("Saving to dataBase")

# def register_user():
#     get_input()
#     valid_input()
#     save_to_db()
#     print("User registration complete")

# register_user()

#---------------------------------------------------------------------------
#Readability

# def calculate_bill(cups, price_per_cup):
#     return cups * price_per_cup

# my_bill = calculate_bill(3,15)
# print(my_bill)

# print("Order for table 2:", calculate_bill(2,50))


#------------------------------------------------------------------------------

#improving tracebality

# def add_vat(price,vat_rate):
#     return price * (100 + vat_rate)/100


# orders = [100,150,200]

# for price in orders:
#     final_amount = add_vat(price,10)
#     print(f"Original: {price}, Final with VAT : {final_amount}")

#--------------------------------------------------------------------------------------

###############              Scope                #########

# def serve_chai():
#     chai_type = "masala"  # Local Scope  inside a function
#     print(f"Inside function {chai_type}")

# chai_type = "lemon"  # global scope
# serve_chai()
# print(f"Outside function {chai_type}")  


# def chai_counter():
#     chai_order = "Lemon" # enclosing scope
#     def print_order():
#         chai_order = "Ginger"
#         print("Inner: ",chai_order)
#     print_order()
#     print("outer: ",chai_order)

# chai_order = "tulsi" # global
# chai_counter()
# print("global: ",chai_order)


#------------------------------------------------------------------------------------

#nonlocal 

# def update_order():
#     chai_type = "Elaichi"
#     def kitchen():
#         #nonlocal chai_type
#         chai_type = "kesar"
#     kitchen()
#     print("After kitchen update ", chai_type)

# update_order()


#Global Scope---------------------------------------------------------------

# chai_type = "plain"

# def front_desk():
#     def kitchen():
#         global chai_type
#         chai_type = "Irani"
#     kitchen()

# front_desk()
# print("Final Global chai", chai_type)

#----------------------------------------------------------------------------------------
#######################################Arguments###############################

# chai = "ginger chai"

# def prepare_chai(order):
#     print("preparing",order)


# prepare_chai(chai)
# print(chai)


# chai = [1,2,3]

# def edit_chai(cup):
#     cup[1] = 42

# edit_chai(chai)
# print(chai)

# def special_chai(*ingredients,**extras):    #args and *kwargs    postitonal and keywords arguments
#     print("Im=ngredients: ",ingredients)
#     print('Extras', extras)

# special_chai("Ginger","cardomom",sweetner= "Honey",foam = "yes")


# def chai_orders(order = []):
#     order.append("Masala")
#     print(order)


# def chai_orders(order = None):
#     if order is None:
#         order = []
#     print(order)
# chai_orders()
# chai_orders()

#------------------------------------------------------------------------------------
# def make_chai():
#    #return "here is your masala chai"
#    print("here is your masala chai")
# return_value = make_chai()
# print(return_value)


# def idle_chaiwla():
#    pass

# print(idle_chaiwla())

# def sold_cups():
#    return 120

# total = sold_cups()

# print(total)


# def chai_status(cups_left):
#    if cups_left ==0:
#       return "chai over"
#    return "Chai is Ready"

# print(chai_status(0))
# print(chai_status(5))

# def chai_report():
#    return 100,20 # sold ,remaining

# sold,remaining = chai_report()
# print("sold: ",sold)
# print("remaining: ",remaining)

#-----------------------------------------------------------------------------------------
# types of  functions
#pure and impure
#recursive
#Lambda

# def pure_chai(cups):
#    return cups * 10

# total_chai = 0

# def impure_chai(cups):
#    global total_chai
#    total_chai += cups

# def pour_chai(n):
#    print(n)
#    if n==0:
#       return "all cups poured"
#    return pour_chai(n-1)
# print(pour_chai(3))

# chai_types = ["light", "kadak", "ginger", "kadak"]


# strong_chai = list(filter(lambda chai: chai!="kadak",chai_types))

# print(strong_chai)
#-----------------------------------------------------------------------------------
# Built in functions

# def chai_flavor(flavor = "masala"):
#     """Return the flavor of chai"""
#     chai = "ginger"
#     return flavor

# print(chai_flavor.__doc__)
# print(chai_flavor.__name__)
    


# def generate_bill(chai=0, samosa=0):
#     """
#     calculate the total bill for chai and samosa
#     :param chai Number pf chai cups(10 rupees each)
#     :param samosa: number o samosa (15 rupees each)
#     :return : (total amount, thanku message)
#     """
#     total = chai*10 + samosa*15
#     return total, "Thank you for visiting"


