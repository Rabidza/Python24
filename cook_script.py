# This is Hour9's example cook script

def get_specials():
    monday = {'B': 'Horseradsish omelete. Note better than it sounds',
              'L': 'Momma\'s Curry. Note: Can be made spicy.',
              'D': 'Beef brisket. Note: Comes with au jus. That\'s procounced "Oh jhoo", not "Ow Juice"'}
    tuesday = {'B': 'Sausage gravy over biscuits. Note: Toast can be subbed',
               'L': 'Grilled cheese and tomato soup. Note: We have vegan cheese.',
               'D': 'Meatloaf. Note: Comes with catsup on the top. Not optional'}
    wednesday = {'B': 'Horseradsish omelete. Note better than it sounds',
                 'L': 'Momma\'s Curry. Note: Can be made spicy.',
                 'D': 'Beef brisket. Note: Comes with au jus. That\'s procounced "Oh jhoo", not "Ow Juice"'}
    thursday = {'B': 'Horseradsish omelete. Note better than it sounds',
                'L': 'Momma\'s Curry. Note: Can be made spicy.',
                'D': 'Beef brisket. Note: Comes with au jus. That\'s procounced "Oh jhoo", not "Ow Juice"'}
    friday = {'B': 'Horseradsish omelete. Note better than it sounds',
              'L': 'Momma\'s Curry. Note: Can be made spicy.',
              'D': 'Beef brisket. Note: Comes with au jus. That\'s procounced "Oh jhoo", not "Ow Juice"'}
    saturday = {'B': 'Horseradsish omelete. Note better than it sounds',
                'L': 'Momma\'s Curry. Note: Can be made spicy.',
                'D': 'Beef brisket. Note: Comes with au jus. That\'s procounced "Oh jhoo", not "Ow Juice"'}
    sunday = {'B': 'Horseradsish omelete. Note better than it sounds',
              'L': 'Momma\'s Curry. Note: Can be made spicy.',
              'D': 'Beef brisket. Note: Comes with au jus. That\'s procounced "Oh jhoo", not "Ow Juice"'}

    specials = {'M': monday,
                'T': tuesday,
                'W': wednesday,
                'R': thursday,
                'F': friday,
                'ST': saturday,     # NH - I had to make this upper case to work
                'SN': sunday}       # NH - I had to make this upper case to work
    return specials

def print_special(special):
    print "The special is:"
    print special
    print "*" * 15

def get_day():
    while True:
        day = raw_input("Day (M/T/W/R/F/St/Sn: ")
        if day.upper() in ['M','T','W','R','F','ST','SN']:
            return day.upper()
        else:
            print "I'm sorry, but {} isn't valid.".format(day)

def get_time():
    while True:
        time = raw_input("Time (B/L/D): ")
        if time.upper() in ['B', 'L', 'D']:
            return time.upper()
        else:
            print "I'm sorry, but {} isnt't a valid time.".format(time)

def main():
    specials = get_specials()
    print "This script will tell you the specials for any day of the week, and time."
    while True:
        day = get_day()
        special = specials[day]
        time = get_time()
        print_special(special[time])
        another = raw_input("Do you want to check another day and time? (Y/N)")
        if another.lower() == 'n':
            break

if __name__ == '__main__':
    main()
