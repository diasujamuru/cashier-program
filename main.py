#import module & library
#tes komen
import module as data
import pandas as pd

#Declare variable(list) for place value
item_price = []
item_name = []
much_item = []
much_item2 = []
total_price = []

#Condition for looping
order_again = 'y'

#Process Looping
while order_again != 'n':

    #Input what menu to output
    choose_menu = input("What menu do you order [food/drink] : ")

    #Condition if user want to order food
    if choose_menu.lower() == "food":
        
        #Output for list of food
        print("============= CASHIER =============")

        print("List of Food : ")
        for i in range(len(data.food)):
            print(str(i+1), data.food[i])

        print("===================================")

        #Input how much order user want
        many_order = int(input("How much your order : "))

        #Process user order
        for order in range(many_order):
            print("Order ", str(order+1)) 
            name_order = input("Your order : ")
            much_item.append(int(input("How much : ")))

            if name_order.lower() == "burger":
                item_name.append("Burger")
                item_price.append("${:,.2f}".format(2))
                total_price.append(much_item[order] * 2.00)
            elif name_order.lower() == "fried fries":
                item_name.append("Fried Fries")
                item_price.append("${:,.2f}".format(1.5))
                total_price.append(much_item[order] * 1.50)
            elif name_order.lower() == "fried chicken":
                item_name.append("Fried Chicken")
                item_price.append("${:,.2f}".format(2.5))
                total_price.append(much_item[order] * 2.50)

        #Input if user want to order again, they will back to choose_menu
        order_again = input("Do you want to order again [y/n] : ")

    #Condition if user want to order drink
    elif choose_menu.lower() == "drink":

        #Output for list of drink
        print("============= CASHIER =============")

        print("List of Food : ")
        for i in range(len(data.drink)):
            print(str(i+1), data.drink[i])

        print("===================================")

        #Input how much order user want
        many_order = int(input("How much your order : "))

        #Process user order
        for order in range(many_order):
            print("Order ", str(order+1)) 
            name_order = input("Your order : ")
            much_item2.append(int(input("How much : ")))
    
            if name_order.lower() == "coca cola":
                item_name.append("Coca Cola")
                item_price.append("${:,.2f}".format(1))
                total_price.append(much_item2[order] * 1.00)
            elif name_order.lower() == "sprite":
                item_name.append("Sprite")
                item_price.append("${:,.2f}".format(1))
                total_price.append(much_item2[order] * 1.00)
            elif name_order.lower() == "milo":
                item_name.append("Milo")
                item_price.append("${:,.2f}".format(1.5))
                total_price.append(much_item2[order] * 1.50)

        #Input if user want to order again, they will back to choose_menu    
        order_again = input("Do you want to order again [y/n] : ")

final_much_item = much_item + much_item2
print(final_much_item)

#dictionary for output with library (Pandas)
order = {
    "Name" : item_name,
    "Price" : item_price,
    "lots of item" : final_much_item,
    "Total" : total_price
}

#Declare dictionary to pandas
final_order = pd.DataFrame(order)

#Output for all of order
print("============== YOUR ORDER =============")
print(final_order)
print("=======================================")

#Process to get price_order, tax_price and final_price_order
price_order = sum(total_price)
tax_price = price_order * 5/100
final_price_order = price_order - tax_price

#Output for price_order, tax_price and final_price_order
print(f"                  Price Order : ${str(price_order)}")
print(f"                  Price Order : ${str(tax_price)}")
print(f"                  Price Order : ${str(final_price_order)}")
