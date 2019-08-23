stock = {
    'kitkat' : 3,
    'chefmeal' : 1,
    'brookside' : 3,
    'burger' : 1,
    'fries' : 2,
    'sushi' : 1,
    'grilled cheese' : 1,
}

prices = {
    'kitkat' : 1.67,
    'chefmeal' : 10,
    'brookside' : 3.27,
    'burger' : 2.65,
    'fries' : 1.50,
    'sushi' : 7.87,
    'grilled cheese' : 2.68,
}

def compute_bill(input("What do you want for lunch")):
    total = 0
    for item in prices:
        item = shopping_list(prices[key])
        total += item
    return total

input("What do you want for lunch")
compute_bill(input("What do you want for lunch"))

