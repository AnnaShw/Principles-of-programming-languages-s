# Emplementation with dispatch function
def shmeasy_park(fee):
    balance = 0

    def charge(amount):
        nonlocal balance
        balance += amount

    def park(time):
        nonlocal balance
        balance -= time * fee
        return 'balance left:' + str(balance)

    def dispatch(message, args):
        if message == 'charge':
            return charge(args)
        elif message == 'park':
            return park(args)
        else:
            return 'unknown message:' + message

    return dispatch


##mblementation with dispatch dictionaty
##def shmeasy_park(fee):
##        balance = 0

##        def charge(amount):
#       nonlocal balance
##           balance += amount

##   def park(time):
##        nonlocal balance
##         balance -= time * fee
##         return 'balance left:' + str(balance)

##  return {"charge":charge,"park":park}


##-----------------------------------------------------------------------------------------
# k = shmeasy_park(5)
# k('charge', 100)
# print(k('park', 10))
# print(k('add', 20))
##-----------------------------------------------------------------------------------------
class Time():
    # constructor
    def __init__(self, h=0, m=0, s=0):
        """

        :param h: hours
        :param m: minutes
        :param s: seconds
        """
        if 0 <= h <= 23:
            self.hour = h
        else:
            self.hour = s
        if 0 <= m <= 59:
            self.minutes = m
        else:
            self.minutes = s
        if 0 <= s <= 59:
            self.seconds = s
        else:
            self.seconds = s

    # print clock in fortmat 03:09:45
    def printTime(self):
        print('%02d:%02d:%02d' % (self.hour, self.minutes, self.seconds))

    def TimeToInt(self):
        """
        Convert current hour into second's that passed from midnight
        :return: second's that passed from midnight
        """
        return self.seconds + self.minutes * 60 + self.hour * 3600

    def Later(self, object):
        """

        :param object: another clock object
        :return: true if current clock(self) bigger than object clock
        """
        if self.hour > object.hour:
            return True
        elif self.hour < object.hour:
            return False
        else:
            if self.minutes > object.minutes:
                return True
            elif self.minutes < object.minutes:
                return False
            else:
                if self.seconds > object.seconds:
                    return True
                elif self.seconds < object.seconds:
                    return False

    def UpdateClock(self, sec):
        """
        This function update clock
        :param sec:new clock in seconds
        :return:
        """
        minutes, seconds = divmod(sec, 60)
        hour, minutes = divmod(minutes, 60)
        hour = hour % 24
        return Time(hour, minutes, seconds)

    def addSecond(self):
        """
        increase second's by one
        :return: second's+=1
        """
        return self.UpdateClock(self.TimeToInt() + 1)

    def __add__(self, obj):
        """
        Receives a current clock and another clock, add the clock data and inserts the character into the current clock
        :param obj: another clock
        :return:the result of adding the time of two clock's
        """
        return self.UpdateClock(self.TimeToInt() + obj.TimeToInt())

    def __sub__(self, number_of_sec):
        """
        Receives a current clock and a number of seconds, deducts the number of seconds from the current clock data and updates  current clock
        :param number_of_sec: number of second than we need to reduce from current clock
        :return: Updated clock
        """
        return self.UpdateClock(self.TimeToInt() - number_of_sec)

    def from_clock_to_str_clock(self):
        """
        A function that converts the watch object into a string that contains all the object details in the format hh:mm:ss
        :return:string
        """
        return '%02d:%02d:%02d' % (self.hour, self.minutes, self.seconds)


start = Time(9, 45, 0)
end = Time(1, 35, 0)
test = Time(1, 10, 15)
start.printTime()  # 09:45:00
print('----------')
Time.printTime(start)
print('----------')
print(start.Later(end))  # True
print(test.TimeToInt())  # 4215
help = test.UpdateClock(4215)
help.printTime()  # 01:10:15
help.addSecond()
help.printTime()  # 01:10:16
(start + end).printTime()  # 09:45:00 + 01:35:00 = 11:20:00
(help - 5).printTime()  # 01:10:11
print(help.__str__())


class TimeZone(Time):
    # constructor
    def __init__(self, h=0, m=0, s=0, zone_name='Jerusalem'):
        Time.__init__(self, h, m, s)
        self.zone_name = zone_name

    def print_zone_information(self):
        print(self.zone_name)
        Time.printTime(self)


child = TimeZone(10, 5, 34, 'Montreal')
zt = TimeZone(10, 55, 34)  # 10:55:34 \n Jerusalem
print('----------')
zt.print_zone_information()
print('----------')
child.print_zone_information()
