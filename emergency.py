email = raw_input("Enter your email text here:\n")

if email.find('emergency') == 0:
     print "Do you want to make this email urgent?"
elif email.find('joke') == 0:
     print "Do you want to set this email as non-urgent?"
else:
    print "Mail sent, without special instructions"

