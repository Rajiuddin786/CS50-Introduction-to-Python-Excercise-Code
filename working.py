import re
import sys

def main():
    print(convert(input('Hours: ')))

def check_value_error(s):
    if not("to" in s):
        raise ValueError('Enter VAlid TIme')

def convert(s):
    check_value_error(s)
    check = re.search('^([0-9]{1,2}):?([0-9]{1,2})?\s?(AM|PM)\s?to\s?([0-9]{1,2}):?([0-9]{1,2})?\s?(AM|PM)$',s,re.IGNORECASE)
    if check:
        hour_first = int(check.group(1))
        if check.group(2):
            minute_first = int(check.group(2))
        else:
            minute_first = 0
        meridian1 = check.group(3)
        hour_second = int(check.group(4))
        if check.group(5):
            minute_second = int(check.group(5))
        else:
            minute_second = 0
        meridian2 = check.group(6)
        if 0 <= hour_first <= 12 and 0 <= int(minute_first) <= 60:
            if not(meridian1 == 'AM' or meridian1 == 'am'):
                if convert_hour1 != 12:
                    convert_hour1 = hour_first + 12
                else:
                    convert_hour1 = 12
            else:
                if convert_hour1 != 12:
                    convert_hour1 = hour_first
                else:
                    convert_hour1 = 0
        else:
            raise ValueError("Enter Correct Time")
        if 0 <= hour_second <= 12 and 0 <= int(minute_second) <= 60:
            if not(meridian2 == 'AM' or meridian2 == 'am'):
                if hour_second != 12:
                    convert_hour2 = hour_second + 12
                else:
                    convert_hour2 = 12
            else:
                if hour_second != 12:
                    convert_hour2 = hour_second
                else:
                    convert_hour2 = 0
        else:
            raise ValueError('Enter correct time')

        if convert_hour1 < 10:
            convert_hour_1 = '0'+str(convert_hour1)
        else:
            convert_hour_1 = str(convert_hour1)
        if minute_first < 10:
            minute_first_str = '0'+str(minute_first)
        else:
            minute_first_str = str(minute_first)
        if convert_hour2 < 10:
            convert_hour_2 = '0'+str(convert_hour2)
        else:
            convert_hour_2 = str(convert_hour2)
        if minute_second < 10:
            minute_second_str = '0'+str(minute_second)
        else:
            minute_second_str = str(minute_second)
        return_value = convert_hour_1+":"+minute_first_str+" to "+convert_hour_2+":"+minute_second_str
        return(return_value)






if __name__ == "__main__":
    main()