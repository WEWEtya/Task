#Program Function
a = -4.5
x = float(input("Enter the number= "))
if x > 0:
    y = 4.7 * x + 3.6 / x
    print("Y= ",y)
elif x > -5 and x < 0:
    y = (1 + x) / 1 - x**4
    print("Y= ",y)
elif x < -5:
    y = 8 * x**3 + a
    print("Y= ",y)