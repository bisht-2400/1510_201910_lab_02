#kshitiz bisht
#A01053490
#22-01-2019
PI = 3.14159
radius = float(input("Enter the radius:"))
circumference = 2*PI*radius
area = PI*radius*radius
double_radius = 2*radius
circumference_new = double_radius*PI*2
area_new = PI*double_radius*double_radius
comp_btw_circum = circumference_new/circumference
comp_btw_area = area_new/area

print("Circumference of the circle is :",circumference)
print("Area of the circle is:",area)
print("The doubles Radius is:",double_radius)
print("New circumference is",comp_btw_circum,"times the old circumference and the new circumference is:",circumference_new)
print("New area is", comp_btw_area, "times the old area and the new area is:",area_new)
