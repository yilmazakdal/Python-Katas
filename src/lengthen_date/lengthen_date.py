from datetime import datetime
def lengthen_date(date):
    try:
        converted_date = datetime.strptime(date,"%d.%m.%Y")
        day = int(converted_date.strftime('%d'))
        suffix  = suffixes(day)
        output_date = converted_date.strftime(f'%A %-d{suffix} %B %Y')
        return output_date
    except:
        return "Invalid date"

def suffixes(number):
    suffix = ["th", "st", "nd", "rd"]
    if number % 10 in [1, 2, 3] and number not in [11, 12, 13]:
        return suffix[number % 10]
    else:
        return suffix[0]