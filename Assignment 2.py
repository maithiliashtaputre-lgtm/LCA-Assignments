#Q2
a, b, c = map(int, input("Enter 3 numbers: ").split())
if a >= b and a >= c:
    print("The largest number is", a)
elif b >= c and b >= a:
    print("The largest number is", b)
else:
    print("The largest number is", c)
