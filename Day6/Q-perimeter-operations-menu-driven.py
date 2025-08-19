
def perimeter_rectangle(length, breadth):
    return 2 * (length + breadth)

def perimeter_square(side):
    return 4*side

def perimeter_circle(radius):
    return 2 * 3.14 * radius

def perimeter_triangle(side):
    return 3 * side



def menu():
    print("\n\t_____ Area Operations _____")
    print("\n Select Operation to perform : \n\t1. Perimeter Rectangle\n\t2. Perimeter Square\n\t3. Perimeter Circle\n\t4. Perimeter Triangle\n\t5. Exit")

while True:
    menu()
    choice = input("Enter Your Choice : ")
    print()
    if choice == '5':
        print("Exiting the program .......")
        break
    elif choice == '1':
        length = float(input("Enter The Length Of Rectangle : "))
        breadth = float(input("Enter The Breadth Of Rectangle : "))
        print()
        result = perimeter_rectangle(length,breadth)
        print(f"Perimeter Of Rectangle : {result}")
    elif choice == '2':
        side = float(input("Enter The Side Of Square : "))
        print()
        result = perimeter_square(side)
        print(f"Perimeter Of Square : {result}")
    elif choice == '3':
        radius = float(input("Enter The Radius Of Cicle : "))
        print()
        result = perimeter_circle(radius)
        print(f"Perimeter Of Circle : {result}")
    elif choice == '4':
        side = float(input("Enter The Side Of Square : "))
        print()
        result = perimeter_triangle(side)
        print(f"Perimeter Of Triangle : {result}")
    
    
    else:
        print("Invalid Input")
