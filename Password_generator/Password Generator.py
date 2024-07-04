#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
choice = [1,2,3]

print("Welcome to the PyPassword Generator!!!")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
easy_password = " "
hard_password = " "
total = nr_numbers + nr_letters + nr_symbols
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(nr_letters):
    easy_password += letters[random.randint(1,52)]
for i in range(nr_numbers):
    easy_password +=  numbers[random.randint(1,9)]
for i in range(nr_symbols):
    easy_password += symbols[random.randint(1,8)] 
print("Easy Password: "+easy_password)
#Hard Level -# Order of characters randomised
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
n_count=0
l_count = 0
s_count=0
while(i<=total):
    c = choice[random.randint(0,2)]
    if  c == 1:
        if l_count < nr_letters:
            l_count +=1
            i+=1
            hard_password += letters[random.randint(1,53)]
    elif  c == 2:
        if n_count < nr_numbers:
            n_count +=1
            i+=1
            hard_password += numbers[random.randint(1,8)]
    elif  c == 3:
        if s_count < nr_symbols:
            s_count +=1
            i+=1
            hard_password += symbols[random.randint(1,8)] 
print("Hard password: "+ hard_password)