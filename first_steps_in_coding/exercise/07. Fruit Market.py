strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())
raspberry_price = strawberry_price * 0.5
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2
money = (strawberry_quantity * strawberry_price) + (banana_quantity * banana_price) + (
        orange_quantity * orange_price) + (raspberry_quantity * raspberry_price)
print(money)
