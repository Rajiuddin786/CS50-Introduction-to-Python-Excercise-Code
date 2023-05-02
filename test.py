def get_date():
    date = input('Enter a date (MM/DD/YYYY or Month Day, Year): ').strip()
    try:
        # try to convert input to YYYY-MM-DD format
        date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError:
        try:
            date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
        except ValueError:
            # if input cannot be converted to YYYY-MM-DD format, prompt user to enter a valid date
            print('Invalid date format. Please enter a date in either MM/DD/YYYY or Month Day, Year format.')
            date = get_date()  # recursively call get_date() until a valid date is entered
    return date

date = get_date()
print(date)
