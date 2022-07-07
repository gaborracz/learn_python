hours = input("Enter the total worked hours: ")
rate = input("Enter the rate: ")

#convert input to float

hours_float = float(hours)
rate_float = float(rate)

if hours_float > 40 :
    excess_hours = hours_float - 40
    extra_rate = rate_float * 1.5
    normal_hours_float = hours_float - excess_hours
    print((normal_hours_float * rate_float) + (excess_hours * extra_rate))
else:
    print(hours_float * rate_float)