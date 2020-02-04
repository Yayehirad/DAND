# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:32:51 2020

@author: ymel0001
"""
#conda install -c anaconda mysql-connector-python
import mysql.connector
from mysql.connector import Error #show error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='root',
                                         password='078@yayu')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        #new one 
        
db=mysql.connector.connect(
        host='localhost',
       database='insta',
      user='root',
    password='078@yayu')
mycursor=db.cursor()
mycursor.excute("SELECT*FROM users")


print(5/0)


sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

print(san_francisco_pop_density>rio_de_janeiro_pop_density)
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length =len(given_name) + len(middle_names) + len(family_name) #todo: calculate how long this name is
print(len(given_name + middle_names + family_name))

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
arr[4:]
print(arr[len(arr)])

tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
#b.add(5)
#b.pop()

#Control flow
phone_balance=5
bank_balance=12
if phone_balance<5:
    phone_balance+=10
    bank_balance-=10
    
print(phone_balance)
if phone_balance<5:
    phone_balance+=10
    bank_balance-=10
    print("10$ charged")
elif phone_balance==5:
    phone_balance+=5
    bank_balance-=5
    print("5$ charged")
else:
    print("sufficient balance")

#prac 
points= 174
if points <=50:
    prize= "wooden rabit"
    print("Congragulations! You won a", prize, "!")
elif points <=150:
    prize= "no prize"
    print("Oh dear, no prize this time.")
elif points<=180:
    prize= "wafer-thin mint"
    print("Congragulations! You won a", prize, "!")
else:
    prize= "penguin"
    print("Congragulations! You won a", prize, "!")

#or
points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)


answer=15
guess=23

if guess > answer:
    print("oops! your guess is too high")
elif guess < answer:
    print("opps! your guess is too low")
else:
    print ("Nice! your guess matched the answer")
    


Solution: Guess My Number
answer = 35
guess = 30   # this is just a sample answer and guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
   result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"
print(result)

# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


points = 174

if points <= 50:
    prize= 'wooden rabit'
elif points <= 150:
    prize = None
elif points <= 180:
    prize = 'wafer-thin mint'
else:
    prize = 'penguin'

print(result)

if prize:
    result= " you won {}!".format(prize)
else:
    result="you didn't win any prize"
print(result)



cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)



usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)):
    usernames[index]=usernames[index].lower().replace(" ", "_")
# write your for loop here


print(usernames)


colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(color.lower())
    print(lower_colors)


cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key,value in cast.items():
    print(key,value)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key in 
#if the key is in the list of fruits, add the value (number of fruits) to result


print(result)

#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

print(result)
#solution
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
   if object in fruits:
       result += count

print("There are {} fruits in the basket.".format(result))
#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

print(result)

#solution
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))











































