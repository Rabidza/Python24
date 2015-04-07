print "Welcome to the receipt program!"
total = 0
seat = ''
while True:
    if seat == 'q':
            break
    seat = raw_input("Enter the value for the seat ['q' to quit]: ")
    while not seat.replace('.', '').isdigit():
        if seat == 'q':
            break
        print "I;m sorry, but '{}' isn't valid. Please try again.".format(seat)
        seat = raw_input("Enter the value for the seat ['q' to quit]: ")

    if seat.replace('.', '').isdigit():
        total += float(seat)

print "*" * 5
print "Total: $", total
