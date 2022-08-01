# WRITE YOUR FUNCTIONS HERE

from unicodedata import name


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

def get_pets_sold(pets):
    return pets["admin"]["pets_sold"]

def increase_pets_sold(pets, pets_increase):
    pets["admin"]["pets_sold"] += pets_increase

def get_stock_count(stock):
    return len(stock["pets"])

def get_pets_by_breed(pets, bsh):
    bsh_list = []
    for pet in pets["pets"]:
        if pet["breed"] == bsh:
            bsh_list.append(bsh)
    return bsh_list

def find_pet_by_name(pets, name):
# navigate to pets list
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pets, name):
# iterate through list to find arthur
    for pet in pets["pets"]:
        if pet["name"] == name:
            pets["pets"].remove(pet)

def add_pet_to_stock(pets, new_pets):
    pets["pets"].append(name)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, remove):
    customer["cash"] -= remove
    return remove

def get_customer_pet_count(customers):
    customer_pets = customers["pets"]
    for customer in customers:
        if customer[1] == []:
            customer_pets.append(customer) 
    return len(customer_pets)

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return customer["pets"]

