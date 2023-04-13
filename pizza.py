#Imports
from textwrap import dedent
import datetime
import os
import string
import re
#Variables
pizza_address = '11430 68 St NW' #Addres of Eastglen (Pizza Place)
topping_total = 0 #counter for topping (will most likely be a bigger number)
#Main Function
def pizza_app():
    #Dicts, vars, and lists for pizza maker
    allowed_chars = "^[aestv0-9\s]*$" 
    user_toppings = [] #Place to put the toppings for the pizza
    pizza = [] #All data for the created pizza
    sizes = { #Pizza sizes (Includes Name and price)
        0: ['Tiny', 1.99],
        1: ['Small', 10.99],
        2: ['Medium', 12.99],
        3: ['Large', 14.99],
    }
    sauces = { #Pizza sauces (Includes Name and price)
        0: ["No Sauce", 0],
        1: ['Marinara sauce', 0], 
        2: ['Pesto sauce', 4.2],
        3: ['Alfredo sauce', 2.1],
        5: ['Garlic butter sauce', 1.5],
        6: ['White sauce', 0.9],
        7: ['Honey mustard sauce', 4.0],
        8: ['Tomato and basil sauce', 2.2],
    }
    cheeses = { #Pizza Cheeses (Includes Name and price)
        0: ["No Cheese", 0],
        1: ["Mozzarella", 0],
        2: ['Cheddar Cheese', 3.0],
        3: ['Parmesan Cheese', 4.0],
        4: ['Provolone Cheese', 2.8],
        5: ['Gouda Cheese', 3.5],
        6: ['Blue Cheese', 4.2],
        7: ['Feta Cheese', 3.8],
        8: ['Havarti Cheese', 3.6],
    }
    toppings = { #Pizza toppings (Includes Name and price)
        1: ['Pepperoni', 1.5],
        2: ['Mushrooms', 1.2],
        3: ['Onions', 1.0],
        4: ['Sausage', 1.8],
        5: ['Bacon', 2.0],
        7: ['Green Peppers', 1.2],
        8: ['Black Olives', 1.1],
        9: ['Pineapple', 1.3],
        10: ['Ham', 1.8],
        11: ['Jalapenos', 1.2],
        12: ['Spinach', 1.5],
    }
    #Nested functions
    def deliv_time(deliv_address): #For estimated deliv time
        pizza_ave = 114 #Ave for pizza place
        pizza_st = 68 #St for pizza place
        if 'st' in deliv_address: #Checks if the house is on a st or ave, and makes deliv_ave and deliv_st be the correct thing
            deliv_ave = int(deliv_address[:deliv_address.find(" ") - 2]) #First 2-3 numbers of address
            deliv_st = int(deliv_address[deliv_address.find(" "):deliv_address.find("s")]) #Numbers next to st
        elif 'ave' in deliv_address:
            deliv_st = int(deliv_address[:deliv_address.find(" ") - 2]) #First 2-3 numbers of address
            deliv_ave = int(deliv_address[deliv_address.find(" "):deliv_address.find("a")]) #Numbers next to ave
        ave_diff = pizza_ave - deliv_ave #calculates how many blocks away the house is from the pizza place
        st_diff = pizza_st - deliv_st #calculates how many blocks away the house is from the pizza place
        if ave_diff < 0: #Checks if the difference in blocks are negative 
            ave_diff = ave_diff * -1 
        if st_diff < 0: 
            st_diff = st_diff * -1 
        total_diff = ave_diff + st_diff #adds the difference in blocks
        time = 15 + (0.24 * total_diff) #calculates est_time and returns that number
        return time
    def clear():
        os.system('cls' if os.name =='nt' else 'clear')
    #Begining_Inputs
    clear()
    print ("Hello user")
    print ("Please enter your name, Address (i.e. 12345 67 St) and Phone number")
    user_name = input("Name: ").capitalize()
    user_address = input("Address (abreveate street or avenue): ").lower()
    while len(user_address) < 9 or len(user_address) > 16: user_address = input("Please enter a valid address: ") #checks if address is between 9 and 16 characters
    while string.punctuation in user_address: user_address = input("Please enter a valid address: ") #checks if there are punctuation in the input 
    while True: #checks if there are any dissallowed characters
        if re.match(allowed_chars, user_address): break
        user_address = input("Please enter a valid address (must only inculde st or ave): ")
    while True: #checks that st or ave are in the right place and its only st or ave
        space_pos = user_address.find(" ")
        user_address = user_address.replace(" ", "")
        if user_address.find("st") in [6,7,8]: 
            if re.match("^[st0-9\s]*$", user_address): break
            pass
        if user_address.find("ave") in [6,7,8]: 
            if re.match("^[ave0-9\s]*$", user_address): break
            pass
        user_address = input("Please enter a valid address (st or ave in wrong place or extra chars): ")
    user_address = user_address[:space_pos] + " " + user_address[space_pos:]
    while True: #checks if the address is only numbers(except for st/ave)
        space_pos = user_address.find(" ")
        user_address = user_address.replace(" ", "")
        if int(user_address[:user_address.find("st")]) != ValueError or int(user_address[:user_address.find("ave")]) != ValueError: 
            break
        user_address = input("Please enter a valid address (not an address): ")
    user_address = user_address[:space_pos] + " " + user_address[space_pos:]
    est_time = deliv_time(user_address)
    user_phone = input("Phone Number: ")

    #Pizza creator
    clear()
    print(dedent(f"""
    Hello {user_name}
    Please pick a pizza size from the following:
    
    1. Small $10.99
    2. Medium $12.99
    3. Large $14.99
    
    Input the number of the size you wish to have"""))
    ask = int(input("> "))
    while ask not in sizes:
        ask = int(input("Please try again: ")) #checks input to see if its an option
    pizza.append(sizes[ask]) #Adds the size and cost to pizza list
    clear()
    print(dedent(f"""
    Hello {user_name}
    Please pick a sauce from the following:
    
    0. No Sauce $0
    1. Marinara sauce $0
    2. Pesto sauce $4.20
    3. Alfredo sauce $2.10
    5. Garlic butter sauce $1.50
    6. White sauce $0.90
    7. Honey mustard sauce $4.00
    8. Tomato and basil sauce $2.20
    
    Input the number of the sauce you wish to have"""))
    ask = int(input("> "))
    while ask not in sauces:
        ask = int(input("Please try again: ")) #checks input to see if its an option
    user_toppings.append(sauces[ask]) #Adds the sauce and cost to toppings list
    clear()
    print(dedent(f"""
    Hello {user_name}
    Please pick a cheese from the following:
    
    0. No Cheese $0
    1. Mozzarella $0
    2. Cheddar Cheese $3.00
    3. Parmesan Cheese $4.00
    4. Provolone Cheese $2.80
    5. Gouda Cheese $3.50
    6. Blue Cheese $4.20
    7. Feta Cheese $3.80
    8. Havarti Cheese $3.60
    
    Input the number of the cheese you wish to have"""))
    ask = int(input("> "))
    while ask not in cheeses:
        ask = int(input("Please try again: ")) #checks input to see if its an option
    user_toppings.append(cheeses[ask]) #Adds the cheese and cost to toppings list
    
    while True:
        clear()
        print(dedent(f"""
        Hello {user_name}
        Please pick a topping from the following:

        0. Done
        1. Pepperoni $1.50
        2. Mushrooms $1.20
        3. Onions $1.00
        4. Sausage $1.80
        5. Bacon $2.00
        7. Green Peppers $1.20
        8. Black Olives $1.10
        9. Pineapple $1.30
        10. Ham $1.80
        11. Jalapenos $1.20
        12. Spinach $1.50

        Input the number of the topping you wish to have
        When done, input 0
        """))
        topping = int(input("> "))
        while topping not in toppings:
            if topping == 0: break
            topping = int(input("Please try again: ")) #checks input to see if its an option
        if topping == 0: break #If user inputs 0, end loop
        user_toppings.append(toppings[topping]) #Adds the topping and cost to toppings list
    pizza.append(user_toppings)
    return pizza, user_name, user_address, est_time

