

def area_rectangle(length,breadth):
    area_result = length * breadth
    print("Area Of Rectangle : ",area_result)

def perimeter_rectangle(length,breadth):
    perimeter_result = 2 * (length + breadth)
    print("Perimeter Of Rectangle : ",perimeter_result)

def area_square(side):
    area_result = side ** 2
    print("Area Of Square : ",area_result)

def perimeter_square(side):
    perimeter_result = 4 * side 
    print("Perimeter Of Square : ",perimeter_result)



length = int(input("Enter the length of rectangle"))
breadth = int(input("Enter the breadth of rectangle"))



area_rectangle(length,breadth)