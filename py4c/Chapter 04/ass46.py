def computepay(h,r):
    p = 0
    if h > 40:
        p = 40 * r + (h - 40) * r * 1.5
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except Exception as e:
    print("Please enter only number!")
    quit()

p = computepay(h, r)
print("Pay",p)
