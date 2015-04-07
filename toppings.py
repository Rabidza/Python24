stock = ['pepperoni']
user_toppings = []

# should be using a loop for this exercise but the book has not covered this yet.
# trying to follow the book
user_choice = raw_input("Please give me a topping: ")
if user_choice in stock:
    print "We have {}".format(user_choice)
    user_toppings.append(user_choice)
else:
    print "Sorry, we don't have {}".format(user_choice)

user_choice_2 = raw_input("Please give one more topping: ")
if user_choice_2 in stock:
    print "We have {}".format(user_choice_2)
    user_toppings.append(user_choice_2)
else:
    print "Sorry, we don't have {}".format(user_choice_2)

print "Here are your toppings:"
print user_toppings
