product = input()
plant = ""
if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
    plant = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    plant = "vegetable"
else:
    plant = "unknown"
print(plant)
