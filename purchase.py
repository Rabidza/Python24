name = raw_input("Give me your name, please: ")
quantity = int(raw_input("How many widgets are you buying? "))
cost = float(raw_input("How much do they  cost, per item? "))

print "Your total is ${}.".format(cost*quantity)
print "Thanks for shopping with us today, {}!".format(name)
