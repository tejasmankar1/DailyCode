##############   LIst Comprehensions  ####################
menu = [

"Masala chai",
"Iced lemaon tea",
"Green Tea",
"Iced Peach tea",
"Ginger tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)

iced_tea1 = [tea for tea in menu if len(tea) > 12]
print(iced_tea1)


######################    Set Comprehensions      ##########################

favourite_chais = [
    "Masala chai",
    "Green tea",
    "Masala chai",
    "Lemon tea",
    "Green tea",
    "Elachai chai"
]


unique_chai = {chai for chai in favourite_chais if len(chai) > 10}
print(unique_chai)



recipes = {
    "Masala Chai" : ["ginger", "cardamom" ,"clove"],
    "Elaichi Chai" : ["cardamom" ,"milk"],
    "Spicy Chai" : ["ginger", "black pepper" ,"clove"]

}


unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)

################### Dictionary comprehensions ########################


tea_prices_inr ={
    "Masala Chai" : 40,
    "Green tea" : 50,
    "lemon tea" : 200
}


tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)

#########################     Generator comprehensions  ##################

daily_sales = [5,10,12,7,3,8,9,15]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)