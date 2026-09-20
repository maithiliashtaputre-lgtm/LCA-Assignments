#Q3
a , b , c = map(int, input("Enter Three Sides: ").split())
def right_triangle(a,b,c):
    sides = sorted([a,b,c])

    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        print("The triangle is a right-angled triangle")
    else:
        print("The triangle is not a right-angled triangle")

right_triangle(a,b,c)