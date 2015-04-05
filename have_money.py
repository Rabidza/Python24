try:
    bank_roll =  float(raw_input("Please enter your bank balance:\n"))
except:
    bank_roll = float(raw_input("Please enter a valid number!\n"))
if bank_roll > 0:
    print "You have money"
elif bank_roll == 0:
    print  "You're out"
else:
    print "You seem to be  in debt"
