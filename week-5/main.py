from datetime import datetime
from time import sleep
import webbrowser

string_compare = False
object_compare = False

time_string_to_compare = ""
date_to_compare = datetime.now()

string_or_object = input("The current time is: {}\n"
                         "Select your alarm clock type (s|o): ".format(datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")))
if string_or_object is "s":
    # string comparison
    time_string_to_compare = input("Type what time you want the alarm to go off at "
                                   "(month/day/year minute:hour:second am/pm): ")
    string_compare = True

elif string_or_object is "o":
    # object comparison
    object_compare = True
    month = input("Type the month: ")
    day = input("Type the day: ")
    year = input("Type the year: ")
    hour = input("Type the hour: ")
    minute = input("Type the minute: ")
    second = input("Type the second: ")
    ampm = input("AM or PM?: ")

    date_to_compare = datetime.strptime('{}/{}/{} {}:{}:{} {}'.format(day, month, year, hour, minute, second, ampm),
                                        '%d/%m/%Y %I:%M:%S %p')

while 1:
    now = datetime.now()
    now = now.replace(microsecond=0)
    fancy_date_time = now.strftime("%m/%d/%Y %I:%M:%S %p")
    if string_compare:
        if fancy_date_time == time_string_to_compare:
            print("Alarm!")
            webbrowser.open("https://www.youtube.com/watch?v=T-L4R98z1Ao&feature=youtu.be&t=18")
            break
    elif object_compare:
        if date_to_compare.timestamp() == now.timestamp():
            print("Alarm!")
            webbrowser.open("https://www.youtube.com/watch?v=T-L4R98z1Ao&feature=youtu.be&t=18")
            break
    print(fancy_date_time, end='')
    sleep(1)
    print('\r', end='')


# \n
# \r\n