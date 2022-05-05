import os

cls = lambda: os.system('cls')

class ShoppingProduct:
    
    def __init__(self, shop_prod_name: str, shop_prod_qty: int):
        """
        :param shop_prod_name: Name of a product in shopping cart
        :param shop_prod_qty: Current quantity in shopping cart
        """

        self.shop_prod_name = shop_prod_name
        self.shop_prod_qty = shop_prod_qty
        


class Products:

    def __init__(self, prod_name: str, prod_stock: int, prod_cost: float):
        """
        :param prod_name: Name of a product
        :param prod_stock: Current stock of products
        :param prod_cost: Product price
        """
                
        self.prod_name = prod_name
        self.prod_stock = prod_stock
        self.prod_cost = prod_cost


prod_list = []
cart = []
pay_basic = []

#Example products
prod_list.append(Products(prod_name = 'Banana', prod_stock = 20, prod_cost = 2.01))
prod_list.append(Products(prod_name = 'Carrot', prod_stock = 30, prod_cost = 3.02))
prod_list.append(Products(prod_name = 'Watermelon', prod_stock = 15, prod_cost = 4.03))


def admin_menu():
    """Admin navigation menu - class Products"""
    while True:
        
        choice = int(input('Select:\n1.Add product\n2.Remove product\n3.Change product\n4.List product\n'))

        if choice == 1:
            add_product()
        elif choice == 2:
            remove_product()
        elif choice == 3:
            change_product()
        elif choice == 4:
            list_product()
            
def list_product():
        # cls()
        indx = 0
        for index in prod_list:
            print(f'Index: {indx} | Product name: {prod_list[indx].prod_name} | Product stock: {prod_list[indx].prod_stock} | Product cost: {prod_list[indx].prod_cost} \n')
            indx +=1  

def add_product():
    """Part of admin menu, let You add product to prod_list - class Products"""
    cls()

    while True:

        try:
            new_prod_id = len(prod_list) + 1
            choice_add_prod_name = str(input('Add product name:\n'))
            choice_add_prod_stock = int(input('Add product quantity:\n'))
            choice_add_prod_cost = float(input('Add product price:\n'))
            break

        except ValueError:
            cls()
            print('Please enter correct values.')
            continue
            
    prod_list.append(Products(prod_name = choice_add_prod_name, prod_stock = choice_add_prod_stock, prod_cost = choice_add_prod_cost))
    cls()
    print(f'You added: \n Product name: {prod_list[new_prod_id-1].prod_name}\n Quantity: {prod_list[new_prod_id-1].prod_stock} \n Price: {prod_list[new_prod_id-1].prod_cost}\n')


def remove_product():
    """Part of admin menu, let You remove product from prod_list - class Products"""
    cls()
    list_product()

    while True:
        try:
            choice = int(input(f'Insert Index number to remove. Possible index is {len(prod_list)-1} and below: \n'))

            if choice <= len(prod_list) -1:
                del prod_list[choice]
                break
            
        except ValueError:
            print('Please enter correct value.')
            continue


def change_product():
    """Part of admin menu, let You change product name, stock and qty in prod_list - class Products"""

    list_product()

    while True:
        try:

            choice_index = int(input('What index You want to change: \n'))
            cls()

            print(f'You selected {prod_list[choice_index].prod_name}')
            choice = int(input('1.Change Product name\n2.Change product stock quantity\n3.Change product price\n'))
            
            if choice == 1:
                cls()

                change_prod_name = str(input(f'Input new product name, current is: {prod_list[choice_index].prod_name}\n'))
                prod_list[choice_index].prod_name = change_prod_name

                cls()
                break

            elif choice == 2:
                cls()

                change_prod_stock = int(input(f'Input new stock for {prod_list[choice_index].prod_name}, current is: {prod_list[choice_index].prod_stock}\n'))
                prod_list[choice_index].prod_stock = change_prod_stock

                cls()
                break
                
            elif choice == 3:
                cls()

                change_prod_cost = int(input(f'Input new price for {prod_list[choice_index].prod_name}, current is: {prod_list[choice_index].prod_cost}\n'))
                prod_list[choice_index].prod_cost = change_prod_cost

                cls()
                break

        except ValueError or TypeError:
            print('Please enter correct value.')
            continue



def shopping_cart():
    """Client navigation menu - class ShoppingProduct """
    cls()
    while True:
        choice = int(input('1.Add to cart\n2.Remove form cart\n3.Clear cart\n4.Summary\n'))

        if choice == 1:
            shopping_cart_add()
        elif choice == 2:
            shopping_cart_remove()
        elif choice == 3:
            shopping_cart_clear()
        elif choice == 4:
            shopping_cart_summary()


def shopping_cart_add():
    """Part of client menu, let You add products to cart - class ShoppingProduct + Products"""
    cls()

    while True:
        list_product()
        try:
            choice = (int(input('Choose index number for product which u want add to your cart:\n'))) 

            if choice >= 0:

                if choice <= len(prod_list) - 1:

                    choice_quantity = (int(input(f'Choose how much You want of {prod_list[choice].prod_name}:\n')))
                    cart.append(ShoppingProduct(shop_prod_name = prod_list[choice].prod_name, shop_prod_qty = choice_quantity))
                    cls()
                    print(f'You added: {cart[-1].shop_prod_name} Qty: {cart[-1].shop_prod_qty}\n')
                    break

                else:
                    print('Please enter correct value.\n')
                    continue

            else: 
                print('Please enter correct value.\n')
                continue

        except ValueError :
            print('Please enter correct value.\n')
            continue


def shopping_cart_remove():
    """Remove item form shopping cart - class ShoppingProduct """
    cls()
    indx = 0

    for item in cart:
        print(f'Index: {indx} Product name: {cart[indx].shop_prod_name}')
        indx += 1

    while True:
        
        index_for_remove = int(input('Input index for remove:\n'))
        if index_for_remove >= 0:
            del cart[index_for_remove]
            cls()
            break
        else:
            print('Please enter correct value.\n')
            continue

def shopping_cart_clear():
    """Remove all items from shopping cart - class ShoppingProduct"""

    cls()
    cart.clear()
    

def shopping_cart_summary(): 
    """Count total cost of all products in cart - class ShoppingProduct + Products"""

    cls()
    pay_basic =[]
    indx_shop = 0   
    indx_cart = 0
    
    for elem in cart:
     
        pay_basic.append(cart[indx_cart].shop_prod_qty * prod_list[indx_shop].prod_cost)
        indx_shop =+ 1
        indx_cart += 1

    total_net = sum(pay_basic)
    total_net_formated = "{:.2f}".format(total_net)
    total_gross = total_net * 1.23
    total_gross_formated = "{:.2f}".format(total_gross)
    print(f'Total Net cost: {total_net_formated} | Total Gross cost: {total_gross_formated}')
    
    if cart ==[]:
        print('Cart is empty.\n')
    
        
                
while True:
    choice = int(input('1.Admin\n2.Client\n'))

    if choice == 1:
        admin_menu()
    elif choice == 2:
        shopping_cart()
    else:
        print('Please enter correct value.\n')
        continue


