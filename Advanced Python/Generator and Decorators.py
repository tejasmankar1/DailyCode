# def serve_chai():
#     yield "cup 1: Masala chai"
#     yield "cup 2 : Ginger chai"
#     yield "cup 3 : Elaichi chai"

# stall = serve_chai()

# for cup in stall:
#     print(cup)



# def get_chai_list():
#     return ["cup1","cup2","cup3"]

# #generator function

# def get_chai_gen():
#     yield "cup1"
#     yield "cup2"
#     yield "cup3"


# chai = get_chai_gen()
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))         # gives error

#########  Infinite Generators   #################
# def infinite_chai():
#     count = 1
#     while True:
#         yield f"Refil #{count}"
#         count += 1

# refill = infinite_chai()
# user = infinite_chai()


# for _ in range(5):
#     print(next(refill))

# for _ in range(5):
#     print(next(user))

##################### send value to genertors   ###############

# def chai_customer():
#     print("welcome ! what chai would u like ?")
#     order = yield
#     while True:
#         print(f"Preparing : {order}")
#         order = yield

# stall = chai_customer()
# next(stall)  # start the generator

# stall.send("Masala Chai")
# stall.send("Lemon Chai")


######################  yield from and close ####################

# def local_chai():
#     yield "Masala Chai"
#     yield "Ginger chai"

# def imported_chai():
#     yield "Matcha"
#     yield "Oolong"

# def full_menu():
#     yield from local_chai()
#     yield from imported_chai()

# for chai in full_menu():
#     print(chai)


# def chai_stall():
#     try:
#         while True:
#             order = yield "waiting for chai order"
#     except:
#         print("stall closed , no more chai")

# stall = chai_stall()
# print(next(stall))
# stall.close()    #memory cleanup


###########################   Decorators #####################

# from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator

# def greet():
#     print("Hello from decorators class from tejas")

# greet()

# print(greet.__name__)



#####################   logger with decorator  ####################

# from functools import wraps

# def log_activity(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling : {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Finished : {func.__name__}")
#         return result
#     return wrapper

# @log_activity
# def brew_chai(type,milk = "no"):
#     print(f"Brewing {type} chai and milk status {milk}")

# brew_chai("Masala")

######################3 Build authorization decorator ##################

# from functools import wraps

# def require_admin(func):
#     @wraps(func)
#     def wrapper(user_role):
#         if user_role != "admin":
#             print("Access denied : Admins only")
#             return None
#         else:
#             return func(user_role)
#     return wrapper


# @require_admin
# def acess_tea_inventory(role):
#     print("Access granted to tea inventory")

# acess_tea_inventory("user")
# acess_tea_inventory("admin")