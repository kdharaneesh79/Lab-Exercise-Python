# Area Calculation

print("Choose a shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
choice = input("Enter your choice (1-3): ")

if choice == "1":
    radius = float(input("Enter radius: "))
    area = 3.14159 * radius * radius
    print("Area of circle:", area)
elif choice == "2":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of rectangle:", area)
elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of triangle:", area)
else:
    print("Invalid choice.")