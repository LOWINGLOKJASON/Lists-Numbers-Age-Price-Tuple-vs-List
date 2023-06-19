#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/otmybengqf-lowinglokjason
#****************************************************************

#############
#Question #1
#############

## set an empty list for item_list, create 10 items in a list
items_list = []
items = ['clothing', 'shoes', 'backpack', 'sunscreen', 'laptop', 'phone', 'food', 'beverage', 'passport', 'boating documents']

## print out a list of the items using a for loop which iterates a number at the beginning of each sentence

for i in range(10):
    print(f'Item {i+1} is {items[i]}')
else:
    print('Please take all the items')
  
## Following the loop, print a statement outside of the loop reminding Bill to make sure he takes all the items.

print('Please make sure to take all the listed items, thank you.')

## Copy all items to a new list and remove five of the items. Print out both lists.

new_items = items.copy()
del new_items[5:]
print('New List', new_items)
print('Original List', items)

#############
#Question #2
#############

## Make a list of the number 1 to 1000 and use a for loop using range() to print the numbers
## From the range, 1 is the starting numbers and 1001 is the ending point which will selcet the previous number as ending number

numbers = []
for number in range(1, 1001):
  numbers.append(number)
print(numbers)

## find the smallest number
print(min(numbers))

## find the largest number
print(max(numbers))

## find the combined total number
print(sum(numbers))

#############
#Question #3
#############

## make a list of odd numbers between 1 and 40
odds = []
for odd in range(1, 41, 2):
  odds.append(odd)
print(odds)

## make a list of even numbers between 1 and 40
evens = []
for even in range(2, 41, 2):
  evens.append(even)
print(evens)

## make a list of the multiples of 3 from 3 to 30
multiples = []
for multiple in range(3, 31, 3):
  multiples.append(multiple)
print(multiples)

#############
#Question #4
#############

## let my age as 24 years old
my_age = 24

## create the dog year when dogs age 7 times faster than humans
dog_year = my_age*7

## create a sentence showing my 
sentence = ('My age', 'in', 'dog years', 'equal to', str(dog_year))

## create a separator and join it to the sentence
separator = ' '
print(separator.join(sentence))

#############
#Question #5
#############

## store the prices of nine items from a pizza store in a list
prices = [12.99, 5.99, 7.99, 10.99, 9.59, 4.99, 6.79, 8.99, 10.25]

## print out sentences using an fstring calculating the total combined price from the first three list entries
print(f'The toatl price of the first three list entries are {sum(prices[:3])}.')

## print out sentences using an fstring calculating the total combined price from the middle three list entries
print(f'The toatl price of the middle three list entries are {sum(prices[3:6])}.')

## print out sentences using an fstring calculating the total combined price from the last three list entries
print(f'The toatl price of the last three list entries are {sum(prices[-3:])}.')

#############
#Question #6
#############

## Make a list of five foods from KFC
kfc_foods = ('hot wings', 'drumstick', 'poutine', 'popcorn chicken', 'twister')

## Use a for loop to print each one of the foods
for food in kfc_foods:
  print(food)

## replace two of the items in your list by overwriting the tuple
kfc_foods = ('sandwich', 'drumstick', 'poutine', 'gravy', 'twister')
print(kfc_foods)

## a tuple is an unchangable after created, it can't be amended unless it is replaced by a new tuple. But elements in a list can be modified without creating a new list. thus, here is the difference amid a tuple and a list.