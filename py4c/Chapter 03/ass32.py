score = input("Enter Score: ")
floatScore = float(score)
if floatScore <= 0:
    print("Please input value between 0.1 and 1.0")
elif floatScore < 0.6:
    print("F")
elif floatScore < 0.7:
    print("D")
elif floatScore < 0.8:
    print("C")
elif floatScore < 0.9:
    print("B")
elif floatScore <= 1.0:
    print("A")
else:
    print("Please input value between 0.1 and 1.0")
