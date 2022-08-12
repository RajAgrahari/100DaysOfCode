#wall painting
import math
def paint_wall(height, breadth, cover):
    num_of_cans = math.ceil((height*breadth)/coverage_per_can)
    print(f"NUMBER OF CANS REQUIRED:{num_of_cans}")

height = int(input("ENTER THE HEIGHT OF THE WALL:"))
breadth = int(input("ENTER THE BREADTH OF THE WALL:"))
coverage_per_can = int(input("ENTER THE COVERAGE AREA OF A CAN :"))
paint_wall(height, breadth, coverage_per_can)
