import re
import sys

def main():
    print(convert(input('Hours: ')))

def convert(s):
    if 'to' in s:
        check = re.search('^([0-9]{1,2}):?([0-9]{1,2})?\s?(AM|PM)\s?to\s?([0-9]{1,2}):?([0-9]{1,2})?\s?(AM|PM)$',s,re.IGNORECASE)
        if check:
            hour_first = int(check.group(1))
            if check.group(2):
                if not(check.group(2) == '00')
                     minute_second = int(check.group(2))
                else:
                    minute_second = '00'
            else:
                minute_first = '00'
            meridian1 = check.group(3)
            hour_second = int(check.group(4))
            if check.group(5):
                if not(check.group(5) == '00')
                    minute_second = int(check.group(5))
                else:
                    minute_second = '00'
            else:
                minute_second = '00'
            meridian2 = check.group(6)
            if 0 <= hour_first <= 12 and 0 <= int(minute_first) <= 60:
                if not(meridian1 == 'AM' or meridian1 == 'am'):
                    convert_hour1 = hour_first + 12
                    convert_hour_1 = str(convert_hour1)
                else:
                    convert_hour_1 = '0'+str(hour_first)
            else:
                raise ValueError("Enter Correct Time")
            if 0 <= hour_second <= 12 and 0 <= int(minute_second) <= 60:
                if not(meridian2 == 'AM' or meridian2 == 'am'):
                    convert_hour2 = hour_second + 12
                    convert_hour_2 = str(convert_hour2)
                else:
                   convert_hour_2 = '0'+str(hour_second)

            else:
                raise ValueError('Enter correct time')
            return_value = convert_hour_1+":"+str(minute_first)+" to "+convert_hour_2+":"+str(minute_second)
            return(return_value)
        else:
            return('')
    else:
        raise ValueError('Enter Valid Time')








if __name__ == "__main__":
    main()