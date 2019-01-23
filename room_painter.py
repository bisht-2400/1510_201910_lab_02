#kshitiz bisht
#A01053490
#22-01-2019


def COVERAGE():
    return 400


length = float(input("Enter the length of room: "))
width = float(input("Enter the breadth of room: "))
height = float(input("Enter the height of room: "))
coat = int(input("No. of coat: "))
surface_area = 2*length*height+length*width+2*height*width
coverage_needed = coat*surface_area
cans_of_paint_required = coverage_needed/COVERAGE()


print("No. of cans you need to buy:", cans_of_paint_required)
