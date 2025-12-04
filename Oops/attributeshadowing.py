class chai:
    temperature = "hot"
    strength = "strong"

cutting = chai()

print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("after changing", cutting.temperature)
print("cup size is : ", cutting.cup)
print("direct look into the class", chai.temperature)

del cutting.temperature
print(cutting.temperature)

del cutting.cup
print(cutting.cup)