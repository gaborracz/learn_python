def computepay(hours_float,rate_float):
    if hours_float > 40 :
        excess_hours = hours_float - 40
        extra_rate = rate_float * 1.5
        normal_hours_float = hours_float - excess_hours
        return((normal_hours_float * rate_float) + (excess_hours * extra_rate))
    else:
        return(hours_float * rate_float)

hours = input("Enter total worked hours: ")
rate = input("Enter rate: ")

hours_float = float(hours)
rate_float = float(rate)

print("Pay %r" % computepay(hours_float,rate_float))