# A function that forms a list of date strings according
# to given start date and duration

def form_date_strs(startyear, startmonth, duration):

    date_strs = []
    year = startyear
    month = startmonth

    i = 0

    while i < duration:

        date_strs.append(str(year)+'-'+format(month, '02'))

        month += 1
        if month > 12:
            month = month - 12
            year = year + 1

        i = i + 1

    
    return date_strs
