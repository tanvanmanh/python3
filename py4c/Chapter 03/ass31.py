# weekly hours
weeklyHours = 40
workHours = 0
overtimeHours = 0

# input hours and rate
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

# calculate overtime hours
if h > weeklyHours:
    workHours = weeklyHours
    overtimeHours = h - weeklyHours
else:
    workHours = h

# calculate pay
pay = ( workHours * r ) + ( overtimeHours * r * 1.5 )
print(pay)
