def h_formula():
    height=int(input("hight of triangle :"))
    base=int(input("base of triangle :"))
    formula=(height*base)/2
    return formula
print(f"area of tringle :{h_formula()}\n")

def area_square():
    side=int(input("side :"))
    s_formula=side**2
    return s_formula
print(f"area of square is :{area_square()}\n")

def area_rectangle():
     length=int(input ("length of rectangle :"))
     width=int(input("width of rectangle : "))
     r_formula=length*width
     return r_formula
print(f"area of rectangle is : {area_rectangle()}\n")

def area_circle():
    radius=int(input("radius :"))
    c_formula=3.14%radius
    return c_formula
print(f"area of circle : {area_circle()}\n")

def area_trapezium():
    base1=int(input("base 1 :" ))
    base2=int(input("base 2 :" ))
    height=int(input("height : "))
    t_formula=base1+base2/2*height
    return t_formula
print(f"area of trapezium is : {area_trapezium()}\n")







    
