
def area_rectangle(length, breadth):
    return length * breadth

def area_square(side):
    return side ** 2

def area_circle(radius):
    return 3.14 * radius * radius

def area_triangle(base,height):
    return 0.5 * base * height



def menu():
    print("\n_____ Area Operations _____")
    print("\n Select Operation to perform : \n\t1. Area Rectangle\n\t2. Area Square\n\t3. Area Circle\n\t4. Area Triangle\n\t5. Exit")

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
        result = area_rectangle(length,breadth)
        print(f"Area Of Rectangle : {result}")
    elif choice == '2':
        side = float(input("Enter The Side Of Square : "))
        print()
        result = area_square(side)
        print(f"Area Of Square : {result}")
    elif choice == '3':
        radius = float(input("Enter The Radius Of Cicle : "))
        print()
        result = area_circle(radius)
        print(f"Area Of Circle : {result}")
    elif choice == '4':
        base = float(input("Enter The Base Of Triangle : "))
        height = float(input("Enter The Height Of Triangle : "))
        print()
        result = area_triangle(base,height)
        print(f"Area Of Triangle : {result}")
    
    
    else:
        print("Invalid Input")
