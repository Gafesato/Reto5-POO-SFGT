from shape.point import Point
from shape.rectangle import Rectangle
from shape.trirectangle import TriRectangle

def main():
    p1 = Point(0, 0)
    p2 = Point(10, 0)
    p3 = Point(10, 5)
    p4 = Point(0, 5)

    rectangle = Rectangle(1, p1, p2, p3, p4)
    print(f"Área del rectángulo: {rectangle.compute_area()}")
    print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()}")
    print(f"Ángulos internos del rectángulo: {rectangle.compute_inner_angles()}")
    
    trirectangle = TriRectangle(1, p1, p2, p4)
    print(f"Área del triángulo rectángulo: {trirectangle.compute_area()}")
    print(f"Ángulos internos del triángulo rectángulo: {trirectangle.compute_inner_angles()}")

if __name__ == '__main__':
    main()