#Running the main function and printing out a recipt
if __name__ == "__main__":
    created_pizza, user, address, eta = pizza_app()

pizza_toppings = "\n".join(["   - " + created_pizza[1][x][0] for x in range(len(created_pizza[1]))]) #For each topping it joins the topping with - and \n to make -topping\n

for item in range(len(created_pizza[1])): topping_total += created_pizza[1][item][1] #Adds the cost up of each topping
pizza_sub = 20 + topping_total + created_pizza[0][1] #adds 20 with the sum of all toppings and pizza size cost
pizza_gst = round((pizza_sub * 0.05),2) #calculates how much gst will be (Alberta) (rounds to 2 decimal places)
pizza_total = round((pizza_sub + pizza_gst),2) #adds sub and gst together (rounds to 2 decimal places)

current_time = datetime.datetime.now() #Gets the current date and time
est_deliv_time = current_time + datetime.timedelta(minutes=eta) #adds estimated delivery time
est_deliv_time = est_deliv_time.time().replace(microsecond=0) #drops the date and gets rid of microseconds

os.system('cls' if os.name =='nt' else 'clear')
#recipt
print (f"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
{user}'(s) Pizza
--------------------------------
Size: {created_pizza[0][0]}
Toppings:
{pizza_toppings}
--------------------------------
Subtotal: {pizza_sub:.2f}
Gst: {pizza_gst:.2f}
Total: {pizza_total:.2f}
--------------------------------
Address: {address}
ETA: {est_deliv_time} ({eta} minutes)
If any of this info is incorrect
please call: 1-800-EDM-PIZZA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""")
