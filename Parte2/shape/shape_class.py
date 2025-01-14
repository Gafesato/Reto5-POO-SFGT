import math

from shape.line import Line
from shape.point import Point
from shape.vector import Vector

class Shape:
    def __init__(self, method: int, *args) -> None:
        """Inicializar Shape con vértices o aristas."""
        self.vertices: list["Point"] = []
        self.edges: list["Line"] = []
        self.__method: int = method

        # Inicialización con vértices
        if method == 1:
            for i in range(len(args)):
                vertice: "Point" = args[i]
                self.vertices.append(vertice)
                edge: "Line" = Line(vertice, args[(i + 1) % len(args)])
                self.edges.append(edge)

        # Inicialización con aristas
        elif method == 2:
            for edge in args:
                self.edges.append(edge)
                if edge.start_point not in self.vertices:
                    self.vertices.append(edge.start_point)
                if edge.end_point not in self.vertices:
                    self.vertices.append(edge.end_point)

        else:
            raise ValueError("No se seleccionó ningún método.")

    def get_method(self):
        return self.__method

    def set_method(self, new_method):
        self.__method == new_method

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    def compute_perimeter(self) -> float:
        """Retorna la suma de las longitudes de cada arista de la figura."""
        return sum(edge.length for edge in self.edges)
    
    def compute_inner_angles(self) -> list[float]:
        """Calcula los ángulos en cada vértice."""
        angles = []
        n = len(self.vertices)
        for i in range(n):
            p1 = self.vertices[i - 1]
            p2 = self.vertices[i]
            p3 = self.vertices[(i + 1) % n]

            # Creo la clase Vector para facilitar el cálculo
            # de los ángulos
            v1 = Vector(p2, p1)
            v2 = Vector(p2, p3)

            cos_theta = v1.scalar_product(v2) / (v1.norm() * v2.norm())
            angle = math.degrees(math.acos(cos_theta))
            angles.append(angle)
        return angles

    def __str__(self) -> str:
        """Mostrar una representación agradable de la figura en cuestión."""
        output = "Vértices: "
        for vertice in self.vertices:
            output += f'[({vertice.x},{vertice.y})] '
        output += "\nAristas: "
        for edge in self.edges:
            output += f'[({edge.start_point.x}),({edge.start_point.y})] -> [({edge.end_point.x}),({edge.end_point.y})]]  '
        return output