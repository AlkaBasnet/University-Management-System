import formulaz

print("Choose a shape/formula to calculate:")
print("1. Area of Triangle")
print("2. Area of Trapezium")
print("3. Area of Rectangle")
print("4. Surface Area of Sphere")
print("5. Volume of Cuboid")

shape = input("Enter your choice (1-5): ")

if shape == "1":
    print("\n-- Triangle Types --")
    print("1. Equilateral Triangle")
    print("2. Isosceles Triangle")
    print("3. Scalene Triangle")
    print("4. Any Triangle (Base & Height)")
    t_choice = input("Enter triangle type (1-4): ")

    if t_choice == "1":
        side = float(input("Enter side of equilateral triangle: "))
        print("Area:", formulaz.area_of_equilateral_triangle(side))

    elif t_choice == "2":
        base = float(input("Enter base of isosceles triangle: "))
        height = float(input("Enter height: "))
        print("Area:", formulaz.area_of_isosceles_triangle(base, height))

    elif t_choice == "3":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        print("Area:", formulaz.area_of_scalene_triangle(a, b, c))

    elif t_choice == "4":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area:", formulaz.area_of_triangle_base_height(base, height))

    else:
        print("Invalid triangle type.")

elif shape == "2":
    b1 = float(input("Enter base1: "))
    b2 = float(input("Enter base2: "))
    h = float(input("Enter height: "))
    print("Area of Trapezium:", formulaz.area_of_trapezium(b1, b2, h))

elif shape == "3":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle:", formulaz.area_of_rectangle(l, w))

elif shape == "4":
    r = float(input("Enter radius of sphere: "))
    print("Surface Area of Sphere:", formulaz.area_of_sphere(r))

elif shape == "5":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    print("Volume of Cuboid:", formulaz.volume_of_cuboid(l, w, h))

else:
    print("Invalid choice.")
