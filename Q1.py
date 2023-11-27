# 1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

height=float(input("Enter The Height\n"))
print(f"Height of A Rectangle ={height}\n")

width=float(input("Enter The Width \n"))
print(f"Width of A Rectangle ={width}\n")


AREA=(height*width)
print(f"AREA of Rectangle ={AREA}")
print(f"type of AREA = {type(AREA)}\n")

Peri=2*(height+width)
print(f"Perimeter of Rectangle ={Peri}")
print(f"type of Perimeter = {type(Peri)}\n")

