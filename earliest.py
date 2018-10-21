def get_earliest(*args):
    earliest_date = args[0]
    earliest_date_int = convert_date_to_int(earliest_date)

    for date in args:
        current_date_int = convert_date_to_int(date)
        if current_date_int < earliest_date_int:
            earliest_date = date
            earliest_date_int = current_date_int

    return earliest_date


def convert_date_to_int(date):
    month, day, year = date.split('/')
    formatted_date = year + month + day
    return int(formatted_date)


