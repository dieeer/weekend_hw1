# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(cash, addition):
    cash["admin"]["total_cash"] += addition
    return addition

def add_or_remove_cash(cash, subtraction):
    cash["admin"]["total_cash"] += subtraction
    return subtraction