#Imports
from textwrap import dedent
import datetime
import os
#Inputs
user_name = None
user_address = None
user_phone = None
# Pizza variables
size = None
sauce = None
cheese = None
user_toppings = []
pizza = []
#Dicts
sizes = {
    0: ['Tiny', 1.99],
    1: ['Small', 10.99],
    2: ['Medium', 12.99],
    3: ['Large', 14.99]
}
#Variables
pizza_address = '11430 68 St NW' #Addres of Eastglen (Pizza Place)
#Functions
def deliv_time(deliv_address):
    pizza_ave = 114 # ave and st used for math later 
    pizza_st = 68 
    # deliv_address = ''.join(deliv_address.split())
    deliv_address = deliv_address.replace(" ", "")
    deliv_address = deliv_address.lower() #gets rid of white space and makes all the text lowercase
    #Checks if house is on a street or address
    if 'st' in deliv_address: #if on st
        deliv_ave = int(deliv_address[:3])
        deliv_st = int(deliv_address[5:7]) #the ave for the house is taken form the first 3 characters and the st is taken from the 6th and 7th
    elif 'ave' in deliv_address: #if on ave
        deliv_st = int(deliv_address[:2])
        deliv_ave = int(deliv_address[4:7]) #the st for the house is taken form the first 2 characters and the st is taken from the 5th and 6th
    ave_diff = pizza_ave - deliv_ave #calculates difference in the ave and st
    st_diff = pizza_st - deliv_st 
    if ave_diff < 0:
        ave_diff = ave_diff * -1 #checks if number is negative and turns it positive if it is ⇊
    if st_diff < 0: 
        st_diff = st_diff * -1 
    total_diff = ave_diff + st_diff #adds both diffs together to get total diff
    time = 15 + (0.2 * total_diff) #calculates a rough delivery time (seconds)
    return time

def clear():
    os.system('cls' if os.name =='nt' else 'clear')
# Proccesing
clear()
print ("Hello")
print ("Please enter your name, Address (i.e. 12345 67 St NW) and Phone number")
user_name = input("Please enter your Name: ").capitalize()
user_address = input("Please enter your Address: ")
while True:
    if len(user_address) >= 11:
        break
    user_address = input("Please enter a valid Address: ")
user_phone = input("Please enter your Phone Number: ")
est_time = deliv_time(user_address)
clear()
print (f"Hello, {user_name}")
print (dedent("""Please Pick a pizza size from the following:
    1: Small $10.99
    2: Medium $12.99
    3: Large $14.99
    
    Please input the number next to the size you want"""))
