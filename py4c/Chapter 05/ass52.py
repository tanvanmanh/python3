largest = None
smallest = None
value = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try:
        value = int(num)
    except Exception as e:
        print("Invalid input")
        continue

    if largest is None and smallest is None:
        largest = value
        smallest = value
    elif value < smallest:
        smallest = value
    elif value > largest:
        largest = value    

print("Maximum is", largest)
print("Minimum is", smallest)
