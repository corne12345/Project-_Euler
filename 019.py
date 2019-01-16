# if a date is a certain day in one year, it is the next day in the following year,
# provided it is not a lap year. 1 Jan 1901 (day 1) is therefore a Tuesday

number_days = 100 * 365 + 25
print(number_days)
days = dict()
for i in range(1, number_days + 1):
    if i % 7 == 0:
        days[i] = 'Monday'
    if i % 7 == 1:
        days[i] = 'Tuesday'
    if i % 7 == 2:
        days[i] = 'Wednesday'
    if i % 7 == 3:
        days[i] = 'Thursday'
    if i % 7 == 4:
        days[i] = 'Friday'
    if i % 7 == 5:
        days[i] = 'Saturday'
    if i % 7 == 6:
        days[i] = 'Sunday'

print(days[36525])

first = 1
firsts=[]
for i in range(1, 101):
    jan = first
    feb = jan + 31
    if i % 4 == 0:
        mar = feb + 29
    else:
        mar = feb + 28
    apr = mar + 31
    may = apr + 30
    jun = may + 31
    jul = jun + 30
    aug = jul + 31
    sep = aug + 31
    okt = sep + 30
    nov = okt + 31
    dec = nov + 30
    first = dec + 31
    firsts += jan, feb, mar, apr, may, jun, jul, aug, sep, okt, nov, dec

counter = 0
first_days = dict()
print(len(firsts))
for k, v in days.items():
    if k in firsts and v == 'Sunday':
        first_days[k] = v
        counter += 1
print(counter)